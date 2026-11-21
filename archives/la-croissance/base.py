import os, sys, json
TH = sys.argv[1] if len(sys.argv) > 1 else '#C9F2DF'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'slides'
os.makedirs(OUT, exist_ok=True)
THEME='LA CROISSANCE'
NPARTS=3
K = '#121212'; Y = '#FFD166'; GP = '#BDEFC9'; RP = '#FFC9C9'; VP = '#DCD3FF'; BP = '#CDE6FF'; OP = '#FFE0B8'

CSS = f"""@font-face{{font-family:F;src:url(../Fredoka.ttf);font-weight:300 700}}
html,body{{margin:0}}
.s{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:F;color:{K};box-sizing:border-box}}
.in{{position:relative;height:100%;box-sizing:border-box;display:flex;flex-direction:column;gap:40px;padding:80px 72px 170px}}
.tag{{align-self:flex-start;background:#fff;border-radius:28px;padding:10px 34px 16px;transform:rotate(-2deg);box-shadow:0 10px 0 {K};font-weight:700;font-size:58px;line-height:1;white-space:nowrap}}
.mid{{display:flex;flex-direction:column;gap:46px;margin:auto 0}}
.big{{margin:0;text-align:center;font-weight:600;font-size:66px;line-height:1.2}}
.txt{{margin:0;text-align:center;font-weight:500;font-size:46px;line-height:1.3}}
.hl{{background:{Y};border-radius:12px;padding:0 12px 6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}}
.card{{background:#fff;border-radius:36px;box-shadow:0 12px 0 {K};padding:36px 36px 40px;display:flex;flex-direction:column;gap:22px}}
.row{{border-radius:28px;box-shadow:0 9px 0 {K};padding:20px 26px;display:flex;align-items:center;gap:24px}}
.ic{{flex:none;width:92px;height:92px;border-radius:50%;background:#fff;border:5px solid {K};display:flex;align-items:center;justify-content:center;box-sizing:border-box}}
.rt{{display:flex;flex-direction:column;gap:4px;flex:1}}
.rt b{{font-weight:700;font-size:42px;line-height:1.1}}
.rt span{{font-weight:400;font-size:32px;line-height:1.25}}
.rt .ex{{display:block;margin-top:4px;font-weight:600;font-size:30px;font-style:normal}}
.arrow{{text-align:center;font-weight:700;font-size:56px;line-height:.8}}
.foot{{position:absolute;left:72px;right:72px;bottom:56px;display:flex;justify-content:space-between;align-items:center}}
.pill{{display:flex;align-items:center;gap:14px;background:{K};border-radius:999px;padding:10px 26px 14px;transform:rotate(-2deg);font-weight:700;font-size:32px;line-height:1;color:#fff}}
"""

ICON = {
 'menage': '<circle cx="32" cy="20" r="10"/><path d="M14 54 C14 40 22 33 32 33 C42 33 50 40 50 54 Z"/>',
 'usine': '<path d="M8 54 V30 L22 38 V30 L36 38 V14 H48 V54 Z"/><path d="M8 54 H56"/>',
 'etat': '<path d="M8 24 L32 10 L56 24 Z"/><path d="M14 28 V48 M26 28 V48 M38 28 V48 M50 28 V48"/><path d="M8 54 H56"/>',
 'monde': '<circle cx="32" cy="32" r="22"/><path d="M10 32 H54"/><path d="M32 10 C22 22 22 42 32 54 C42 42 42 22 32 10"/>',
 'carton': '<path d="M10 22 L32 12 L54 22 V46 L32 56 L10 46 Z"/><path d="M10 22 L32 32 L54 22 M32 32 V56"/>',
 'up': '<path d="M32 52 V14 M18 28 L32 14 L46 28"/>',
 'down': '<path d="M32 12 V50 M18 36 L32 50 L46 36"/>',
 'euro': '<path d="M46 16 C40 11 32 10 26 14 C18 19 16 30 18 38 C20 48 32 56 46 48"/><path d="M10 28 H36 M10 38 H34"/>',
 'pourcent': '<circle cx="20" cy="20" r="7"/><circle cx="44" cy="44" r="7"/><path d="M48 14 L16 50"/>',
 'cle': '<circle cx="22" cy="32" r="12"/><path d="M34 32 H56 M48 32 V42 M56 32 V40"/>',
 'piege': '<path d="M32 10 L56 52 H8 Z"/><path d="M32 26 V38"/><circle cx="32" cy="45" r="1.5"/>',
 'pont': '<path d="M6 40 H58"/><path d="M10 40 C18 22 46 22 54 40"/><path d="M18 40 V52 M46 40 V52 M32 26 V40"/>',
 'cadenas': '<rect x="14" y="28" width="36" height="26" rx="5"/><path d="M22 28 V20 a10 10 0 0 1 20 0 V28"/>',
}
def ic(name, color=K, size=56):
    return f'<div class="ic"><svg width="{size}" height="{size}" viewBox="0 0 64 64" fill="none" stroke="{color}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round">{ICON[name]}</svg></div>'

def row(icon, title, sub, bg):
    return f'<div class="row" style="background:{bg}">{ic(icon)}<div class="rt"><b>{title}</b><span>{sub}</span></div></div>'

LOGO_S = '<img src="../logo.png" style="width:150px;transform:rotate(-4deg)">'
def foot(label, n, tot, bonus=False):
    lab = f'<span style="color:{Y}">BONUS</span>' if bonus else f'<span style="color:{Y}">{label}</span>'
    return f'<div class="foot">{LOGO_S}<div class="pill">{lab}<span>{n}/{tot}</span></div></div>'

SWIPE = '<div style="position:absolute;right:72px;bottom:56px"><svg width="150" height="118" viewBox="0 0 100 78" fill="none" stroke="#121212" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"><path d="M84 16 C68 4 44 4 26 14"/><path d="M33 5 L26 14 L36 19"/><g transform="translate(34 14)"><path fill="#fff" d="M28 42 V12 a4 4 0 0 1 8 0 V30 V26 a4 4 0 0 1 8 0 V32 V29 a4 4 0 0 1 8 0 V44 C52 54 46 60 38 60 H34 C28 60 24 57 21 52 L13 40 a4 4 0 0 1 6.5 -4.5 L28 42 Z"/></g></svg></div>'

def cover(part, sub, dark=False):
    bg = K if dark else TH
    shadow = '#fff' if dark else K
    card_bg = TH if dark else '#fff'
    if dark:
        sticker = f'<div style="position:absolute;right:70px;top:-150px;background:{Y};border:5px solid {K};border-radius:30px;padding:12px 40px 20px;transform:rotate(8deg);box-shadow:7px 11px 0 {K};font-weight:700;font-size:96px;line-height:1">BONUS</div>'
    else:
        sticker = ''
    partpill = '' if dark else f'<div style="background:{Y};color:{K};border:5px solid {K};border-radius:999px;padding:14px 50px 22px;transform:rotate(2deg);box-shadow:7px 11px 0 {K};font-weight:700;font-size:60px;line-height:1;white-space:nowrap">Partie {part}/{NPARTS}</div>'
    subpill = f'<div style="background:#FF6B6B;color:#fff;border:5px solid {K};border-radius:32px;padding:16px 40px 24px;transform:rotate({2 if dark else -1.5}deg);box-shadow:7px 11px 0 {shadow if dark else K};font-weight:{600 if dark else 700};font-size:{70 if dark else (84 if len(sub)<16 else 66)}px;line-height:1.1;white-space:nowrap">{sub}</div>'
    swipe = SWIPE.replace('stroke="#121212" stroke-width="4"', f'stroke="{"#fff" if dark else K}" stroke-width="4"').replace('fill="#fff"', f'fill="{K if dark else "#fff"}"')
    return f'''<div class="s" style="background:{bg}"><div class="in" style="justify-content:space-between;gap:0">
<img src="../logo.png" style="width:240px;transform:rotate(-4deg);align-self:flex-start">
<div style="display:flex;flex-direction:column;gap:{48 if not dark else 64}px;align-items:center">
<div style="position:relative"><div style="background:{card_bg};border:6px solid {K};border-radius:44px;padding:26px 50px 40px;transform:rotate(-2deg);box-shadow:10px 18px 0 {shadow};font-weight:700;font-size:{(100 if '<br>' in THEME else (138 if len(THEME)<=11 else 116))}px;line-height:1.05;text-align:center;white-space:nowrap">{THEME}</div>{sticker}</div>
{partpill}{subpill}</div><div></div></div>{swipe}</div>'''

def nextpost(n, t):
    return f'<div style="background:{K};color:#fff;border-radius:30px;padding:16px 30px 20px;display:flex;align-items:center;justify-content:space-between;gap:20px;transform:rotate(-1deg)"><div style="display:flex;flex-direction:column;gap:6px"><span style="color:{Y};font-weight:700;font-size:30px">Prochain post · Partie {n}/{NPARTS}</span><span style="font-weight:600;font-size:42px;line-height:1.1">{t}</span></div><span style="font-weight:700;font-size:64px;color:{Y}">→</span></div>'

def slide(inner, footer, bg=None):
    return f'<div class="s" style="background:{bg or TH}"><div class="in">{inner}</div>{footer}</div>'

def tile(icon,who,verb,ex,bg,rot):
    return f'<div style="background:{bg};border-radius:34px;box-shadow:0 10px 0 {K};padding:30px 24px 30px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:10px;transform:rotate({rot}deg)">{ic(icon,K,64).replace("width:92px;height:92px","width:116px;height:116px")}<b style="font-size:40px;line-height:1.1">{who}</b><span style="font-weight:600;font-size:32px;background:#fff;border-radius:999px;padding:4px 18px 8px">{verb}</span><span style="font-size:28px">{ex}</span></div>'
def why(who,what,ex,bg):
    return f'<div style="display:flex;align-items:stretch;border-radius:30px;box-shadow:0 10px 0 {K};overflow:hidden;background:#fff"><div style="background:{bg};width:290px;flex:none;display:flex;align-items:center;justify-content:center;padding:20px;border-right:4px solid {K}"><b style="font-size:38px;text-align:center;line-height:1.1">{who}</b></div><div style="padding:38px 28px;display:flex;flex-direction:column;gap:10px;justify-content:center"><b style="font-size:40px;line-height:1.15">→ {what}</b><span style="font-size:32px;font-weight:500">{ex}</span></div></div>'

PIG = """<svg width="{w}" viewBox="0 0 220 190" fill="none" stroke="#121212" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
<g transform="translate(0 6)">{coin}
<path d="M44 152 v20 h20 v-14 M136 156 v16 h20 v-20" fill="#FF9EB5"/>
<ellipse cx="104" cy="112" rx="76" ry="56" fill="#FFB3C6"/>
<path d="M62 64 L56 36 L86 56" fill="#FF9EB5"/>
<rect x="166" y="96" width="34" height="34" rx="12" fill="#FF9EB5"/>
<circle cx="178" cy="113" r="3" fill="#121212" stroke="none"/><circle cx="189" cy="113" r="3" fill="#121212" stroke="none"/>
<circle cx="146" cy="96" r="5" fill="#121212" stroke="none"/>
<path d="M86 66 h40"/>
<path d="M28 108 c-14 -4 -14 -20 0 -16"/>
{extra}</g></svg>"""
def pig(w=260, coin=True, sad=False):
    c = '<g transform="translate(92 -4)"><ellipse cx="14" cy="22" rx="20" ry="20" fill="#FFD166"/><path d="M14 12 v20"/></g>' if coin else ''
    e = '<path d="M128 126 q10 -10 22 0" />' if sad else '<path d="M130 122 q10 10 22 0"/>'
    if sad: e += '<path d="M60 92 l14 22 l-10 6 l16 22" stroke="#121212" stroke-width="5"/>'
    return PIG.format(w=w, coin=c, extra=e)

def deco(svg, right=80, bottom=150, rot=-8):
    return f'<div style="position:absolute;right:{right}px;bottom:{bottom}px;transform:rotate({rot}deg);pointer-events:none">{svg}</div>'

def jar(w=230, full=True):
    coins_full = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="22" ry="9" fill="#FFD166"/>' for x,y in [(70,196),(112,196),(150,196),(88,184),(132,184),(70,172),(112,172),(150,172),(90,160),(130,160),(110,148)])
    coins_few = '<ellipse cx="96" cy="196" rx="22" ry="9" fill="#FFD166"/><ellipse cx="136" cy="198" rx="22" ry="9" fill="#FFD166"/>'
    falling = '<g transform="translate(160 18) rotate(20)"><ellipse cx="0" cy="0" rx="20" ry="20" fill="#FFD166"/><path d="M0 -9 v18"/></g>' if full else '<path d="M188 70 q8 12 0 18 q-8 -6 0 -18 Z" fill="#9AD4FF" stroke-width="4"/>'
    return f"""<svg width="{w}" viewBox="0 0 220 230" fill="none" stroke="#121212" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
{falling}
<rect x="62" y="46" width="96" height="24" rx="8" fill="#B9A7FF"/>
<path d="M58 70 h104 c18 0 26 14 26 30 v96 c0 14 -10 24 -24 24 h-108 c-14 0 -24 -10 -24 -24 v-96 c0 -16 8 -30 26 -30 Z" fill="#EAF6FF"/>
{coins_full if full else coins_few}
<rect x="52" y="104" width="116" height="34" rx="8" fill="#fff" stroke-width="5"/>
<text x="110" y="129" text-anchor="middle" font-family="F" font-weight="700" font-size="22" fill="#121212" stroke="none">ÉPARGNE</text>
<path d="M50 160 v28" stroke="#fff" stroke-width="7" opacity=".9"/>
</svg>"""

P = {}
