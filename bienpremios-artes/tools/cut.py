import sys,os
from PIL import Image, ImageOps
from rembg import remove, new_session
src,dst,model=sys.argv[1],sys.argv[2],sys.argv[3]
s=new_session(model)
for f in sorted(os.listdir(src)):
    im=ImageOps.exif_transpose(Image.open(os.path.join(src,f))).convert('RGB')
    im.thumbnail((1600,1600))
    out=remove(im,session=s,post_process_mask=True)
    bb=out.getchannel('A').point(lambda v:255 if v>20 else 0).getbbox()
    out=out.crop(bb)
    n=os.path.splitext(f)[0]+'.png'; out.save(os.path.join(dst,n)); print(n,out.size)
