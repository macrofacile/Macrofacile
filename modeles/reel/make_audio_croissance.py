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
for t in [0.2,0.9, 5.6,8.6,10.0,10.5, 13.8,14.6,17.4, 21.3,21.8,22.8,23.3,24.8, 29.4,30.1,30.5]: add(sfx,pop(),t,.55)
for t in [0.9,2.4,6.0,10.0,14.0,17.6,21.6,25.4,31.4]: add(sfx,blip(),t,.3)
add(sfx,rise(2.2),6.0,1.0); add(sfx,ding(),8.15,.35)
add(sfx,vroom(1.6),16.0,.7); add(sfx,vroom(1.2),25.4,.7); add(sfx,ding(),30.9,.45)
# musique 3 : 112 bpm, Sol majeur, G-Em-C-D, vibraphone (FM) + basse ronde + petit kick + shaker
bpm=112; beat=60/bpm; bar=4*beat; mus=np.zeros(N)
def vib(f,dur):
    n=int(dur*SR);t=np.arange(n)/SR;m=np.sin(2*np.pi*f*3.5*t)*1.2*np.exp(-t*6)
    return np.sin(2*np.pi*f*t+m)*np.exp(-t*2.2)*(1+.25*np.sin(2*np.pi*6*t))*np.minimum(1,t/.004)
def kick():
    n=int(.25*SR);t=np.arange(n)/SR;f=120*np.exp(-t*30)+45;return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*14)
def shaker():
    n=int(.07*SR);x=rng.standard_normal(n);x=x-np.convolve(x,np.ones(3)/3,'same');return x*env(n,.004,.02)
chords=[(196.0,246.94,293.66),(164.81,196.0,246.94),(130.81,164.81,196.0),(146.83,185.0,220.0)]
bass=[98.0,82.41,65.41,73.42]
arp=[0,1,2,1,0,2,1,2]
mel=[587.33,493.88,587.33,659.25, 493.88,392.0,440.0,493.88, 523.25,493.88,440.0,392.0, 440.0,493.88,587.33,587.33]
nb=int(D/bar)+1
for b in range(nb):
    c=chords[b%4];t0=b*bar
    for k,i in enumerate(arp): add(mus,vib(c[i]*2,beat*1.2),t0+k*beat/2,.12)
    add(mus,tone(bass[b%4],beat*1.6,.01,.5,(1,2,3)),t0,.35);add(mus,tone(bass[b%4],beat*.9,.01,.3,(1,2,3)),t0+2.5*beat,.25)
    for k in range(4): add(mus,kick(),t0+k*beat,.3 if k%2==0 else .18)
    for k in range(8): add(mus,shaker(),t0+k*beat/2+beat/4,.12)
    if 1<=b<nb-1:
        for k in range(4): add(mus,vib(mel[(b%4)*4+k]*2,beat*1.5),t0+k*beat,.07)
fade=np.ones(N);fi=int(1*SR);fo=int(3*SR);fade[:fi]=np.linspace(0,1,fi);fade[-fo:]=np.linspace(1,0,fo);mus*=fade
mix=sfx*.9+mus*.6;mix=mix/np.max(np.abs(mix))*.89
def save(name,a):
    w=wave.open(name,'w');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.stack([a,a],1)*32767).astype('<i2').tobytes());w.close()
save('mix-croissance.wav',mix); m=mus/np.max(np.abs(mus))*.89; save('musique-croissance.wav',m); print('ok')
