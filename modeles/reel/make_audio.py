# Bruitages + musique (libre de droits) pour un reel Macro facile, 36 s
import numpy as np, wave, sys
SR=44100; D=36.0; N=int(SR*D)
rng=np.random.default_rng(3)
def env(n,a=0.005,r=0.2):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/r)
def add(buf,sig,t0,g=1.0):
    i=int(t0*SR)
    if i>=len(buf): return
    j=min(len(buf),i+len(sig)); buf[i:j]+=sig[:j-i]*g
def tone(f,dur,a=0.005,r=0.2,h=(1,)):
    n=int(dur*SR); t=np.arange(n)/SR; s=sum(np.sin(2*np.pi*f*k*t)/(k*k) for k in h); return s*env(n,a,r)
def pop(): n=int(.12*SR);t=np.arange(n)/SR;f=900*np.exp(-t*18)+300;return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.002,.04)
def blip(): return tone(1320,.15,.002,.05,(1,2))*.7+tone(1980,.15,.002,.04)*.4
def whoosh():
    n=int(.5*SR);x=rng.standard_normal(n);x=np.convolve(x,np.ones(30)/30,'same');t=np.arange(n)/n;return x*np.sin(np.pi*t)**2*.9
def chalk(dur):
    n=int(dur*SR);x=rng.standard_normal(n);x=x-np.convolve(x,np.ones(6)/6,'same');am=.5+.5*np.sin(2*np.pi*14*np.arange(n)/SR)
    return x*am*np.minimum(1,np.arange(n)/(.03*SR))*np.minimum(1,(n-np.arange(n))/(.05*SR))*.35
def gliss(f0,f1,dur):
    n=int(dur*SR);t=np.arange(n)/SR;f=np.linspace(f0,f1,n);return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.01,dur)*.5
def ding(): return tone(1568,1.2,.002,.5,(1,2,3))+tone(2093,1.2,.002,.4)*.5
sfx=np.zeros(N)
for t in [5.2,13.2,21.0,29.4]: add(sfx,whoosh(),t-.1,.6)
for t in [0.2,0.9, 5.2,6.0,6.6,7.2,7.8,8.6, 13.2,13.8,14.4,14.8,15.8, 21.0,21.6,22.2,23.0, 29.4,30.1,30.5]: add(sfx,pop(),t,.55)
for t in [0.9,2.4,5.5,9.6,14.2,17.0,21.8,25.0,31.4]: add(sfx,blip(),t,.35)
add(sfx,gliss(400,900,.6),13.8,.5); add(sfx,gliss(700,250,.7),21.6,.5)
add(sfx,chalk(.9),23.6,1.0); add(sfx,ding(),30.9,.45)
# musique 104 bpm, C-G-Am-F
bpm=104; beat=60/bpm; bar=4*beat
mus=np.zeros(N)
chords=[(261.63,329.63,392.0),(196.0,246.94,293.66),(220.0,261.63,329.63),(174.61,220.0,261.63)]
bass=[130.81,98.0,110.0,87.31]
nb=int(D/bar)+1
for b in range(nb):
    c=chords[b%4]; t0=b*bar
    for k in range(8):  # marimba en croches
        f=c[[0,1,2,1,0,2,1,2][k]]*2
        add(mus,tone(f,.5,.002,.18,(1,4)),t0+k*beat/2,.22)
    add(mus,tone(bass[b%4],bar,.01,.9,(1,2)),t0,.35)
    for f in c: add(mus,tone(f,bar,.3,2.5),t0,.06)
    for k in range(4):
        n=int(.25*SR);tt=np.arange(n)/SR;add(mus,np.sin(2*np.pi*(55+90*np.exp(-tt*30))*tt)*env(n,.002,.12),t0+k*beat,.5 if k%2==0 else .3)
        x=rng.standard_normal(int(.05*SR));add(mus,x*env(len(x),.001,.015),t0+k*beat+beat/2,.08)
fade=np.ones(N);fi=int(1*SR);fo=int(3*SR);fade[:fi]=np.linspace(0,1,fi);fade[-fo:]=np.linspace(1,0,fo)
mus*=fade
mix=sfx*.9+mus*.55
mix=mix/np.max(np.abs(mix))*.89
st=np.stack([mix,mix],1)
def save(name,a):
    w=wave.open(name,'w');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((a*32767).astype('<i2').tobytes());w.close()
save('mix-demande.wav',st)
m=mus/np.max(np.abs(mus))*.89; save('musique-36s.wav',np.stack([m,m],1))
print('ok')
