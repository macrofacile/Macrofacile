# Bruitages + musique (composée, libre de droits) pour le reel LA CROISSANCE, 36 s
import numpy as np, wave
SR=44100; D=53.0; N=int(SR*D); rng=np.random.default_rng(11)
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
for t in [5.2,13.4,22.0,31.0,39.0,46.8]: add(sfx,whoosh(),t-.1,.6)
for t in [0.2,0.9, 5.8,6.4,7.2,7.8,9.6, 14.0,15.6,17.4, 22.6,25.0,27.4, 31.6,33.2,33.6,34.8,36.2, 39.6,40.6,41.6,43.2, 46.8,47.5,47.9,48.3]: add(sfx,pop(),t,.5)
for t in [0.9,2.4,6.2,9.0,14.4,17.8,23.0,27.6,32.0,36.4,39.8,43.4,48.8]: add(sfx,blip(),t,.28)
add(sfx,rise(1.0),17.4,.6); add(sfx,ding(),27.6,.4); add(sfx,rise(0.8),31.6,.5); add(sfx,ding(),48.3,.45)
# musique 5 : bossa lounge, 120 bpm, Fa majeur, Fmaj7-Dm7-Gm7-C7, piano électrique + basse + brosses
bpm=120; beat=60/bpm; bar=4*beat; mus=np.zeros(N)
def ep(f,dur):
    n=int(dur*SR);t=np.arange(n)/SR;m=np.sin(2*np.pi*f*t)*1.0*np.exp(-t*5)
    return (np.sin(2*np.pi*f*t+m)+.3*np.sin(2*np.pi*2*f*t)*np.exp(-t*4))*np.exp(-t*1.8)*(1+.15*np.sin(2*np.pi*5*t))*np.minimum(1,t/.005)
def brush():
    n=int(.18*SR);x=rng.standard_normal(n);x=x-np.convolve(x,np.ones(5)/5,'same');return x*env(n,.01,.07)
def rim():
    n=int(.05*SR);t=np.arange(n)/SR;return (np.sin(2*np.pi*1700*t)+rng.standard_normal(n)*.3)*np.exp(-t*90)
def kick():
    n=int(.2*SR);t=np.arange(n)/SR;f=100*np.exp(-t*30)+48;return np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-t*16)
chords=[(174.61,220.0,261.63,329.63),(146.83,174.61,220.0,261.63),(196.0,233.08,293.66,349.23),(130.81,164.81,196.0,233.08)]
bass=[87.31,73.42,98.0,65.41]
comp=[0,1.5,2.5,3.5]
mel=[880.0,783.99,698.46,659.25, 698.46,880.0,587.33,659.25, 932.33,880.0,783.99,698.46, 659.25,587.33,523.25,587.33]
nb=int(D/bar)+1
for b in range(nb):
    c=chords[b%4];t0=b*bar
    for st in comp:
        for f in c: add(mus,ep(f*2,beat*1.2),t0+st*beat,.045)
    add(mus,tone(bass[b%4],beat*1.4,.01,.5,(1,2)),t0,.32);add(mus,tone(bass[b%4]*1.5,beat*.9,.01,.3,(1,2)),t0+1.5*beat,.22);add(mus,tone(bass[b%4]*2,beat*1.4,.01,.4,(1,2)),t0+2*beat,.26)
    add(mus,kick(),t0,.2);add(mus,kick(),t0+2*beat,.16)
    for k in range(8): add(mus,brush(),t0+k*beat/2,.10 if k%2 else .06)
    for st in [0,1.5,3,4.5-2,2.5]: add(mus,rim(),t0+st*beat,.12)
    if 1<=b<nb-1:
        for k in range(4): add(mus,ep(mel[(b%4)*4+k],beat*1.3),t0+k*beat+(0.5*beat if k==1 else 0),.11)
fade=np.ones(N);fi=int(1*SR);fo=int(3*SR);fade[:fi]=np.linspace(0,1,fi);fade[-fo:]=np.linspace(1,0,fo);mus*=fade
mix=sfx*.9+mus*.65;mix=mix/np.max(np.abs(mix))*.89
w=wave.open('mix-banques.wav','w');w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.stack([mix,mix],1)*32767).astype('<i2').tobytes());w.close();print('ok')
