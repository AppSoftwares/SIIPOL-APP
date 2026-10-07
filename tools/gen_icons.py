# Genera assets/ (icono y splash SIIPOL). Requiere: pip install pillow
import math, os
from PIL import Image, ImageDraw, ImageFont
os.makedirs('assets', exist_ok=True)
def font(sz):
    for p in ['/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf','/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf',
              'C:/Windows/Fonts/arialbd.ttf','/System/Library/Fonts/Supplemental/Arial Bold.ttf']:
        try: return ImageFont.truetype(p, sz)
        except Exception: pass
    return ImageFont.load_default()
GOLD=(184,137,58); CREAM=(243,227,190); G1=(107,20,37); G2=(58,9,19)
def grad(size,c1,c2):
    im=Image.new('RGB',(size,size)); px=im.load()
    for y in range(size):
        for x in range(size):
            t=(x+y)/(2*size-2); px[x,y]=tuple(int(c1[i]+(c2[i]-c1[i])*t) for i in range(3))
    return im
def star(d,cx,cy,R,r,fill):
    pts=[]
    for i in range(10):
        a=-math.pi/2+i*math.pi/5; rad=R if i%2==0 else r
        pts.append((cx+rad*math.cos(a),cy+rad*math.sin(a)))
    d.polygon(pts,fill=fill)
def shield(S,scale=1.0):
    im=Image.new('RGBA',(S,S),(0,0,0,0)); d=ImageDraw.Draw(im)
    w=S*0.56*scale; h=S*0.66*scale; cx=S/2
    def pts(k):
        ww=w*k; hh=h*k; t=S*0.5-hh/2
        p=[(cx-ww/2,t+hh*0.08),(cx,t),(cx+ww/2,t+hh*0.08),(cx+ww/2,t+hh*0.52)]
        for i in range(1,31):
            a=i/30; p.append((cx+ww/2*(1-a)*math.cos(a*math.pi/2),t+hh*0.52+hh*0.48*math.sin(a*math.pi/2)))
        q=[(cx-x+cx,y) for x,y in p]
        return p+q[::-1]
    d.polygon(pts(1.0),fill=GOLD); d.polygon(pts(0.93),fill=G1); d.polygon(pts(0.86),outline=CREAM,fill=None)
    star(d,cx,S*0.40,S*0.085*scale,S*0.035*scale,CREAM)
    f=font(int(S*0.088*scale)); tx='SIIPOL'; bb=d.textbbox((0,0),tx,font=f)
    d.text((cx-(bb[2]-bb[0])/2,S*0.50),tx,font=f,fill=(255,255,255))
    f2=font(int(S*0.042*scale)); t2='VEN 9-1-1'; bb=d.textbbox((0,0),t2,font=f2)
    d.text((cx-(bb[2]-bb[0])/2,S*0.60),t2,font=f2,fill=GOLD)
    return im
S=1024; bg=grad(S,G1,G2); sh=shield(S)
icon=bg.copy(); icon.paste(sh,(0,0),sh)
icon.save('assets/icon-only.png'); icon.save('assets/icon.png')
shield(S,0.72).save('assets/icon-foreground.png'); bg.save('assets/icon-background.png')
for name,c in (('splash',(74,13,25)),('splash-dark',(36,5,13))):
    sp=Image.new('RGB',(2732,2732),c); s=shield(1024,1.0).resize((900,900)); sp.paste(s,((2732-900)//2,(2732-900)//2),s); sp.save(f'assets/{name}.png')
print('assets generados')