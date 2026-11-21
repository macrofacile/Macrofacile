# Bruitages + musique (composée, libre de droits) pour le reel LA CROISSANCE, 36 s
import numpy as np, wave
SR=44100; D=36.0; N=int(SR*D); rng=np.random.default_rng(11)
def env(n,a=0.005,r=0.2):
    t=np.arange(n)/SR; return np.minimum(1,t/a)*np.exp(-t/r)
def add(buf,sig,t0,g=1.0):
    i=int(t0*SR)
    if i>=len(buf): return
    j=min(len(buf),i+len(sig)); buf[i:j]+=sig[:j-i]*g
def tone(f,dur,a=0.005,r=0.2,h=(1,)):
    n=int(dur*SR); t=np.arange(n)/SR; return sum(np.sin(2*np.pi*f*k*t)/(k*k) for k in h)*env(n,a,r)
def pop(): n=int(.12*SR);t=np.arange(n)/SR;f=900*np.exp(-t*18)+300;return np.sin(2*np.pi*np.cumsum(f)/SR)*env(n,.002,.04)
def blip(): return tone(1320,.15,.002,.05,(1,2))*.7+tone(1980,.15,.002,.04)*.4
def whoosh():
    n=int(.5*SR);x=rng.standard_normal(n);x=np.convolve(x,np.ones(30)/30,'same');t=np.arange(n)/n;return x*np.sin(np.pi*t)**2*.9
def rise(dur):  # montée pour le graphique
    n=int(dur*SR);t=np.arange(n)/SR;f=np.linspace(300,1100,n);return np.sin(2*np.pi*np.cumsum(f)/SR)*np.minimum(1,t/.05)*np.minimum(1,(dur-t)/.1)*.35
def vroom(dur):
    n=int(dur*SR);t=np.arange(n)/SR;f=70+90*np.sin(np.pi*t/dur)
    x=np.sign(np.sin(2*np.pi*np.cumsum(f)/SR))*.5+rng.standard_normal(n)*.15
    x=np.convolve(x,np.ones(40)/40,'same');return x*np.sin(np.pi*t/dur)**1.5*.8
def ding(): return tone(1568,1.2,.002,.5,(1,2,3))+tone(2093,1.2,.002,.4)*.5
sfx=np.zeros(N)
for t in [5.2,13.2,21.0,29.4]: add(sfx,whoosh(),t-.1,.6)
for t in [0.2,0.9, 5.6,8.6,10.0,10.5, 13.8,15.0,16.2,17.4, 21.6,22.8,24.0,25.2, 29.4,30.1,30.5]: add(sfx,pop(),t,.55)
for t in [0.9,2.4,6.0,10.0,14.0,17.6,21.6,25.4,31.4]: add(sfx,blip(),t,.3)
add(sfx,rise(2.2),6.0,1.0); add(sfx,ding(),8.15,.35)
add(sfx,rise(1.0),16.2,.6)
n_=int(1.0*SR);t_=np.arange(n_)/SR;add(sfx,np.sin(2*np.pi*np.cumsum(np.linspace(900,300,n_))/SR)*np.minimum(1,t_/.05)*np.minimum(1,(1-t_)/.1)*.35,24.0,.6); add(sfx,ding(),30.9,.45)

def piano(f,dur):
    n=int(dur*SR);t=np.arange(n)/SR
    return sum(np.sin(2*np.pi*f*k*t)*np.exp(-t*(1.5+k*1.2))/k**1.5 for k in (1,2,3,4))*np.minimum(1,t/.003)
def pluck(f,dur):
    n=int(dur*SR);p=int(SR/f);buf=rng.uniform(-1,1,p);out=np.zeros(n)
    for k in range(n): out[k]=buf[k%p];buf[k%p]=0.5*(buf[k%p]+buf[(k+1)%p])*0.995
    return out
def glock(f,dur):
    n=int(dur*SR);t=np.arange(n)/SR;return (np.sin(2*np.pi*f*t)+.4*np.sin(2*np.pi*f*2.76*t)*np.exp(-t*8))*np.exp(-t*3)*np.minimum(1,t/.002)
def whistle(f,dur):
    n=int(dur*SR);t=np.arange(n)/SR;v=1+.006*np.sin(2*np.pi*5.5*t)*np.minimum(1,t/.2)
    return np.sin(2*np.pi*np.cumsum(f*v)/SR)*np.minimum(1,t/.04)*np.minimum(1,(dur-t)/.06)
def clap():
    n=int(.12*SR);x=rng.standard_normal(n);x=x-np.convolve(x,np.ones(3)/3,'same');return x*env(n,.002,.035)
def kick():
    n=int(.2*SR);t=np.arange(n)/SR;f=110*np.exp(-t*30)+50;return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*16)
def fadeit(m):
    fade=np.ones(N);fi=int(1*SR);fo=int(3*SR);fade[:fi]=np.linspace(0,1,fi);fade[-fo:]=np.linspace(1,0,fo);return m*fade
def song(name,bpm,chords,bass,mel,inst,mel_inst,comp):
    beat=60/bpm;bar=4*beat;mus=np.zeros(N);nb=int(D/bar)+1;cache={}
    def ci(f,d):
        k=(round(f,2),round(d,2))
        if k not in cache: cache[k]=inst(f,d)
        return cache[k]
    for b in range(nb):
        c=chords[b%4];t0=b*bar
        for k,(st,idx) in enumerate(comp): add(mus,ci(c[idx]*2,beat*1.6),t0+st*beat,.13)
        add(mus,tone(bass[b%4],beat*1.8,.01,.5,(1,2)),t0,.32);add(mus,tone(bass[b%4]*1.5,beat*1.5,.01,.4,(1,2)),t0+2*beat,.22)
        add(mus,kick(),t0,.22);add(mus,kick(),t0+2*beat,.18)
        for k in (1,3): add(mus,clap(),t0+k*beat,.22)
        if 1<=b<nb-1:
            for k in range(4): add(mus,mel_inst(mel[(b%4)*4+k],beat*.9),t0+k*beat,.10)
    mus=fadeit(mus);mix=sfx*.9+mus*.6;mix=mix/np.max(np.abs(mix))*.89
    w=wave.open(name,'w');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.stack([mix,mix],1)*32767).astype('<i2').tobytes());w.close()
arp=[(0,0),(.5,1),(1,2),(1.5,1),(2,0),(2.5,1),(3,2),(3.5,1)]
# C : sifflement + guitare, Fa majeur, F-C-Dm-Bb, 108 bpm
song('mixC.wav',108,[(174.61,220.0,261.63),(130.81,164.81,196.0),(146.83,174.61,220.0),(116.54,146.83,174.61)],[87.31,65.41,73.42,58.27],
 [880.0,1046.5,880.0,698.46, 783.99,659.25,783.99,1046.5, 880.0,698.46,880.0,1174.66, 932.33,880.0,783.99,698.46],pluck,whistle,[(0,0),(1,1),(1.5,2),(2,0),(3,1),(3.5,2)])
print('ok')
