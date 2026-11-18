# Bruitages + musique (libre de droits) pour un reel Macro facile, 36 s
import numpy as np, wave, sys
SR=44100; D=36.0; N=int(SR*D)
rng=np.random.default_rng(7)
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
for t in [0.2,0.9, 5.2,5.8,6.3,7.4,7.9,9.4, 13.2,13.7,14.1,14.8,16.8,17.2, 21.3,21.7,22.5,22.9,23.7,24.1,25.2, 29.4,30.1,30.5]: add(sfx,pop(),t,.55)
for t in [0.9,2.4,5.6,9.6,14.4,17.2,21.6,25.2,31.4]: add(sfx,blip(),t,.35)
add(sfx,gliss(700,250,.5),14.8,.45); add(sfx,ding(),16.8,.35)
add(sfx,chalk(.8),26.0,1.0); add(sfx,whoosh(),25.6,.5); add(sfx,ding(),30.9,.45)
# musique 2 : 90 bpm, Fa majeur, F-Dm-Bb-C, ukulele (Karplus-Strong) + piano doux + claquements de doigts
bpm=90; beat=60/bpm; bar=4*beat
mus=np.zeros(N)
def pluck(f,dur,bright=0.5):
    n=int(dur*SR); p=int(SR/f); buf=rng.uniform(-1,1,p); out=np.zeros(n)
    for k in range(n):
        out[k]=buf[k%p]; buf[k%p]=0.5*(buf[k%p]+buf[(k+1)%p])*0.996
    return out*np.minimum(1,np.arange(n)/(.003*SR))
def epiano(f,dur):
    n=int(dur*SR);t=np.arange(n)/SR
    return (np.sin(2*np.pi*f*t)+.3*np.sin(2*np.pi*2*f*t))*np.exp(-t*1.2)*(1+.15*np.sin(2*np.pi*5*t))*np.minimum(1,t/.02)
chords=[(174.61,220.0,261.63),(146.83,174.61,220.0),(116.54,146.83,174.61),(130.81,164.81,196.0)]
bass=[87.31,73.42,58.27,65.41]
pattern=[0,2,1,2, 0,2,1,2]  # croches, ukulele
strum_t=[0,.75,1.5,2,2.75,3.5]
cache={}
def pl(f):
    k=round(f,2)
    if k not in cache: cache[k]=pluck(f,.9)
    return cache[k]
mel=[523.25,440.0,466.16,523.25, 587.33,523.25,440.0,392.0, 466.16,440.0,392.0,349.23, 392.0,440.0,523.25,523.25]
nb=int(D/bar)+1
for b in range(nb):
    c=chords[b%4]; t0=b*bar
    for st in strum_t:
        for k,f in enumerate(c): add(mus,pl(f*2),t0+st*beat+k*0.012,.16)
    for f in c: add(mus,epiano(f,bar),t0,.07)
    add(mus,tone(bass[b%4],beat*1.8,.01,.6,(1,2)),t0,.32); add(mus,tone(bass[b%4]*1.5,beat*1.8,.01,.6,(1,2)),t0+2*beat,.22)
    for k in (1,3):
        x=rng.standard_normal(int(.06*SR)); x=x-np.convolve(x,np.ones(4)/4,'same'); add(mus,x*env(len(x),.001,.02),t0+k*beat,.25)
    if b>=1 and b<nb-1:
        for k in range(4):
            add(mus,tone(mel[(b%4)*4+k],beat*.9,.005,.35,(1,3)),t0+k*beat+beat*0.5,.10)
fade=np.ones(N);fi=int(1*SR);fo=int(3*SR);fade[:fi]=np.linspace(0,1,fi);fade[-fo:]=np.linspace(1,0,fo)
mus*=fade
mix=sfx*.9+mus*.55
mix=mix/np.max(np.abs(mix))*.89
st=np.stack([mix,mix],1)
def save(name,a):
    w=wave.open(name,'w');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((a*32767).astype('<i2').tobytes());w.close()
save('mix-monnaie.wav',st)
m=mus/np.max(np.abs(mus))*.89; save('musique-monnaie.wav',np.stack([m,m],1))
print('ok')
