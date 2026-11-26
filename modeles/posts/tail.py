FITJS = "<script>/*fitjs*/document.fonts.ready.then(()=>{for(const e of document.querySelectorAll('.fit')){let f=124;while(e.offsetWidth>760&&f>60){f-=2;e.style.fontSize=f+'px'}}})</script>"
import re
def _contour(h):
    # règle nov. 2026 : blocs avec contour noir + ombre en biais
    return re.sub(r'box-shadow:0 (\d+)px 0 #121212', lambda m: f'border:5px solid #121212;box-shadow:{max(5,round(int(m.group(1))*0.6))}px {m.group(1)}px 0 #121212', h)
for k, lst in P.items():
    for i, h in enumerate(lst, 1):
        open(f'{OUT}/{k}-{i}.html', 'w').write(_contour(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}{FITJS}</body></html>'))
print('ok')
