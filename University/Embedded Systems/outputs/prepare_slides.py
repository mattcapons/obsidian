from pathlib import Path
import concurrent.futures
import hashlib
import json
import re
import subprocess
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT.parents[1]
OUT = ROOT / 'outputs'
inventory = json.loads((OUT / 'inventory.json').read_text())
FONT = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 22)

def prepare(entry):
    source = VAULT / entry['source']
    images = ROOT / 'Attachments' / entry['group'] / entry['stem']
    if any(images.glob('slide-*.png')):
        raise RuntimeError(f'Existing slide images must be compared and preserved before revision: {images}')
    images.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(['mutool', 'draw', '-q', '-b', 'MediaBox', '-w', '3200', '-h', '3200', '-o', str(images/'slide-%03d.png'), str(source)], capture_output=True, text=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    xml = subprocess.run(['mutool', 'draw', '-q', '-F', 'stext', str(source)], capture_output=True, text=True, check=True).stdout
    xml_path = OUT / 'structured-text' / entry['group'] / (entry['stem']+'.xml')
    xml_path.parent.mkdir(parents=True, exist_ok=True)
    xml_path.write_text(xml)
    pages = []
    plain_pages = Path(entry['text']).read_text().split('\f')
    for n, page in enumerate(ET.fromstring(xml).findall('page'), 1):
        width, height = float(page.attrib['width']), float(page.attrib['height'])
        lines = []
        for line in page.findall('.//line'):
            chars = line.findall('.//char')
            text = ''.join(c.attrib.get('c', '') for c in chars).strip()
            if not text:
                continue
            bbox = [float(v) for v in line.attrib['bbox'].split()]
            size = max([float(f.attrib['size']) for f in line.findall('font')] or [0])
            lines.append({'text': text, 'bbox': bbox, 'font_size':size})
        candidates = [l for l in lines if l['bbox'][1] < height*.24 and l['font_size'] >= 15 and not re.search(r'©|prof\.|politecnico|william\.|AA 20', l['text'], re.I)]
        if candidates:
            first = max(candidates, key=lambda x:x['font_size'])
            title = first['text']
        else:
            title = next((l['text'] for l in lines if len(l['text']) > 5 and not re.search(r'©|http|^\d+/\d+/\d+',l['text'])),entry['stem'])
        footer = [l['text'] for l in lines if l['bbox'][1] > height*.88 and re.fullmatch(r'\d{1,3}', l['text'])]
        header = [l['text'] for l in lines if l['bbox'][1] < height*.07 and re.fullmatch(r'\d{1,3}', l['text'])]
        printed = (footer or header or [None])[0]
        png = images / f'slide-{n:03}.png'
        with Image.open(png) as im:
            pixel_size = list(im.size)
        pages.append({'page':n,'title':title,'printed_number':printed,'width_pt':width,'height_pt':height,'image':str(png.relative_to(VAULT)), 'image_size':pixel_size,'text_sha256':hashlib.sha256(plain_pages[n-1].encode()).hexdigest(),'lines':lines})
    sheets = OUT / 'review' / entry['group'] / entry['stem']
    sheets.mkdir(parents=True,exist_ok=True)
    for start in range(0,len(pages),6):
        subset = pages[start:start+6]
        sheet = Image.new('RGB',(2000, 3*825),(222,224,228))
        draw = ImageDraw.Draw(sheet)
        for slot,p in enumerate(subset):
            x,y = (slot%2)*1000,(slot//2)*825
            label = f"PDF {p['page']:03}: {p['title']}"
            draw.text((x+12,y+10),label[:75],font=FONT,fill='black')
            with Image.open(VAULT/p['image']) as slide:
                slide.thumbnail((984,775),Image.Resampling.LANCZOS)
                sheet.paste(slide,(x+(1000-slide.width)//2,y+45+(775-slide.height)//2))
        sheet.save(sheets/f'review-{start+1:03}-{start+len(subset):03}.jpg',quality=92)
    entry['image_folder'] = str(images.relative_to(VAULT))
    entry['page_data'] = pages
    entry['render_warnings'] = result.stderr.strip()
    print(f"Rendered {entry['stem']}: {len(pages)} pages",flush=True)
    return entry

if __name__=='__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        inventory = list(pool.map(prepare,inventory))
    (OUT/'source-map.json').write_text(json.dumps(inventory,indent=2,ensure_ascii=False))
    print('DONE',sum(e['pages'] for e in inventory),flush=True)
