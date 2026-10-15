import pymupdf,json
from pathlib import Path
base=Path('Advanced Algorithms and Parallel Programming'); out=Path('outputs/exam-bank')
g=json.loads((out/'grouped.json').read_text()); keys=sorted({(x['q']['file'],x['q']['page']) for x in g if x['q'].get('visual')})
attach=base/'Attachments/Exam Question Bank';attach.mkdir(parents=True,exist_ok=True)
sheet=pymupdf.open();page=sheet.new_page(width=1200,height=400*((len(keys)+3)//4))
for i,(f,n) in enumerate(keys):
 d=pymupdf.open(base/'Old Exams'/f); p=d[n-1]
 stem=f.replace('Tema Esame ','').replace('.pdf','')+f'-p{n}.png'
 p.get_pixmap(matrix=pymupdf.Matrix(1.5,1.5)).save(attach/stem)
 x=(i%4)*300;y=(i//4)*400
 page.show_pdf_page(pymupdf.Rect(x,y+20,x+290,y+395),d,n-1)
 page.insert_text((x+3,y+12),f[11:-4],fontsize=9)
page.get_pixmap().save(out/'visual-review.png')
print(keys)
