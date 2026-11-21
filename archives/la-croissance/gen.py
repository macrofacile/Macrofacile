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
        sticker = f'<div style="position:absolute;right:-50px;top:-138px;background:{Y};border:5px solid {K};border-radius:30px;padding:12px 40px 20px;transform:rotate(8deg);box-shadow:7px 11px 0 {K};font-weight:700;font-size:96px;line-height:1">BONUS</div>'
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
OP = '#FFF3D6'  # fond abricot : blocs orange éclaircis pour qu'ils ressortent
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

# ---------- PARTIE 1 : L'ÉTAT ----------
F = lambda n, t=5: foot('PARTIE 1', n, t)
P['p1'] = [
 cover(1, 'L\'État'),
 slide(f'''<div class="tag">L'État a 2 boutons</div><div class="mid" style="gap:56px;margin:auto 0">
<p class="big" style="font-size:58px;margin-bottom:90px">Avec, il peut faire<br><span class="hl">accélérer ou ralentir</span> l'économie</p>
{row('euro','1 · Les impôts','ce qu\'on paie à l\'État<i class="ex">ex. : la TVA cachée dans le prix de ta baguette</i>',OP)}
{row('etat','2 · Les dépenses publiques','ce que l\'État paie<i class="ex">ex. : les écoles, les routes, les hôpitaux</i>',BP)}</div>''', F(2)),
 slide(f'''<div class="tag">Accélérer : moins d'impôts</div><div class="mid" style="gap:22px;margin:auto 0">
{row('etat','L\'État baisse les impôts','ex. : Emma paie 50 € d\'impôts en moins par mois',BP)}<div class="arrow">↓</div>
{row('menage','Emma a plus d\'argent','elle s\'offre un resto en plus',OP)}<div class="arrow">↓</div>
{row('usine','Le resto a plus de clients','il embauche un serveur',GP)}
{result('→ on achète plus, on produit plus')}{ill(PLATE.format(w=330),30)}</div>''', F(3)),
 slide(f'''<div class="tag">Accélérer : plus de dépenses</div><div class="mid" style="gap:22px;margin:auto 0">
{row('ecole','L\'État construit une école','il paie une entreprise du bâtiment',BP)}<div class="arrow">↓</div>
{row('usine','L\'entreprise embauche','maçons, électriciens, peintres…',GP)}<div class="arrow">↓</div>
{row('menage','Les ouvriers ont un salaire','et le dépensent : courses, sorties…',OP)}
{result('→ l\'économie accélère')}{ill(SCHOOL.format(w=330),30,2)}</div>''', F(4)),
 slide(f'''<div class="tag">Et pour ralentir ?</div><div class="mid" style="gap:30px;margin:auto 0">
<p class="big" style="font-size:58px;margin-bottom:70px">L'État fait <span class="hl">l'inverse</span></p>
{upr('Il monte les impôts','Emma a moins d\'argent → elle sort moins',RP)}
{down('Il dépense moins','moins de chantiers → moins d\'embauches',RP)}
<p class="txt" style="font-size:38px;margin-top:10px">Pourquoi il ferait ça ?<br><b>Par exemple pour réduire ses dettes.</b></p>
{nextpost(2,'La banque centrale et les taux d\'intérêt')}</div>''', F(5)),
]

# ---------- PARTIE 2 : LES TAUX ----------
F = lambda n, t=5: foot('PARTIE 2', n, t)
P['p2'] = [
 cover(2, 'La banque centrale'),
 slide(f'''<div class="tag">C'est qui ?</div><div class="mid" style="gap:34px;margin:auto 0">
{ill(BANK.format(w=300),0,0)}<p class="big" style="font-size:56px;margin:20px 0 70px">La banque centrale,<br>c'est <span class="hl">la banque des banques</span></p>
{row('etat','Pour l\'euro : la BCE','une seule pour tous les pays de l\'euro<i class="ex">ex. : aux États-Unis, c\'est la Fed</i>',BP)}
{row('pourcent','Elle fixe le taux d\'intérêt','les banques suivent<i class="ex">ex. : le taux de ton crédit monte ou baisse avec</i>',OP)}</div>''', F(2)),
 slide(f'''<div class="tag">Le taux, ça change quoi ?</div><div class="mid" style="gap:30px;margin:auto 0">
{ill(CAR.format(w=380),0,-3)}<p class="big" style="font-size:52px;margin:10px 0 40px">Emma emprunte 10 000 €<br>pour une voiture, sur 4 ans</p>
<div style="display:flex;gap:26px">
<div class="card" style="flex:1;background:{GP};align-items:center;text-align:center;gap:10px"><b style="font-size:76px">2 %</b><span style="font-size:34px;font-weight:500">elle paie environ</span><b style="font-size:46px">400 €</b><span style="font-size:32px;font-weight:500">d'intérêts</span></div>
<div class="card" style="flex:1;background:{RP};align-items:center;text-align:center;gap:10px"><b style="font-size:76px">6 %</b><span style="font-size:34px;font-weight:500">elle paie environ</span><b style="font-size:46px">1 300 €</b><span style="font-size:32px;font-weight:500">d'intérêts</span></div></div>
<p class="txt" style="font-size:40px;margin-top:20px">Même voiture… <b>3 fois plus d'intérêts !</b></p></div>''', F(3)),
 slide(f'''<div class="tag">Taux bas = on accélère</div><div class="mid" style="gap:36px;margin:auto 0">
{row('etat','La BCE baisse les taux d\'intérêt','emprunter coûte moins cher',BP)}<div class="arrow">↓</div>
{row('menage','Emma achète sa voiture','au lieu d\'attendre',OP)}<div class="arrow">↓</div>
{row('usine','Une entreprise emprunte','pour ouvrir un nouveau magasin',GP)}
{result('→ l\'économie accélère')}</div>''', F(4)),
 slide(f'''<div class="tag">Taux hauts = on freine</div><div class="mid" style="gap:26px;margin:auto 0">{ill(PRICE.format(w=300),0,0)}
{upr('La BCE monte les taux d\'intérêt','emprunter coûte plus cher',RP)}
{down('On emprunte moins, on achète moins','Emma garde sa vieille voiture',RP)}
<p class="txt" style="font-size:38px;margin-top:10px">Pourquoi freiner ?<br><b>Pour calmer les prix quand ils montent trop vite<br>(c'est l'inflation).</b></p>
{nextpost(3,'Les deux ensemble')}</div>''', F(5)),
]

# ---------- PARTIE 3 : LES DEUX ENSEMBLE ----------
F = lambda n, t=5: foot('PARTIE 3', n, t)
P['p3'] = [
 cover(3, 'Les deux ensemble'),
 slide(f'''<div class="tag">Une voiture, 2 pédales</div><div class="mid" style="gap:30px;margin:auto 0">
<p class="big" style="font-size:54px">Imagine l'économie<br>comme <span class="hl">une voiture</span></p>
<div style="display:flex;justify-content:center;margin:10px 0">{pedales(600)}</div>
<p class="txt" style="font-size:40px">L'État appuie avec <b>les impôts et les dépenses</b>.<br>La BCE appuie avec <b>les taux d'intérêt</b>.</p></div>''', F(2)),
 slide(f'''<div class="tag">Les deux accélèrent</div><div class="mid" style="gap:36px;margin:auto 0">
{row('etat','L\'État dépense plus','ex. : il construit des écoles',BP)}
<div class="arrow">+</div>
{row('pourcent','La BCE baisse les taux','les crédits coûtent moins cher',OP)}
<div class="arrow">↓</div>
{result('→ ça démarre fort !',GP)}
<p class="txt" style="font-size:36px;margin-top:10px">C'est ce qu'on fait quand l'économie va mal.</p></div>''', F(3)),
 slide(f'''<div class="tag">L'un accélère, l'autre freine</div><div class="mid" style="gap:36px;margin:auto 0">
{row('etat','L\'État dépense plus','il veut faire accélérer',BP)}
<div class="arrow">+</div>
{upr('La BCE monte les taux','elle veut calmer les prix',RP)}
<div class="arrow">↓</div>
{result('→ la voiture avance à peine',RP)}
<p class="txt" style="font-size:36px;margin-top:10px">L'un annule (en partie) ce que fait l'autre.</p></div>''', F(4)),
 slide(f'''<div class="tag">À retenir</div><div class="mid" style="gap:56px;margin:auto 0">
{ill(CAR.format(w=400),0,-3)}<p class="big" style="font-size:58px;margin:30px 0 30px">L'économie a<br><span class="hl">2 pédales</span></p>
<p class="txt" style="font-size:40px">Les impôts et les dépenses pour l'État,<br>les taux d'intérêt pour la BCE.<br><b>Tout dépend de s'ils vont dans le même sens.</b></p>
{nextpost('B','2020 : tout le monde accélère').replace('Partie B/3','Bonus')}</div>''', F(5)),
]

# ---------- BONUS : LE COVID ----------
F = lambda n, t=5: foot('', n, t, bonus=True)
P['bonus'] = [
 cover(0, 'Le Covid :<br>tout le monde accélère', dark=True).replace('white-space:nowrap">Le Covid','white-space:normal;text-align:center">Le Covid'),
 slide(f'''<div class="tag">Mars 2020</div><div class="mid" style="gap:30px;margin:auto 0">
{ill(SHOP.format(w=330),0,-2)}<p class="big" style="font-size:58px;margin:20px 0 40px">Confinement :<br><span class="hl">tout s'arrête</span></p>
{down('Les magasins et les restos ferment','ex. : le resto d\'Emma n\'a plus de clients',RP)}
{down('Les entreprises produisent moins','elles risquent de licencier',RP)}
<p class="txt" style="font-size:40px;margin-top:10px">Il faut appuyer sur <b>l'accélérateur</b>, vite.</p></div>''', F(2)),
 slide(f'''<div class="tag">L'État accélère</div><div class="mid" style="gap:56px;margin:auto 0">
<p class="big" style="font-size:58px;margin-bottom:80px">En France :<br><span class="hl">« quoi qu'il en coûte »</span></p>
{row('menage','Le chômage partiel','l\'État paie une grande partie des salaires<i class="ex">ex. : Emma ne travaille pas, mais reçoit son salaire</i>',BP)}
{row('usine','Des aides aux entreprises','pour éviter qu\'elles ferment',GP)}</div>''', F(3)),
 slide(f'''<div class="tag">La BCE aussi</div><div class="mid" style="gap:30px;margin:auto 0">
{ill(ZERO.format(w=220),0,-6)}<p class="big" style="font-size:54px;margin:20px 0 50px">Elle garde des taux d'intérêt<br><span class="hl">très bas (autour de 0 %)</span></p>
{row('pourcent','Les crédits restent pas chers','ex. : les entreprises peuvent emprunter pour tenir',OP)}
<p class="txt" style="font-size:40px;margin-top:20px">Les <b>2 pédales</b> appuient<br>sur l'accélérateur en même temps.</p></div>''', F(4)),
 slide(f'''<div class="tag">Résultat</div><div class="mid" style="gap:26px;margin:auto 0">
{row('up','2021 : l\'économie repart fort','les magasins rouvrent, on rachète',GP)}
{row('pourcent','2022 : les prix flambent','l\'inflation grimpe',RP)}
{upr('La BCE monte les taux','à partir de l\'été 2022, pour freiner',RP)}
<p class="txt" style="font-size:36px;margin-top:6px">Après l'accélérateur… <b>le frein.</b></p>
{quizblock}</div>''', F(5)),
]
import re
def _contour(h):
    # règle nov. 2026 : blocs avec contour noir + ombre en biais
    return re.sub(r'box-shadow:0 (\d+)px 0 #121212', lambda m: f'border:5px solid #121212;box-shadow:{max(5,round(int(m.group(1))*0.6))}px {m.group(1)}px 0 #121212', h)
for k, lst in P.items():
    for i, h in enumerate(lst, 1):
        open(f'{OUT}/{k}-{i}.html', 'w').write(_contour(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>'))
print('ok')
