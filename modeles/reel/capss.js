const {chromium}=require('playwright');const {spawn}=require('child_process');
const [from,to,out]=[parseFloat(process.argv[2]),parseFloat(process.argv[3]),process.argv[4]];
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920},deviceScaleFactor:2});
await p.goto('file://'+__dirname+'/reel.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);
if(out.endsWith('.jpg')){await p.evaluate(t=>render(t),from);await p.screenshot({path:out,type:'png'});await b.close();return}
const ff=spawn('ffmpeg',['-y','-loglevel','error','-f','image2pipe','-framerate','30','-c:v','png','-i','-','-vf','scale=1080:1920:flags=lanczos','-c:v','libx264','-crf','10','-preset','slow','-tune','animation','-profile:v','high','-level','4.2','-pix_fmt','yuv420p','-r','30',out+'.tmp.mp4']);
for(let f=Math.round(from*30);f<Math.round(to*30);f++){await p.evaluate(t=>render(t),f/30);ff.stdin.write(await p.screenshot({type:'png'}));}
ff.stdin.end();ff.on('close',c=>{if(c===0)require('fs').renameSync(out+'.tmp.mp4',out);console.log('done',c)});await b.close();})();
