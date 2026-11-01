from pathlib import Path
import re, zlib, hashlib, json

root = Path('University/Advanced Algorithms and Parallel Programming')
out = Path('outputs/performance-review-2026-11-01')
bank = (root / 'Past Exam Question Bank.md').read_text()
section = bank.split('### AAPP-02-008\n', 1)[1].split('## PRAM algorithms', 1)[0]
names = list(dict.fromkeys(re.findall(r'Source: \[\[([^#]+\.pdf)', section)))
records = []

for name in names:
    data = (root / 'Old Exams' / name).read_bytes()
    objs = {int(m[1]): m[2] for m in re.finditer(rb'(\d+)\s+\d+\s+obj\b(.*?)endobj', data, re.S)}

    def stream(n):
        ob = objs[n]
        sm = re.search(rb'stream\r?\n(.*?)\r?\nendstream', ob, re.S)
        if not sm:
            return b''
        return zlib.decompress(sm[1]) if b'/FlateDecode' in ob.split(b'stream', 1)[0] else sm[1]

    for n, ob in list(objs.items()):
        if not re.search(rb'/Type\s*/ObjStm\b', ob):
            continue
        first = int(re.search(rb'/First\s+(\d+)', ob)[1])
        count = int(re.search(rb'/N\s+(\d+)', ob)[1])
        decoded = stream(n)
        header = list(map(int, re.findall(rb'\d+', decoded[:first])))
        pairs = list(zip(header[::2], header[1::2]))
        assert len(pairs) == count
        for i, (oid, offset) in enumerate(pairs):
            end = first + pairs[i + 1][1] if i + 1 < len(pairs) else len(decoded)
            objs[oid] = decoded[first + offset:end]

    fonts = {}
    for ob in objs.values():
        for f, n in re.findall(rb'/(F\d+)\s+(\d+)\s+\d+\s+R', ob):
            cm = re.search(rb'/ToUnicode\s+(\d+)\s+\d+\s+R', objs.get(int(n), b''))
            if not cm:
                continue
            cmap, mapping = stream(int(cm[1])), {}
            for block in re.findall(rb'beginbfchar(.*?)endbfchar', cmap, re.S):
                for a, b in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', block):
                    mapping[bytes.fromhex(a.decode())] = bytes.fromhex(b.decode()).decode('utf-16-be', errors='replace')
            for block in re.findall(rb'beginbfrange(.*?)endbfrange', cmap, re.S):
                for a, b, c in re.findall(rb'<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>\s*<([0-9A-Fa-f]+)>', block):
                    start, end, dest = int(a, 16), int(b, 16), int(c, 16)
                    if end - start > 2000:
                        continue
                    for i in range(start, end + 1):
                        mapping[i.to_bytes(len(a) // 2, 'big')] = (dest + i - start).to_bytes(len(c) // 2, 'big').decode('utf-16-be', errors='replace')
            fonts[f] = mapping

    def decode(raw, mapping):
        if not mapping:
            return raw.decode('cp1252', errors='replace')
        lengths = sorted({len(k) for k in mapping}, reverse=True)
        result, i = '', 0
        while i < len(raw):
            for length in lengths:
                k = raw[i:i + length]
                if k in mapping:
                    result += mapping[k]
                    i += length
                    break
            else:
                result += '\ufffd'
                i += 1
        return result

    def unescape(raw):
        raw = re.sub(rb'\\([0-7]{1,3})', lambda m: bytes([int(m[1], 8)]), raw)
        raw = re.sub(rb'\\(?:\r\n|\r|\n)', b'', raw)
        return re.sub(rb'\\(.)', lambda m: {b'n': b'\n', b'r': b'\r', b't': b'\t', b'b': b'\b', b'f': b'\f'}.get(m[1], m[1]), raw)

    pages = []

    def walk(n):
        ob = objs[n]
        if re.search(rb'/Type\s*/Page\b', ob):
            pages.append(n)
        else:
            kids = re.search(rb'/Kids\s*\[(.*?)\]', ob, re.S)
            if kids:
                for k in re.findall(rb'(\d+)\s+\d+\s+R', kids[1]):
                    walk(int(k))

    cat = next(ob for ob in objs.values() if re.search(rb'/Type\s*/Catalog\b', ob))
    walk(int(re.search(rb'/Pages\s+(\d+)\s+\d+\s+R', cat)[1]))
    cm = re.search(rb'/Contents\s*(\[.*?\]|\d+\s+\d+\s+R)', objs[pages[1]], re.S)
    parts = []
    for cid in re.findall(rb'(\d+)\s+\d+\s+R', cm[1]):
        for bt in re.findall(rb'BT\b(.*?)\bET', stream(int(cid)), re.S):
            font = re.search(rb'/(F\d+)\s+[\d.]+\s+Tf', bt)
            mapping = fonts.get(font[1], {}) if font else {}
            for s in re.findall(rb'\((?:\\.|[^\\)])*\)|<[0-9a-fA-F\s]+>', bt, re.S):
                raw = unescape(s[1:-1]) if s.startswith(b'(') else bytes.fromhex(s[1:-1].decode())
                parts.append(decode(raw, mapping))
    text = re.sub(r'\s+', ' ', ''.join(parts))
    (out / (name + '.page2.txt')).write_text(text + '\n')
    records.append({'source': name, 'sha256': hashlib.sha256(data).hexdigest(), 'pages': len(pages), 'extracted_page': 2})
    if name in ['Tema Esame 2024-09-05-1st.pdf', 'Tema Esame 2024-11-12-1st.pdf', 'Tema Esame 2025-07-04-1st.pdf', 'Tema Esame 2026-2-09-1st.pdf', 'Tema Esame 2026-9-10-1st.pdf']:
        clean = re.sub(r'_{3,}', ' [answer space] ', text)
        start = re.search(r'Exercise\s*(?:n\.\s*)?1', clean)
        start = start.start() if start else 0
        print(name + '\n' + clean[start:start + 1450] + '\n')

(out / 'source-checks.json').write_text(json.dumps(records, indent=2) + '\n')
print(f'Checked {len(records)} exam source PDFs.')
