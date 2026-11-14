import sys
from PIL import Image
d=sys.argv[1]
for k in ['p1','p2','p3','p4','bonus']:
    ims=[Image.open(f'{d}/{k}-{i}.png') for i in range(1,6)]
    w,h=432,540;g=24
    sh=Image.new('RGB',(5*w+6*g,h+2*g),'#e9e9e9')
    for i,im in enumerate(ims): sh.paste(im.resize((w,h),Image.LANCZOS),(g+i*(w+g),g))
    sh.save(f'{d}/planche-{k}.png')
