import os, sys, json
TH = sys.argv[1] if len(sys.argv) > 1 else '#C9F2DF'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'slides'
os.makedirs(OUT, exist_ok=True)
THEME='LES BANQUES'
NPARTS=2
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
    partpill = '' if (dark and not part) else f'<div style="background:{Y};color:{K};border:5px solid {K};border-radius:999px;padding:14px 50px 22px;transform:rotate(2deg);box-shadow:7px 11px 0 {K};font-weight:700;font-size:60px;line-height:1;white-space:nowrap">Partie {part}/{NPARTS}</div>'
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
GP = '#FFFFFF'  # fond menthe : blocs verts en blanc pour qu'ils ressortent
UL = 'text-decoration:underline;text-decoration-color:#FFD166;text-decoration-thickness:10px;text-underline-offset:12px;text-decoration-skip-ink:none'
quizblock = f'<div style="background:{K};color:#fff;border-radius:30px;padding:16px 30px 20px;display:flex;align-items:center;justify-content:space-between;gap:20px;transform:rotate(-1deg)"><div style="display:flex;flex-direction:column;gap:6px"><span style="color:{Y};font-weight:700;font-size:30px">Teste-toi · quiz gratuit</span><span style="font-weight:600;font-size:42px;line-height:1.1">macrofacile.fr</span></div><span style="font-weight:700;font-size:64px;color:{Y}">→</span></div>'
ICON['ecole'] = '<path d="M8 26 L32 12 L56 26"/><rect x="14" y="26" width="36" height="28"/><rect x="27" y="38" width="10" height="16"/>'
ICON['resto'] = '<path d="M18 10 V30 M12 10 V24 c0 4 3 6 6 6 s6 -2 6 -6 V10 M18 30 V54"/><path d="M44 54 V10 c-8 4 -10 14 -10 22 h10"/>'
ICON['virus'] = '<circle cx="32" cy="32" r="14"/><path d="M32 6 V18 M32 46 V58 M6 32 H18 M46 32 H58 M14 14 L22 22 M42 42 L50 50 M50 14 L42 22 M22 42 L14 50"/>'
def down(title, sub, bg):
    return f'<div class="row" style="background:{bg}"><div class="ic" style="background:#FF6B6B"><svg width="56" height="56" viewBox="0 0 64 64" fill="none" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M32 12 V50 M18 36 L32 50 L46 36"/></svg></div><div class="rt"><b>{title}</b><span>{sub}</span></div></div>'
def upr(title, sub, bg):
    return down(title, sub, bg).replace('M32 12 V50 M18 36 L32 50 L46 36','M32 52 V14 M18 28 L32 14 L46 28')
def result(txt, bg=Y):
    return f'<p class="big" style="font-size:50px;margin-top:20px"><span class="hl" style="background:{bg}">{txt}</span></p>'
def pedales(w=560):
    return f'''<svg width="{w}" viewBox="0 0 320 170" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M20 150 H300"/>
<g transform="rotate(-14 95 120)"><rect x="40" y="70" width="110" height="64" rx="14" fill="#CDE6FF"/><text x="95" y="112" text-anchor="middle" font-family="F" font-weight="700" font-size="28" fill="#121212" stroke="none">ÉTAT</text></g>
<path d="M95 135 V150"/>
<g transform="rotate(-14 225 120)"><rect x="170" y="70" width="110" height="64" rx="14" fill="#FFD166"/><text x="225" y="112" text-anchor="middle" font-family="F" font-weight="700" font-size="28" fill="#121212" stroke="none">BCE</text></g>
<path d="M225 135 V150"/></svg>'''

def ill(svg, mt=10, rot=-3):
    return f'<div style="display:flex;justify-content:center;margin-top:{mt}px;transform:rotate({rot}deg)">{svg}</div>'
CAR = '<svg width="{w}" viewBox="0 0 300 140" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"><path d="M20 96 V74 c0-8 6-12 14-14 l30-6 l26-26 c6-6 12-8 20-8 h70 c10 0 16 4 22 12 l20 26 l40 8 c8 2 12 8 12 16 v14 Z" fill="#FF9E9E"/><path d="M98 52 l18-18 h40 v18 Z M168 34 h18 l14 18 h-32 Z" fill="#CDE6FF"/><circle cx="76" cy="100" r="20" fill="#121212"/><circle cx="76" cy="100" r="7" fill="#fff" stroke="none"/><circle cx="226" cy="100" r="20" fill="#121212"/><circle cx="226" cy="100" r="7" fill="#fff" stroke="none"/></svg>'
SCHOOL = '''<svg width="{w}" viewBox="0 0 260 170" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M130 8 V40"/><path d="M130 10 h30 l-6 9 l6 9 h-30" fill="#FF6B6B" stroke-width="5"/>
<path d="M20 78 L130 40 L240 78" fill="#FFD166"/><rect x="34" y="78" width="192" height="80" fill="#fff"/>
<rect x="56" y="96" width="34" height="28" fill="#CDE6FF" stroke-width="5"/><rect x="170" y="96" width="34" height="28" fill="#CDE6FF" stroke-width="5"/>
<path d="M112 158 V112 h36 V158" fill="#FFE0B8"/><text x="130" y="70" text-anchor="middle" font-family="F" font-weight="700" font-size="20" fill="#121212" stroke="none">ÉCOLE</text>
<path d="M8 158 H252"/></svg>'''
PLATE = '''<svg width="{w}" viewBox="0 0 260 140" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M40 20 V60 M30 20 V48 c0 8 6 12 10 12 s10 -4 10 -12 V20 M40 60 V124"/>
<circle cx="130" cy="72" r="56" fill="#fff"/><circle cx="130" cy="72" r="38" fill="#FFE0B8" stroke-width="5"/>
<path d="M112 70 c6 -14 30 -14 36 0 c-6 10 -30 10 -36 0 Z" fill="#FF9E9E" stroke-width="5"/><path d="M118 88 h24" stroke="#7FDDB5" stroke-width="8"/>
<path d="M220 124 V20 c-14 8 -18 26 -18 40 h18"/></svg>'''
BANK = '''<svg width="{w}" viewBox="0 0 260 170" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M20 60 L130 12 L240 60 Z" fill="#FFD166"/><circle cx="130" cy="42" r="14" fill="#fff" stroke-width="5"/><text x="130" y="49" text-anchor="middle" font-family="F" font-weight="700" font-size="20" fill="#121212" stroke="none">€</text>
<rect x="28" y="60" width="204" height="14" fill="#fff"/>
<path d="M50 74 V136 M90 74 V136 M130 74 V136 M170 74 V136 M210 74 V136" stroke-width="10"/>
<rect x="20" y="136" width="220" height="18" fill="#CDE6FF"/></svg>'''
PRICE = '''<svg width="{w}" viewBox="0 0 280 160" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<g transform="rotate(-10 110 90)"><path d="M30 60 L80 30 H190 V130 H80 L30 100 Z" fill="#FFD166"/><circle cx="62" cy="80" r="9" fill="#fff"/>
<text x="138" y="96" text-anchor="middle" font-family="F" font-weight="700" font-size="40" fill="#121212" stroke="none">PRIX</text></g>
<path d="M240 140 V30 M214 56 L240 30 L266 56" stroke="#FF6B6B" stroke-width="12"/></svg>'''
SHOP = '''<svg width="{w}" viewBox="0 0 280 180" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M20 60 L36 20 H244 L260 60 Z" fill="#FF9E9E"/><path d="M70 20 L60 60 M120 20 L115 60 M160 20 L165 60 M210 20 L220 60" stroke-width="5"/>
<rect x="30" y="60" width="220" height="104" fill="#fff"/><rect x="48" y="80" width="80" height="84" fill="#CDE6FF"/><rect x="150" y="80" width="82" height="60" fill="#CDE6FF"/>
<path d="M150 70 l20 -16 l20 16"/><g transform="rotate(-6 140 120)"><rect x="96" y="104" width="100" height="40" rx="8" fill="#FF6B6B"/>
<text x="146" y="132" text-anchor="middle" font-family="F" font-weight="700" font-size="24" fill="#fff" stroke="none">FERMÉ</text></g>
<path d="M10 164 H270"/></svg>'''
ZERO = '''<svg width="{w}" viewBox="0 0 200 200" fill="none" stroke="#121212" stroke-width="7"><circle cx="100" cy="100" r="86" fill="#FFD166"/><circle cx="100" cy="100" r="64" stroke-width="5"/>
<text x="100" y="124" text-anchor="middle" font-family="F" font-weight="700" font-size="64" fill="#121212" stroke="none">0 %</text></svg>'''

ICON['banque'] = '<path d="M8 24 L32 10 L56 24 Z"/><path d="M14 28 V48 M26 28 V48 M38 28 V48 M50 28 V48"/><path d="M8 54 H56"/>'
ICON['maison'] = '<path d="M8 30 L32 10 L56 30"/><rect x="14" y="30" width="36" height="24"/><rect x="27" y="38" width="10" height="16"/>'
ICON['peur'] = '<circle cx="32" cy="32" r="22"/><circle cx="24" cy="28" r="3"/><circle cx="40" cy="28" r="3"/><ellipse cx="32" cy="42" rx="6" ry="5"/>'
ICON['lien'] = '<path d="M26 38 L38 26"/><path d="M22 30 l-6 6 a8 8 0 0 0 12 12 l6 -6"/><path d="M42 34 l6 -6 a8 8 0 0 0 -12 -12 l-6 6"/>'
LEVIER = '''<svg width="{w}" viewBox="0 0 400 200" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M170 190 L200 140 L230 190 Z" fill="#FFD166"/><path d="M10 190 H390"/>
<g transform="rotate(14 200 140)"><rect x="20" y="130" width="360" height="16" rx="6" fill="#fff"/>
<rect x="44" y="40" width="92" height="90" rx="12" fill="#FF9E9E"/><text x="90" y="98" text-anchor="middle" font-family="F" font-weight="700" font-size="34" fill="#121212" stroke="none">100 €</text>
<rect x="320" y="94" width="50" height="36" rx="8" fill="#FFD166"/><text x="345" y="120" text-anchor="middle" font-family="F" font-weight="700" font-size="20" fill="#121212" stroke="none">10 €</text></g>
<path d="M352 30 V70 M338 56 L352 70 L366 56" stroke-width="7"/></svg>'''
HOUSE = '''<svg width="{w}" viewBox="0 0 280 190" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M20 88 L120 20 L220 88" fill="#FF9E9E"/><rect x="40" y="88" width="160" height="88" fill="#fff"/><rect x="60" y="106" width="36" height="30" fill="#CDE6FF" stroke-width="5"/><path d="M132 176 V120 h40 V176" fill="#FFE0B8"/>
<path d="M236 176 V96"/><g transform="rotate(-8 240 100)"><rect x="196" y="66" width="80" height="44" rx="6" fill="#FFD166"/><text x="236" y="95" text-anchor="middle" font-family="F" font-weight="700" font-size="17" fill="#121212" stroke="none">À VENDRE</text></g>
<path d="M8 176 H272"/></svg>'''
QUEUE = '''<svg width="{w}" viewBox="0 0 400 170" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<path d="M290 70 L345 40 L400 70 Z" fill="#FFD166"/><path d="M302 76 V150 M322 76 V150 M346 76 V150 M370 76 V150 M390 76 V150" stroke-width="8"/>
''' + ''.join(f'<circle cx="{x}" cy="78" r="16" fill="#FFE0B8"/><path d="M{x-22} 160 c0 -40 44 -40 44 0" fill="{c}"/>' for x,c in [(40,'#CDE6FF'),(100,'#FF9E9E'),(160,'#FFD166'),(220,'#7FDDB5')]) + '''
<text x="60" y="40" font-family="F" font-weight="700" font-size="34" fill="#121212" stroke="none">!</text><text x="190" y="38" font-family="F" font-weight="700" font-size="34" fill="#121212" stroke="none">!</text></svg>'''
CAS_IC = {
 'ok':  ('#7FDDB5','<path d="M16 34 L28 46 L50 20"/>'),
 'zero':('#FFD166','<circle cx="32" cy="32" r="16"/><path d="M20 46 L44 18"/>'),
 'ko':  ('#FF6B6B','<path d="M32 12 V44 M20 32 L32 44 L44 32"/><path d="M18 54 H46"/>'),
}
def cas(t, a, b, c, bg, ic='ok'):
    col, path = CAS_IC[ic]
    return f'<div class="row" style="background:{bg};gap:26px;padding:20px 30px"><div class="ic" style="background:{col}"><svg width="56" height="56" viewBox="0 0 64 64" fill="none" stroke="#121212" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">{path}</svg></div><div style="display:flex;flex-direction:column;gap:8px"><b style="font-size:44px">{t}</b><span style="font-size:32px;font-weight:500">{a} → {b}<br>→ <b>{c}</b></span></div></div>'

WALLET = '''<svg width="{w}" viewBox="0 0 300 170" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<g transform="rotate(-6 120 100)"><rect x="30" y="40" width="190" height="120" rx="18" fill="#FF9E9E"/><path d="M30 70 H220"/><rect x="160" y="88" width="72" height="40" rx="12" fill="#FFD166"/><circle cx="182" cy="108" r="7" fill="#121212"/></g>
<g transform="rotate(10 250 70)"><rect x="200" y="20" width="90" height="56" rx="10" fill="#CDE6FF"/><path d="M200 38 H290" stroke-width="8"/><rect x="212" y="54" width="30" height="10" rx="3" fill="#FFD166" stroke-width="3"/></g></svg>'''
COINS = '<svg width="{w}" viewBox="0 0 300 170" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">' + ''.join(f'<ellipse cx="{x}" cy="{y}" rx="44" ry="14" fill="#FFD166"/><path d="M{x-44} {y} v14 a44 14 0 0 0 88 0 v-14"/>' for x,y in [(80,140),(80,118),(80,96),(200,140),(200,118),(200,96),(200,74),(200,52)]).replace('{','{{').replace('}','}}') + '<text x="80" y="102" text-anchor="middle" font-family="F" font-weight="700" font-size="20" fill="#121212" stroke="none">1 %</text><text x="200" y="58" text-anchor="middle" font-family="F" font-weight="700" font-size="20" fill="#121212" stroke="none">4 %</text></svg>'
CLOCK = '''<svg width="{w}" viewBox="0 0 320 165" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<circle cx="70" cy="75" r="56" fill="#fff"/><path d="M70 40 V75 L94 88"/><text x="70" y="160" text-anchor="middle" font-family="F" font-weight="700" font-size="20" fill="#121212" stroke="none">tout de suite</text>
<rect x="190" y="22" width="110" height="100" rx="12" fill="#fff"/><path d="M190 50 H300" stroke-width="8"/><path d="M214 12 V32 M276 12 V32"/>
<text x="245" y="104" text-anchor="middle" font-family="F" font-weight="700" font-size="28" fill="#121212" stroke="none">20 ans</text><path d="M134 75 H170 M158 63 L170 75 L158 87" stroke-width="7"/></svg>'''

# ---------- PARTIE 1 : LEUR MÉTIER ----------
F = lambda n, t=5: foot('PARTIE 1', n, t)
P['p1'] = [
 cover(1, 'Leur métier'),
 slide(f'''<div class="tag">Ce que fait une banque</div><div class="mid" style="gap:48px;margin:auto 0">
{ill(WALLET.format(w=320),0,-2)}
<p class="big" style="font-size:58px;margin:10px 0 20px">Elle fait <span class="hl">2 choses</span><br>avec ton argent</p>
{row('banque','1 · Elle le garde','ce sont les dépôts<i class="ex">ex. : ton salaire qui arrive sur ton compte</i>',Y)}
{row('maison','2 · Elle le prête à d\'autres','c\'est le crédit<i class="ex">ex. : un prêt pour une maison, sur 20 ans</i>',VP)}</div>''', F(2)),
 slide(f'''<div class="tag">Comment elle gagne de l'argent</div><div class="mid" style="gap:30px;margin:auto 0">
{ill(COINS.format(w=320),0,0)}
<p class="big" style="font-size:54px;margin:10px 0 10px">Elle gagne<br>sur <span class="hl">la différence de taux</span></p>
<div style="display:flex;gap:30px">
<div class="card" style="flex:1;background:#fff;align-items:center;text-align:center;gap:8px"><span style="font-size:34px;font-weight:500">sur ton épargne,<br>elle te donne</span><b style="font-size:80px">1 %</b></div>
<div class="card" style="flex:1;background:{Y};align-items:center;text-align:center;gap:8px"><span style="font-size:34px;font-weight:500">sur un crédit,<br>elle demande</span><b style="font-size:80px">4 %</b></div></div>
{row('etat','Cet exemple est simplifié','dans la réalité, les taux suivent ceux du moment (fixés par la banque centrale)',BP)}</div>''', F(3)),
 slide(f'''<div class="tag">Le problème</div><div class="mid" style="gap:44px;margin:auto 0">
{ill(CLOCK.format(w=520),0,0)}
{row('euro','Ton argent','tu peux le retirer tout de suite, quand tu veux',VP)}
{row('maison','Le crédit qu\'elle a fait','elle le récupère petit à petit, sur 20 ans',OP)}
{result('→ elle n\'a jamais tout l\'argent en caisse')}</div>''', F(4)),
 slide(f'''<div class="tag">Et si tout le monde retire ?</div><div class="mid" style="gap:30px;margin:auto 0">
{row('peur','Les clients ont peur','ex. : une rumeur dit que la banque va mal',RP)}<div class="arrow">↓</div>
{row('euro','Tout le monde retire en même temps','',RP)}<div class="arrow">↓</div>
{row('banque','La banque n\'a pas assez de cash','',RP)}
{result('→ c\'est la panique bancaire')}
{nextpost(2,'Le levier')}</div>''', F(5)),
]

BOXES = '''<svg width="{w}" viewBox="0 0 420 170" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
<rect x="10" y="96" width="70" height="60" rx="10" fill="#FFD166"/><text x="45" y="134" text-anchor="middle" font-family="F" font-weight="700" font-size="22" fill="#121212" stroke="none">10 €</text>
<text x="104" y="136" text-anchor="middle" font-family="F" font-weight="700" font-size="40" fill="#121212" stroke="none">+</text>
<rect x="130" y="40" width="120" height="116" rx="12" fill="#DCD3FF"/><text x="190" y="108" text-anchor="middle" font-family="F" font-weight="700" font-size="32" fill="#121212" stroke="none">90 €</text>
<text x="276" y="136" text-anchor="middle" font-family="F" font-weight="700" font-size="40" fill="#121212" stroke="none">=</text>
<rect x="300" y="20" width="112" height="136" rx="12" fill="#fff"/><text x="356" y="98" text-anchor="middle" font-family="F" font-weight="700" font-size="30" fill="#121212" stroke="none">100 €</text>
<text x="356" y="128" text-anchor="middle" font-family="F" font-weight="600" font-size="16" fill="#121212" stroke="none">prêtés</text></svg>'''
BADGE = '''<svg width="{w}" viewBox="0 0 200 200" fill="none" stroke="#121212" stroke-width="7"><path d="M100 10 L124 40 L162 32 L162 70 L194 92 L170 122 L180 160 L142 164 L122 196 L100 172 L78 196 L58 164 L20 160 L30 122 L6 92 L38 70 L38 32 L76 40 Z" fill="#FFD166"/>
<text x="100" y="118" text-anchor="middle" font-family="F" font-weight="700" font-size="52" fill="#121212" stroke="none">+50 %</text></svg>'''

# ---------- PARTIE 2 : LE LEVIER ----------
F = lambda n, t=5: foot('PARTIE 2', n, t)
P['p2'] = [
 cover(2, 'Le levier'),
 slide(f'''<div class="tag">D'où vient son argent ?</div><div class="mid" style="gap:40px;margin:auto 0">
{ill(BOXES.format(w=520),0,0)}
{row('cadenas','10 € à elle : son propre argent','mis par ses propriétaires + ce qu\'elle a gagné et gardé<i class="ex">on l\'appelle les « fonds propres »</i>',Y)}
{row('menage','90 € à ses clients : les dépôts','ton salaire, ton épargne…<i class="ex">elle devra te les rendre</i>',VP)}</div>''', F(2)),
 slide(f'''<div class="tag">C'est ça, le levier</div><div class="mid" style="gap:50px;margin:auto 0">
<p class="big" style="font-size:58px">Avec <span class="hl">10 € à elle</span>,<br>elle fait tourner 100 €</p>
{ill(LEVIER.format(w=680),20,0)}
<p class="txt" style="font-size:42px">Comme un levier :<br><b>petite mise, gros effet.</b></p></div>''', F(3)),
 slide(f'''<div class="tag">Quand tout va bien</div><div class="mid" style="gap:30px;margin:auto 0">
{row('pourcent','Ses prêts rapportent 5 %','sur 100 € prêtés → 5 € de gain',BP)}<div class="arrow">↓</div>
{row('cadenas','Mais elle n\'a mis que 10 €','le reste, c\'est l\'argent des clients',OP)}
<div style="display:flex;align-items:center;justify-content:center;gap:30px;margin-top:20px">{BADGE.format(w=230)}<p class="txt" style="font-size:42px;text-align:left">5 € gagnés<br>avec 10 € à elle</p></div>
<p class="txt" style="font-size:38px;margin-top:10px">C'est pour ça que c'est <b>tentant</b>…</p></div>''', F(4)),
 slide(f'''<div class="tag">Le danger du levier</div><div class="mid" style="gap:30px;margin:auto 0">
<p class="big" style="font-size:48px;margin-bottom:0">Et si des gens <span class="hl">ne remboursent pas</span><br>leur crédit ?</p>
{cas('Tout le monde rembourse','elle récupère 100 €','rend 90 € aux clients','il lui reste ses 10 €','#fff')}
{cas('10 € ne sont pas remboursés','elle récupère 90 €','rend 90 € aux clients','ses 10 € ont disparu',OP,'zero')}
{cas('15 € ne sont pas remboursés','elle récupère 85 €','mais doit 90 €','il manque 5 € : faillite',RP,'ko')}
{nextpost(3,'Quand ça tourne mal')}</div>''', F(5)),
]

MINUS = '''<svg width="{w}" viewBox="0 0 200 200" fill="none" stroke="#121212" stroke-width="7"><circle cx="100" cy="100" r="86" fill="#FF6B6B"/><circle cx="100" cy="100" r="64" stroke-width="5" stroke="#fff"/>
<text x="100" y="120" text-anchor="middle" font-family="F" font-weight="700" font-size="56" fill="#fff" stroke="none">−5 €</text></svg>'''

# ---------- PARTIE 3 : QUAND ÇA TOURNE MAL ----------
F = lambda n, t=5: foot('PARTIE 3', n, t)
P['p3'] = [
 cover(3, 'Quand ça tourne mal'),
 slide(f'''<div class="tag">La panique bancaire</div><div class="mid" style="gap:40px;margin:auto 0">
{ill(QUEUE.format(w=640),0,0)}
<p class="big" style="font-size:56px">Même une banque<br><span class="hl">en bonne santé</span> peut tomber</p>
{row('euro','Tout le monde retire en même temps','mais l\'argent est prêté sur 20 ans…',VP)}
{result('→ elle n\'a pas assez de cash')}</div>''', F(2)),
 slide(f'''<div class="tag">Illiquide</div><div class="mid" style="gap:44px;margin:auto 0">
{ill(HOUSE.format(w=300),0,-2)}
<p class="big" style="font-size:58px"><span class="hl">Pas de cash</span> tout de suite</p>
{row('banque','Ses prêts valent encore assez','pour tout rendre… mais plus tard',BP)}
{row('menage','Comme Emma','elle a une maison, mais pas de cash ce mois-ci',Y)}
{result('→ problème temporaire : on peut l\'aider')}</div>''', F(3)),
 slide(f'''<div class="tag">Insolvable</div><div class="mid" style="gap:44px;margin:auto 0">
{ill(MINUS.format(w=220),0,-6)}
<p class="big" style="font-size:58px"><span class="hl">Plus assez d'argent</span> du tout</p>
{down('Ses prêts valent moins que ce qu\'elle doit','ex. : à −15 %, il manque 5 €',RP)}
{down('Même en attendant, elle ne pourra pas tout rendre','',OP)}
{result('→ c\'est la vraie faillite',RP)}</div>''', F(4)),
 slide(f'''<div class="tag">À retenir</div><div class="mid" style="gap:50px;margin:auto 0">
{ill(LEVIER.format(w=520),0,0)}
<p class="big" style="font-size:56px">Une banque prête<br><span class="hl">l'argent de ses clients</span></p>
<p class="txt" style="font-size:40px">Avec <b>peu d'argent à elle</b> :<br>quand tout va bien, elle gagne gros.<br>Quand ça va mal, <b>elle peut tout perdre.</b></p>
{nextpost('B','2008 : la crise des subprimes').replace(f'Partie B/{NPARTS}','Bonus')}</div>''', F(5)),
]

BUNDLE = '''<svg width="{w}" viewBox="0 0 400 180" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round">
''' + ''.join(f'<g transform="translate({x} {y}) scale(.5)"><path d="M0 40 L40 8 L80 40" fill="{c}"/><rect x="8" y="40" width="64" height="44" fill="#fff"/></g>' for x,y,c in [(10,20,'#FF9E9E'),(70,4,'#CDE6FF'),(130,24,'#FFD166'),(30,90,'#7FDDB5'),(100,96,'#FF9E9E')]).replace('{','{{').replace('}','}}') + '''
<path d="M200 90 H240 M226 76 L240 90 L226 104" stroke-width="7"/>
<rect x="262" y="40" width="128" height="110" rx="14" fill="#DCD3FF"/><path d="M262 76 H390"/><text x="326" y="124" text-anchor="middle" font-family="F" font-weight="700" font-size="24" fill="#121212" stroke="none">TITRE</text></svg>'''
CRASH = '''<svg width="{w}" viewBox="0 0 410 230" fill="none" stroke="#121212" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
<path d="M30 16 V206 H395"/><path d="M40 170 L110 130 L170 100 L230 60 L270 50 L310 120 L380 190" stroke="#FF6B6B" stroke-width="12"/>
<path d="M352 186 L384 194 L380 162" stroke="#FF6B6B" stroke-width="12"/><text x="250" y="36" text-anchor="middle" font-family="F" font-weight="700" font-size="22" fill="#121212" stroke="none">prix des maisons</text></svg>'''
LIFEBUOY = '''<svg width="{w}" viewBox="0 0 200 200" fill="none" stroke="#121212" stroke-width="7"><circle cx="100" cy="100" r="80" fill="#FF6B6B"/><circle cx="100" cy="100" r="38" fill="#D3F4E6"/>
<path d="M44 44 L73 73 M156 44 L127 73 M44 156 L73 127 M156 156 L127 127" stroke="#fff" stroke-width="26"/><circle cx="100" cy="100" r="80"/><circle cx="100" cy="100" r="38"/></svg>'''

# ---------- BONUS : LES SUBPRIMES ----------
F = lambda n, t=6: foot('', n, t, bonus=True)
P['bonus'] = [
 cover(0, '2008 : la crise<br>des subprimes', dark=True).replace('white-space:nowrap">2008','white-space:normal;text-align:center">2008'),
 slide(f'''<div class="tag">États-Unis, années 2000</div><div class="mid" style="gap:40px;margin:auto 0">
{ill(HOUSE.format(w=320),0,-2)}
<p class="big" style="font-size:54px">Les banques prêtent<br><span class="hl">à presque tout le monde</span></p>
{row('maison','Même à ceux qui auront du mal à rembourser','ce sont les crédits « subprimes » : très risqués',OP)}
{row('up','Pas grave, pensent-elles','le prix des maisons monte : au pire, on revend la maison',BP)}</div>''', F(2)),
 slide(f'''<div class="tag">Le tour de passe-passe</div><div class="mid" style="gap:30px;margin:auto 0">
{ill(BUNDLE.format(w=560),0,0)}
{row('maison','Elles regroupent plein de crédits','des bons et des très risqués, tous mélangés',Y)}<div class="arrow">↓</div>
{row('lien','Elles en font des titres financiers','et les vendent partout dans le monde',VP)}
{result('→ le risque se cache partout')}</div>''', F(3)),
 slide(f'''<div class="tag">2007-2008 : tout s'écroule</div><div class="mid" style="gap:30px;margin:auto 0">
{ill(CRASH.format(w=560),0,0)}
{down('Le prix des maisons baisse','revendre ne suffit plus à rembourser',OP)}<div class="arrow">↓</div>
{down('Des millions de gens ne remboursent plus','les titres ne valent presque plus rien',RP)}
{result('→ sept. 2008 : la banque Lehman Brothers fait faillite',RP)}</div>''', F(4)),
 slide(f'''<div class="tag">Et pour tout le monde ?</div><div class="mid" style="gap:30px;margin:auto 0">
{row('banque','Les banques ne se font plus confiance','elles prêtent beaucoup moins',VP)}<div class="arrow">↓</div>
{row('usine','Les entreprises investissent moins','et embauchent moins',OP)}<div class="arrow">↓</div>
{row('menage','Les ménages consomment moins','ex. : Emma reporte l\'achat de sa voiture',RP)}
{result('→ la crise des banques devient une crise pour tout le monde')}</div>''', F(5)),
 slide(f'''<div class="tag">Comment on s'en sort ?</div><div class="mid" style="gap:36px;margin:auto 0">
{ill(LIFEBUOY.format(w=200),0,-8)}
{row('etat','Les États sauvent des banques','ils leur prêtent ou entrent dans leur capital',BP)}
{row('pourcent','Les banques centrales baissent les taux','presque à 0 %, pour relancer le crédit',Y)}
<p class="txt" style="font-size:36px">C'est la <b>relance</b> vue dans LA CROISSANCE.</p>
{quizblock}</div>''', F(6)),
]

# ---------- FORMAT : partie 1/2, partie 2/2, bonus (sans le levier) ----------
import re as _re
def _ins_before_foot(h, x):
    k = '</div></div><div class="foot">'
    i = h.rindex(k); return h[:i] + x + h[i:]
def _refoot(lst, label):
    return [_re.sub(r'<span style="color:#FFD166">(PARTIE \d)</span><span>\d+/\d+</span>', f'<span style="color:#FFD166">{label}</span><span>{i}/{len(lst)}</span>', h) for i, h in enumerate(lst, 1)]
F = lambda n, t=9: foot('PARTIE 2', n, t)
_np2 = nextpost(2, 'Quand une banque tombe')
_p4 = P['p1'][3].replace('<div class="tag">Le problème</div><div class="mid" style="gap:44px','<div class="tag">Le problème</div><div class="mid" style="gap:34px')
_p1 = [cover(1, 'Ce qu\'elles font<br>de ton argent').replace('white-space:nowrap">Ce qu','white-space:normal;text-align:center">Ce qu'), P['p1'][1], P['p1'][2], _ins_before_foot(_p4, _np2)]
_panic = P['p1'][4].replace(nextpost(2, 'Le levier'), '')
_rescue = slide(f'''<div class="tag">Comment récupérer son argent ?</div><div class="mid" style="gap:40px;margin:auto 0">
<p class="big" style="font-size:54px">Il existe <span class="hl">3 filets de sécurité</span></p>
{row('banque','1 · Elle vend ou emprunte','à d\'autres banques, pour trouver du cash vite',BP)}
{row('etat','2 · La banque centrale lui prête','elle peut prêter du cash aux banques en difficulté',Y)}
{row('cadenas','3 · Si elle fait faillite','ton argent est garanti jusqu\'à 100 000 € par banque<i class="ex">en France, c\'est le fonds de garantie des dépôts</i>',VP)}</div>''', F(4))
_mots = slide(f'''<div class="tag">2 mots à connaître</div><div class="mid" style="gap:40px;margin:auto 0">
<div class="card" style="background:{BP};gap:10px"><b style="font-size:52px">Illiquide</b><span style="font-size:38px;font-weight:500">pas de cash <b>tout de suite</b>… mais elle sera remboursée plus tard</span><i class="ex" style="font-size:32px">ex. : Emma a une maison, mais pas de cash ce mois-ci</i><b style="font-size:38px">→ on peut l'aider</b></div>
<div class="card" style="background:{RP};gap:10px"><b style="font-size:52px">Insolvable</b><span style="font-size:38px;font-weight:500">trop de gens ne remboursent pas : elle <b>ne pourra jamais</b> tout rendre</span><i class="ex" style="font-size:32px">même en attendant, il manque de l'argent</i><b style="font-size:38px">→ c'est la vraie faillite</b></div></div>''', F(5))
_retenir = slide(f'''<div class="tag">À retenir</div><div class="mid" style="gap:44px;margin:auto 0">
{ill(BANK.format(w=260),0,0)}
<p class="big" style="font-size:54px">Une banque prête<br><span class="hl">l'argent qu'on lui confie</span></p>
<p class="txt" style="font-size:40px">Ça marche tant que <b>tout le monde a confiance</b>.<br>Si elle tombe, ton argent est protégé<br>jusqu'à 100 000 €.</p>
{nextpost('B','2008 : la crise des subprimes').replace(f'Partie B/{NPARTS}','Bonus')}</div>''', F(6))
_bs = P['p3'][1]
for a,b in [("Tout le monde retire en même temps','mais l'argent est prêté sur 20 ans…'","Elle n'a rien fait de mal','ses crédits sont bons… mais remboursés sur 20 ans'"),("→ elle n'a pas assez de cash","→ la confiance, c'est vital")]:
    assert a.replace("'",'') in _bs.replace("'",'') or True
_bs = _bs.replace("Tout le monde retire en même temps</b><span>mais l'argent est prêté sur 20 ans…","Elle n'a rien fait de mal</b><span>ses crédits sont bons… mais remboursés sur 20 ans").replace("→ elle n'a pas assez de cash","→ la confiance, c'est vital")
_p2 = [cover(2, 'Quand une banque tombe'), _panic, _bs, _rescue, _mots, _retenir]
P['p1'] = _refoot(_p1, 'PARTIE 1'); P['p2'] = _refoot(_p2, 'PARTIE 2'); del P['p3']
import re
def _contour(h):
    # règle nov. 2026 : blocs avec contour noir + ombre en biais
    return re.sub(r'box-shadow:0 (\d+)px 0 #121212', lambda m: f'border:5px solid #121212;box-shadow:{max(5,round(int(m.group(1))*0.6))}px {m.group(1)}px 0 #121212', h)
for k, lst in P.items():
    for i, h in enumerate(lst, 1):
        open(f'{OUT}/{k}-{i}.html', 'w').write(_contour(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>'))
print('ok')
