import os, sys, json
TH = sys.argv[1] if len(sys.argv) > 1 else '#C9F2DF'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'slides'
os.makedirs(OUT, exist_ok=True)
THEME='LA MONNAIE'
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
        sticker = f'<div style="position:absolute;right:-30px;top:-92px;background:{Y};color:{K};border:5px solid {K};border-radius:999px;padding:14px 48px 22px;transform:rotate(7deg);box-shadow:7px 11px 0 {K};font-weight:700;font-size:50px;line-height:1;white-space:nowrap">Partie {part}/{NPARTS}</div>'
    subpill = f'<div style="background:#FF6B6B;color:#fff;border:5px solid {K};border-radius:32px;padding:16px 40px 24px;transform:rotate({2 if dark else -1.5}deg);box-shadow:7px 11px 0 {shadow if dark else K};font-weight:{600 if dark else 700};font-size:{70 if dark else (84 if len(sub)<16 else 66)}px;line-height:1.1;white-space:nowrap">{sub}</div>'
    swipe = SWIPE.replace('stroke="#121212" stroke-width="4"', f'stroke="{"#fff" if dark else K}" stroke-width="4"').replace('fill="#fff"', f'fill="{K if dark else "#fff"}"')
    return f'''<div class="s" style="background:{bg}"><div class="in" style="justify-content:space-between;gap:0">
<img src="../logo.png" style="width:240px;transform:rotate(-4deg);align-self:flex-start">
<div style="display:flex;flex-direction:column;gap:64px;align-items:center">
<div style="position:relative"><div style="background:{card_bg};border:6px solid {K};border-radius:44px;padding:26px 50px 40px;transform:rotate(-2deg);box-shadow:10px 18px 0 {shadow};font-weight:700;font-size:138px;line-height:1;white-space:nowrap">{THEME}</div>{sticker}</div>
{subpill}</div><div></div></div>{swipe}</div>'''

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
def line(a,b,bg): return f'<div class="row" style="background:{bg};justify-content:space-between;padding:14px 26px"><b style="font-size:38px">{a}</b><b style="font-size:42px">{b}</b></div>'

P = {}

UL = 'text-decoration:underline;text-decoration-color:#FFD166;text-decoration-thickness:10px;text-underline-offset:12px;text-decoration-skip-ink:none'
quizblock = f'<div style="background:{K};color:#fff;border-radius:30px;padding:16px 30px 20px;display:flex;align-items:center;justify-content:space-between;gap:20px;transform:rotate(-1deg)"><div style="display:flex;flex-direction:column;gap:6px"><span style="color:{Y};font-weight:700;font-size:30px">Teste-toi · quiz gratuit</span><span style="font-weight:600;font-size:42px;line-height:1.1">macrofacile.fr</span></div><span style="font-weight:700;font-size:64px;color:{Y}">→</span></div>'
def bars():
    return f'''<div style="display:flex;align-items:flex-end;justify-content:center;gap:60px;height:330px">
<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><b style="font-size:46px">~15 %</b><div style="width:170px;height:60px;background:{OP};border:5px solid {K};border-radius:14px 14px 0 0"></div><span style="font-weight:600;font-size:30px">Billets et pièces</span></div>
<div style="display:flex;flex-direction:column;align-items:center;gap:12px"><b style="font-size:46px">~85 %</b><div style="width:170px;height:230px;background:{BP};border:5px solid {K};border-radius:14px 14px 0 0"></div><span style="font-weight:600;font-size:30px">Argent sur des comptes</span></div></div>'''
def billet(w=300):
    return f'''<svg width="{w}" viewBox="0 0 240 130" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round">
<rect x="6" y="6" width="228" height="118" rx="12" fill="#BDEFC9"/><rect x="22" y="22" width="196" height="86" rx="8" fill="#fff" stroke-width="4"/>
<circle cx="70" cy="65" r="26" fill="#FFD166" stroke-width="4"/><text x="70" y="75" text-anchor="middle" font-family="F" font-weight="700" font-size="28" fill="#121212" stroke="none">€</text>
<text x="160" y="80" text-anchor="middle" font-family="F" font-weight="700" font-size="44" fill="#121212" stroke="none">20</text></svg>'''
def troc_old(w=330):
    return f'''<svg width="{w}" viewBox="0 0 300 150" fill="none" stroke="#121212" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
<g transform="rotate(-18 70 80)"><rect x="10" y="62" width="130" height="36" rx="18" fill="#F2C29B"/><path d="M40 70 l10 20 M70 70 l10 20 M100 70 l10 20" stroke-width="5"/></g>
<path d="M190 70 h44 l10 26 h40 c8 0 10 14 0 16 h-94 Z" fill="#B9A7FF"/><path d="M190 112 h94" />
<path d="M150 50 l30 30 M180 50 l-30 30" stroke="#D63031" stroke-width="9"/></svg>'''

def troc(w=330):
    return f"""<svg width="{w}" viewBox="0 0 340 150" fill="none" stroke="#121212" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">
<circle cx="50" cy="85" r="34" fill="#FF6B6B"/><path d="M50 51 c0-12 6-20 14-24"/><path d="M58 40 c10-10 24-8 28 0 c-10 6-20 6-28 0 Z" fill="#7FDDB5"/>
<path d="M115 60 l30 30 M145 60 l-30 30" stroke="#D63031" stroke-width="9"/>
<circle cx="210" cy="108" r="30" fill="#fff"/><circle cx="300" cy="108" r="30" fill="#fff"/>
<path d="M210 108 L238 62 L280 62 L300 108" stroke="#FF6B6B" stroke-width="8"/><path d="M238 62 L256 108 L280 62" stroke="#FF6B6B" stroke-width="8"/>
<path d="M210 108 H256"/><path d="M228 48 H250" stroke-width="8"/><path d="M238 62 L232 48"/>
<path d="M280 62 L276 44 H292" stroke-width="7"/><circle cx="256" cy="108" r="5" fill="#121212"/>
</svg>"""

# ---------- PARTIE 1 ----------
F = lambda n, t=4: foot('PARTIE 1', n, t)
P['p1'] = [
 cover(1, 'C\'est quoi ?'),
 slide(f'''<div class="tag">C'est quoi ?</div><div class="mid" style="gap:30px;margin:auto 0">
<p class="big" style="font-size:58px;margin-bottom:70px">La monnaie, c'est<br><span class="hl">ce qui sert à payer</span></p>
{row('euro','Les billets et les pièces','l\'argent qu\'on peut toucher<i class="ex">ex. : le billet de 20 € dans ta poche</i>',OP)}
{row('menage','L\'argent sur ton compte','on ne le touche pas, mais c\'est aussi de la monnaie<i class="ex">ex. : tu paies ton kebab par carte → −10 € sur ton compte</i>',BP)}</div>''', F(2)),
 slide(f'''<div class="tag">Sans monnaie…</div><div class="mid" style="gap:40px;margin:auto 0">
<p class="big" style="font-size:58px;margin-bottom:20px">… il faudrait faire<br><span class="hl">du troc</span></p>
<div style="display:flex;justify-content:center">{troc(500)}</div>
<div class="card"><p class="txt" style="font-size:40px;line-height:1.4">Tu as des pommes et tu veux un vélo…<br><b>mais le vendeur ne veut pas<br>de pommes !</b></p></div></div>''', F(3)),
 slide(f'''<div class="tag">À quoi elle sert ?</div><div class="mid" style="gap:24px;margin:auto 0">
{row('euro','1 · Payer','tout le monde l\'accepte<i class="ex">ex. : ta baguette à 1,20 €</i>',OP)}
{row('pourcent','2 · Comparer les prix','tout se mesure en euros<i class="ex">ex. : un jean 40 €, un vélo 300 €</i>',BP)}
{row('cle','3 · Garder pour plus tard','on peut la mettre de côté<i class="ex">ex. : Emma met 100 € de côté pour ses vacances</i>',VP)}
{nextpost(2,'Les banques et la monnaie')}</div>''', F(4)),
]

# ---------- PARTIE 2 ----------
F = lambda n, t=4: foot('PARTIE 2', n, t)
P['p2'] = [
 cover(2, 'Les banques'),
 slide(f'''<div class="tag">Ta banque, elle fait quoi ?</div><div class="mid" style="gap:70px;margin:auto 0">
{row('etat','Elle garde ton argent','ex. : ton salaire arrive sur ton compte',BP)}
{row('euro','Elle te permet de payer','ex. : ta carte bancaire, un virement',OP)}
{row('up','Elle prête','ex. : un crédit pour une voiture',GP)}</div>''', F(2)),
 slide(f'''<div class="tag">Le crédit, c'est quoi ?</div><div class="mid" style="gap:16px;margin:auto 0">
{row('menage','Emma veut une voiture à 10 000 €','mais elle n\'a pas tout cet argent',BP)}<div class="arrow">↓</div>
{row('etat','La banque lui prête 10 000 €','Emma achète la voiture tout de suite',VP)}<div class="arrow">↓</div>
{row('euro','Emma rembourse chaque mois','ex. : environ 225 €/mois pendant 4 ans',OP)}
<p class="big" style="font-size:46px;margin:26px 0 10px">Au total, elle rembourse un peu plus :<br><span class="hl">ce sont les intérêts</span></p>
<p class="txt" style="font-size:34px">→ C'est comme ça que la banque gagne de l'argent</p></div>''', F(3)),
 slide(f'''<div class="tag">Ce que ça permet</div><div class="mid" style="gap:36px;margin:auto 0">
<p class="big" style="font-size:52px;margin-bottom:70px">Acheter maintenant…<br><span class="hl">et payer petit à petit</span></p>
{row('etat','Une famille achète une maison','sans attendre 20 ans d\'économies',BP)}
{row('usine','Une entreprise ouvre un magasin','et embauche',GP)}
{nextpost(3,'Une journée avec Emma')}</div>''', F(4)),
]

# ---------- PARTIE 3 : UNE JOURNEE ----------
F = lambda n, t=5: foot('PARTIE 3', n, t)
def moment(h,title,sub,tag,bg):
    return f'''<div style="display:flex;gap:22px;align-items:stretch">
<div style="display:flex;flex-direction:column;align-items:center;width:150px;flex:none"><div style="background:{K};color:{Y};border-radius:999px;padding:10px 22px 16px;font-weight:700;font-size:52px">{h}</div><div style="flex:1;width:6px;background:{K};margin-top:8px;border-radius:3px"></div></div>
<div style="flex:1;background:{bg};border-radius:30px;box-shadow:0 9px 0 {K};padding:40px 32px 44px;display:flex;flex-direction:column;gap:14px;margin-bottom:70px">
<b style="font-size:42px;line-height:1.15;white-space:nowrap">{title}</b><span style="font-size:40px;line-height:1.3">{sub}</span>
<span style="align-self:flex-start;background:#fff;border-radius:999px;padding:6px 22px 10px;font-weight:700;font-size:36px;margin-top:6px">→ {tag}</span></div></div>'''
P['p3'] = [
 cover(3, 'Une journée avec Emma'),
 slide(f'''<div class="tag">Le matin</div><div class="mid" style="gap:10px;margin:60px 0 auto">
{moment('8h','Son salaire tombe','elle ne le touche pas… mais c\'est bien de la monnaie','l\'argent sur un compte',BP)}
{moment('12h','Sandwich à 6 € par carte','le resto accepte, comme tout le monde','payer',OP)}</div>''', F(2)),
 slide(f'''<div class="tag">L'après-midi</div><div class="mid" style="gap:10px;margin:60px 0 auto">
{moment('15h','Elle hésite entre 2 jeans','un à 40 €, l\'autre à 60 € : facile de choisir','comparer',GP)}
{moment('18h','Elle met 100 € de côté','pour ses vacances cet été','garder pour plus tard',VP)}</div>{deco(jar(190),445,140,-5)}''', F(3)),
 slide(f'''<div class="tag">Le soir</div><div class="mid" style="gap:10px;margin:60px 0 auto">
{moment('19h','Un crédit pour une voiture','la banque lui prête 10 000 €, elle rembourse chaque mois','les banques',Y)}
<p class="txt" style="font-size:40px;margin-top:20px">… avec un peu plus à rembourser :<br><b>les intérêts</b></p>
<div style="display:flex;justify-content:center;margin-top:30px;transform:rotate(-3deg)"><svg width="520" viewBox="0 0 300 140" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"><path d="M20 96 V74 c0-8 6-12 14-14 l30-6 l26-26 c6-6 12-8 20-8 h70 c10 0 16 4 22 12 l20 26 l40 8 c8 2 12 8 12 16 v14 Z" fill="#FF9E9E"/><path d="M98 52 l18-18 h40 v18 Z M168 34 h18 l14 18 h-32 Z" fill="#CDE6FF"/><circle cx="76" cy="100" r="20" fill="#121212"/><circle cx="76" cy="100" r="7" fill="#fff" stroke="none"/><circle cx="226" cy="100" r="20" fill="#121212"/><circle cx="226" cy="100" r="7" fill="#fff" stroke="none"/></svg></div></div>''', F(4)),
 slide(f'''<div class="tag">À retenir</div><div class="mid" style="gap:60px;margin:auto 0">
<p class="big" style="font-size:60px;margin-bottom:40px">La monnaie est partout<br><span class="hl">dans ta journée.</span></p>
<p class="txt" style="font-size:40px">Payer, comparer, garder…<br>et les banques la font circuler.</p>
{nextpost('B','Pourquoi un billet de 20 € vaut 20 € ?').replace('Partie B/3','Bonus')}</div>''', F(5)),
]

# ---------- BONUS ----------
F = lambda n, t=5: foot('', n, t, bonus=True)
P['bonus'] = [
 cover(0, 'Pourquoi un billet<br>de 20 € vaut 20 € ?', dark=True).replace('white-space:nowrap">Pourquoi','white-space:normal;text-align:center">Pourquoi'),
 slide(f'''<div class="tag">Imagine…</div><div class="mid" style="gap:44px;margin:auto 0">
<p class="big" style="font-size:60px;margin-bottom:20px">Un billet de 20 €,<br>c'est juste… <span style="{UL}">du papier</span>.</p>
<div style="display:flex;justify-content:center">{billet(360)}</div>
<div class="card"><p class="txt" style="font-size:40px">Il coûte quelques centimes à fabriquer.<br><b>Alors pourquoi tout le monde l'accepte ?</b></p></div></div>''', F(2)),
 slide(f'''<div class="tag">Avant</div><div class="mid" style="gap:40px;margin:auto 0">
<p class="big" style="font-size:58px;margin-bottom:20px">Autrefois, la monnaie<br><span class="hl">valait son poids en métal</span></p>
<div style="display:flex;justify-content:center"><svg width="320" viewBox="0 0 240 150" fill="none" stroke="#121212" stroke-width="6"><ellipse cx="80" cy="96" rx="58" ry="46" fill="#FFD166"/><ellipse cx="80" cy="96" rx="40" ry="30" stroke-width="4"/><text x="80" y="107" text-anchor="middle" font-family="F" font-weight="700" font-size="28" fill="#121212" stroke="none">OR</text><ellipse cx="170" cy="70" rx="50" ry="40" fill="#E6E6E6"/><ellipse cx="170" cy="70" rx="34" ry="26" stroke-width="4"/><path d="M152 58 q8 -10 18 -8" stroke-width="5" stroke-linecap="round"/></svg></div>
{row('euro','Des pièces en or ou en argent','leur valeur, c\'était le métal à l\'intérieur',OP)}
<p class="txt" style="font-size:40px;margin-top:10px">Aujourd'hui, un billet, c'est du papier.<br><b>Alors d'où vient sa valeur ?</b></p></div>''', F(3)),
 slide(f'''<div class="tag">La réponse : la confiance</div><div class="mid" style="gap:40px;margin:auto 0">
<p class="big" style="font-size:50px;margin-bottom:60px">Tu acceptes un billet de 20 €…<br><span class="hl">parce que tu sais que le boulanger<br>l'acceptera aussi</span></p>
{row('etat','L\'euro est la monnaie officielle','en France, un commerçant doit l\'accepter',VP)}
{row('pourcent','La banque centrale veille','à ce que sa valeur reste stable',BP)}</div>''', F(4)),
 slide(f'''<div class="tag">Et chez nous ?</div><div class="mid" style="gap:30px;margin:auto 0">
<p class="big" style="font-size:52px;margin-bottom:20px">Le 1er janvier 2002, la France<br><span class="hl">change de monnaie</span></p>
<div style="display:flex;gap:20px;align-items:center">
<div class="row" style="background:{RP};flex:1;flex-direction:column;gap:4px;padding:22px"><b style="font-size:40px">Le franc</b><span style="font-size:30px;font-weight:500">au revoir</span></div>
<b style="font-size:60px">→</b>
<div class="row" style="background:{GP};flex:1;flex-direction:column;gap:4px;padding:22px"><b style="font-size:40px">L'euro</b><span style="font-size:30px;font-weight:500">bonjour</span></div></div>
<p class="txt" style="font-size:36px">Du jour au lendemain, tout le monde<br>accepte les nouveaux billets.<br><b>Pourquoi ? Parce que tout le monde a confiance.</b></p>
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
