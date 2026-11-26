import sys,glob
from PIL import Image
d=sys.argv[1]
for k in ['p1','p2','bonus']:
    n=len(glob.glob(f'{d}/{k}-[0-9]*.png'))
    ims=[Image.open(f'{d}/{k}-{i}.png') for i in range(1,n+1)]
    w,h=432,540;g=24;cols=min(n,5) if n<=5 else (n+1)//2;rows=(n+cols-1)//cols
    sh=Image.new('RGB',(cols*w+(cols+1)*g,rows*h+(rows+1)*g),'#e9e9e9')
    for i,im in enumerate(ims): sh.paste(im.resize((w,h),Image.LANCZOS),(g+(i%cols)*(w+g),g+(i//cols)*(h+g)))
    sh.save(f'{d}/planche-{k}.png')
