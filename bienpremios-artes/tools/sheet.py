import sys,os
from PIL import Image, ImageOps, ImageDraw
src,dst=sys.argv[1],sys.argv[2]
fs=sorted(os.listdir(src)); cells=[]
for f in fs:
    try:
        im=ImageOps.exif_transpose(Image.open(os.path.join(src,f))).convert('RGB')
    except Exception as e: print('X',f,e); continue
    print(f, im.size); im.thumbnail((300,400)); c=Image.new('RGB',(310,430),(40,40,40)); c.paste(im,(5,5)); ImageDraw.Draw(c).text((5,412),f[:44],fill='white'); cells.append(c)
W=Image.new('RGB',(310*6,430*((len(cells)+5)//6)),(20,20,20))
for i,c in enumerate(cells): W.paste(c,((i%6)*310,(i//6)*430))
W.save(dst)
