const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
(async()=>{const dir=process.argv[2];const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
for(const f of fs.readdirSync(dir).filter(f=>f.endsWith('.html')).sort()){await p.goto('file://'+path.resolve(dir,f));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(150);
const ov=await p.evaluate(()=>{const s=document.querySelector('.s');const r=[];s.querySelectorAll('*').forEach(e=>{const b=e.getBoundingClientRect();if(b.right>1082||b.bottom>1352||b.left<-2)r.push(e.tagName+':'+(e.textContent||'').slice(0,20))});return r.slice(0,3)});
if(ov.length)console.log(f,'OVERFLOW',ov);
await p.screenshot({path:path.resolve(dir,f.replace('.html','.png'))});}
await b.close()})()
