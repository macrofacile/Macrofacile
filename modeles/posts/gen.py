import os, sys, json
TH = sys.argv[1] if len(sys.argv) > 1 else '#C9F2DF'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'slides'
os.makedirs(OUT, exist_ok=True)
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
    sticker = f'<div style="position:absolute;right:-10px;top:-92px;background:{Y};border-radius:30px;padding:12px 40px 20px;transform:rotate(8deg);box-shadow:0 10px 0 {K};font-weight:700;font-size:96px;line-height:1">BONUS</div>' if dark else ''
    partpill = '' if dark else f'<div style="background:{Y};color:{K};border-radius:999px;padding:14px 48px 22px;transform:rotate(2deg);box-shadow:0 10px 0 {K};font-weight:700;font-size:70px;line-height:1">Partie {part}/4</div>'
    subpill = f'<div style="background:#FF6B6B;color:#fff;border-radius:32px;padding:16px 40px 24px;transform:rotate({2 if dark else -1.5}deg);box-shadow:0 10px 0 {K if not dark else K};font-weight:{500 if dark else 600};font-size:{76 if dark else 60}px;line-height:1.1;white-space:nowrap">{sub}</div>'
    swipe = SWIPE.replace('stroke="#121212" stroke-width="4"', f'stroke="{"#fff" if dark else K}" stroke-width="4"').replace('fill="#fff"', f'fill="{K if dark else "#fff"}"')
    return f'''<div class="s" style="background:{bg}"><div class="in" style="justify-content:space-between;gap:0">
<img src="../logo.png" style="width:300px;transform:rotate(-4deg);align-self:flex-start">
<div style="display:flex;flex-direction:column;gap:50px;align-items:center">
<div style="position:relative"><div style="background:{card_bg};border-radius:44px;padding:24px 56px 38px;transform:rotate(-2deg);box-shadow:0 14px 0 {shadow};font-weight:700;font-size:124px;line-height:1;white-space:nowrap">LA DEMANDE</div>{sticker}</div>
{partpill}{subpill}</div><div></div></div>{swipe}</div>'''

def nextpost(n, t):
    return f'<div style="background:{K};color:#fff;border-radius:30px;padding:16px 30px 20px;display:flex;align-items:center;justify-content:space-between;gap:20px;transform:rotate(-1deg)"><div style="display:flex;flex-direction:column;gap:6px"><span style="color:{Y};font-weight:700;font-size:30px">Prochain post · Partie {n}/4</span><span style="font-weight:600;font-size:42px;line-height:1.1">{t}</span></div><span style="font-weight:700;font-size:64px;color:{Y}">→</span></div>'

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
# ---------- PARTIE 1 ----------
F = lambda n, t=4: foot('PARTIE 1', n, t)
P['p1'] = [
 cover(1, 'Qui achète ?'),
 slide(f'''<div class="tag">L'idée</div><div class="mid">
<p class="big" style="margin-bottom:70px">Tout ce qu'on produit dans le pays…<br><span class="hl">finit par être acheté.</span></p>
<div class="card"><p class="txt" style="font-size:44px">Le PIB, c'est donc aussi<br><b style="font-weight:700">la somme de tous les achats finaux.</b></p><p class="txt" style="font-size:32px;line-height:1.4">Ex. : ta baguette, la machine d'une usine,<br>l'école construite par l'État…</p></div>
<p class="txt" style="font-weight:600;font-size:56px"><span style="text-decoration:underline;text-decoration-color:#FFD166;text-decoration-thickness:10px;text-underline-offset:12px;text-decoration-skip-ink:none">Mais acheté… par qui ?</span></p></div>''', F(2)),
 slide(f'''<div class="tag">Les 4 acheteurs</div><div class="mid" style="gap:22px">
{row('menage','Les ménages','→ la consommation : courses, voiture, vacances',GP)}
{row('usine','Les entreprises','→ l\'investissement : machines, terrains, bâtiments',VP)}
{row('etat','L\'État','→ les dépenses publiques : écoles, hôpitaux, avions',BP)}
{row('monde','L\'étranger','→ les exportations : du vin français vendu à Sydney',OP)}
<div style="display:flex;align-items:center;gap:18px;margin-top:14px"><div style="flex:1;border-top:5px dashed {K}"></div><b style="font-size:36px">+ 1 cas à part</b><div style="flex:1;border-top:5px dashed {K}"></div></div>
{row('carton','Les stocks','produit mais pas vendu → personne ne l\'a acheté, mais ça compte quand même dans le PIB<br><b style="font-size:32px;font-weight:600">Ex. : 100 vélos produits, 90 vendus → 10 en stock</b>','#fff')}</div>''', F(3)),
 slide(f'''<div class="tag">L'étranger</div><div class="mid" style="gap:30px;margin:10px 0 0">
<div style="display:flex;flex-direction:column;gap:30px;margin-top:-10px">
<div><div style="font-weight:600;font-size:48px;line-height:1.2;white-space:nowrap">On vend à l'étranger → <span class="hl">exportations</span></div><div style="font-weight:500;font-size:32px;margin-top:4px">Ex. : la France vend des Airbus et du vin</div></div>
<div><div style="font-weight:600;font-size:48px;line-height:1.2;white-space:nowrap">On achète à l'étranger → <span class="hl">importations</span></div><div style="font-weight:500;font-size:32px;margin-top:4px">Ex. : la France achète des iPhone et du pétrole</div></div></div>
<div class="card"><span style="text-align:left;font-weight:600;font-size:40px">La différence, c'est la balance commerciale</span>
{row('up','Excédent → on vend plus','Ex. : on vend pour 120, on achète pour 100',GP)}
{row('down','Déficit → on achète plus','Ex. : on vend pour 100, on achète pour 120',RP)}</div>
<p class="txt" style="font-size:42px;font-weight:600;text-align:center"><span style="text-decoration:underline;text-decoration-color:#FFD166;text-decoration-thickness:9px;text-underline-offset:11px;text-decoration-skip-ink:none">La France est en déficit depuis des années.</span></p>
{nextpost(2,'Pourquoi ils achètent ?')}</div>''', F(4)),
 
]
# ---------- PARTIE 2 ----------
F = lambda n, t=5: foot('PARTIE 2', n, t)
def line(a,b,bg): return f'<div class="row" style="background:{bg};justify-content:space-between;padding:14px 26px"><b style="font-size:38px">{a}</b><b style="font-size:42px">{b}</b></div>'
P['p2'] = [
 cover(2, 'Pourquoi ils achètent ?'),
 slide(f'''<div class="tag">Les ménages</div><div class="mid" style="gap:40px;margin:50px 0 auto">
<p class="big" style="font-size:52px">Ils consomment selon leur<br><span class="hl">revenu disponible</span></p>
<div class="card" style="gap:12px"><span style="text-align:center;font-weight:600;font-size:34px">= ce qui reste vraiment pour vivre</span>
{line('Salaire','2 000 €',BP)}{line('− Impôts','200 €',RP)}{line('+ Aides (ex. : APL)','100 €',GP)}{line('Revenu disponible','1 900 €',Y)}</div>
<div style="display:flex;gap:18px">
<div class="row" style="background:{GP};flex:1;flex-direction:column;gap:2px;padding:16px"><b style="font-size:34px">Revenu ↑</b><span style="font-size:28px">→ on consomme plus</span></div>
<div class="row" style="background:{RP};flex:1;flex-direction:column;gap:2px;padding:16px"><b style="font-size:34px">Revenu ↓</b><span style="font-size:28px">→ on consomme moins</span></div></div>
<p class="txt" style="font-size:32px">Ex. : une prime de 300 € → un resto, un nouveau jean…</p></div>''', F(2)),
 slide(f'''<div class="tag">Les entreprises</div><div class="mid" style="gap:40px;margin:50px 0 auto">
<p class="big" style="font-size:52px">Elles <span class="hl">investissent</span> :<br>machines, bâtiments…</p>
<p class="txt" style="font-size:34px;margin-top:-14px">Ex. : une boulangerie achète un nouveau four</p>
<div class="card" style="margin-top:50px;gap:26px;padding:40px 36px 44px"><span style="text-align:center;font-weight:600;font-size:38px">Ça dépend surtout de…</span>
{row('pourcent','Les taux d\'intérêt','taux bas → emprunter coûte moins cher → on investit plus<i class="ex">Ex. : emprunter 10&nbsp;000&nbsp;€ coûte 200&nbsp;€/an à 2&nbsp;%, 500&nbsp;€/an à 5&nbsp;%</i>',VP)}
{row('cle','L\'usure des machines','une machine trop vieille → il faut la remplacer<i class="ex">Ex. : le four a 15 ans et tombe en panne</i>',OP)}</div></div>''', F(3)),
 slide(f'''<div class="tag">L'État</div><div class="mid" style="gap:40px;margin:50px 0 auto">
<p class="big" style="font-size:52px">Ses dépenses et ses impôts sont <span class="hl">décidés chaque année</span> dans le budget</p>
<p class="txt" style="font-size:36px;margin-top:-10px">→ c'est la <b>politique budgétaire</b></p>
<div class="card" style="gap:16px">
{row('etat','Il dépense','Ex. : construire une école, acheter des avions, payer les profs',BP)}
{row('euro','Il prélève des impôts','Ex. : la TVA sur tes courses, l\'impôt sur le revenu',OP)}</div>
<p class="txt" style="font-size:34px">Ex. : en crise, l'État peut dépenser plus pour relancer l'économie</p></div>''', F(4)),
 slide(f'''<div class="tag">L'État : attention !</div><div class="mid" style="gap:36px;margin:60px 0 auto">
<p class="big" style="font-size:50px;margin-bottom:24px">L'État compte dans la demande<br>seulement quand il <span class="hl">achète</span></p>
{row('up','Ça compte','Ex. : le salaire d\'un prof → l\'État achète son travail<i class="ex" style="font-weight:400;font-size:32px">Ex. : un nouvel hôpital → l\'État achète sa construction</i>',GP)}
{row('down','Ça ne compte pas','Ex. : les APL, le chômage → l\'État donne de l\'argent, il n\'achète rien<i class="ex" style="margin-top:12px">↳ cet argent va aux ménages : c\'est eux qui le dépensent (le « + Aides » du revenu disponible)</i>',RP)}
{nextpost(3,'L\'effet boule de neige')}</div>''', F(5)),
]
# ---------- PARTIE 3 ----------
F = lambda n, t=5: foot('PARTIE 3', n, t)
def box(t, bg, ex=''):
    e = f'<span style="font-weight:500;font-size:30px;line-height:1.2">{ex}</span>' if ex else ''
    return f'<div class="row" style="background:{bg};justify-content:center;text-align:center;flex-direction:column;gap:6px;padding:28px 20px"><b style="font-size:42px;line-height:1.15">{t}</b>{e}</div>'
P['p3'] = [
 cover(3, 'L\'effet boule de neige'),
 slide(f'''<div class="tag">Tout part de là</div><div class="mid" style="gap:64px;margin:90px 0 auto">
<p class="big" style="font-size:58px">Quand les gens achètent plus…<br><span class="hl" style="white-space:nowrap">la demande augmente.</span></p>
<p class="txt" style="font-size:42px;margin-top:-30px">→ et les entreprises produisent plus</p>
<div class="card" style="gap:18px;padding:40px 36px 44px"><span style="font-weight:600;font-size:40px;text-align:center">Ex. : à Noël</span>
{row('menage','Les gens achètent plus de jouets','→ la demande de jouets augmente',GP)}
{row('usine','Les usines produisent plus','elles embauchent des intérimaires',VP)}</div>
<p class="txt" style="font-size:40px">Et ces intérimaires… <b>vont dépenser leur salaire.</b></p></div>''', F(2)),
 slide(f'''<div class="tag">La boule de neige</div><div class="mid" style="gap:16px;margin:40px 0 auto">
{box('La demande monte','#fff','Ex. : les gens achètent plus de vélos')}<div class="arrow">↓</div>
{box('Les entreprises produisent plus',GP,'l\'usine fabrique plus de vélos')}<div class="arrow">↓</div>
{box('Les revenus montent',BP,'elle embauche → de nouveaux salaires')}<div class="arrow">↓</div>
{box('Les gens consomment plus',Y,'les ouvriers vont au resto, font les courses…')}
<p class="txt" style="font-size:40px;font-weight:600;margin-top:10px">… et la demande remonte encore ↺</p></div>''', F(3)),
 slide(f'''<div class="tag">Un autre exemple</div><div class="mid" style="gap:16px;margin:40px 0 auto">
{row('pont','L\'État construit un pont','il paie une entreprise → de la demande en plus',BP)}<div class="arrow">↓</div>
{row('menage','L\'entreprise embauche','des ouvriers touchent un salaire',GP)}<div class="arrow">↓</div>
{row('euro','Les ouvriers dépensent','resto, courses, sorties',OP)}<div class="arrow">↓</div>
{row('up','Les commerces vendent plus','la demande augmente encore → ils embauchent',Y)}
<p class="txt" style="font-size:36px;margin-top:14px">→ 1 € dépensé au départ peut créer <b>plus d'1 €</b> d'activité au total</p></div>''', F(4)),
 slide(f'''<div class="tag">Et à l'envers ?</div><div class="mid" style="gap:80px;margin:auto 0">
<p class="big" style="font-size:56px">Ça marche aussi <span class="hl">dans l'autre sens.</span></p>
<div class="card" style="background:{RP};gap:24px;padding:48px 36px 52px"><div style="display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:12px 10px"><span style="display:inline-flex;align-items:center;gap:8px;background:#fff;border-radius:999px;padding:6px 16px 8px;font-weight:700;font-size:32px">Demande<svg width="30" height="30" viewBox="0 0 30 30" style="flex:none"><circle cx="15" cy="15" r="15" fill="#D63031"/><path d="M15 7 V22 M9 16 L15 22 L21 16" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="font-weight:700;font-size:34px">→</span><span style="display:inline-flex;align-items:center;gap:8px;background:#fff;border-radius:999px;padding:6px 16px 8px;font-weight:700;font-size:32px">Production<svg width="30" height="30" viewBox="0 0 30 30" style="flex:none"><circle cx="15" cy="15" r="15" fill="#D63031"/><path d="M15 7 V22 M9 16 L15 22 L21 16" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="font-weight:700;font-size:34px">→</span><span style="display:inline-flex;align-items:center;gap:8px;background:#fff;border-radius:999px;padding:6px 16px 8px;font-weight:700;font-size:32px">Licenciements</span><span style="font-weight:700;font-size:34px">→</span><span style="display:inline-flex;align-items:center;gap:8px;background:#fff;border-radius:999px;padding:6px 16px 8px;font-weight:700;font-size:32px">Revenus<svg width="30" height="30" viewBox="0 0 30 30" style="flex:none"><circle cx="15" cy="15" r="15" fill="#D63031"/><path d="M15 7 V22 M9 16 L15 22 L21 16" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="font-weight:700;font-size:34px">→</span><span style="display:inline-flex;align-items:center;gap:8px;background:#fff;border-radius:999px;padding:6px 16px 8px;font-weight:700;font-size:32px">Consommation<svg width="30" height="30" viewBox="0 0 30 30" style="flex:none"><circle cx="15" cy="15" r="15" fill="#D63031"/><path d="M15 7 V22 M9 16 L15 22 L21 16" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span><span style="font-weight:700;font-size:38px">↺</span></div>
<span style="font-weight:600;font-size:32px;text-align:center;margin-top:8px">Ex. : une usine ferme → 500 chômeurs → ils achètent moins → la demande baisse dans les commerces du coin → ils licencient aussi</span></div>
{nextpost(4,'Le récap')}</div>''', F(5)),
]
# ---------- PARTIE 4 : RECAP ----------
F = lambda n, t=5: foot('PARTIE 4', n, t)
def mini(icon,t,sub,bg): return row(icon,t,sub,bg)
P['p4'] = [
 cover(4, 'Le récap'),
 slide(f'''<div class="tag">1 · Qui achète ?</div><div class="mid" style="gap:26px;margin:auto 0">
<div style="display:grid;grid-template-columns:1fr 1fr;gap:26px">
{tile('menage','Les ménages','consomment','ex. : courses, vacances',GP,-2)}
{tile('usine','Les entreprises','investissent','ex. : un nouveau four',VP,1.5)}
{tile('etat','L\'État','dépense','ex. : une école',BP,1.5)}
{tile('monde','L\'étranger','achète nos exportations','ex. : des Airbus',OP,-2)}</div>
<div style="display:flex;align-items:center;gap:20px;background:#fff;border:4px dashed {K};border-radius:28px;padding:18px 26px">{ic('carton')}<div style="font-weight:500;font-size:32px;line-height:1.3"><b>+ les stocks</b> : produit mais pas vendu<br>ex. : 10 vélos en réserve</div></div></div>''', F(2)),
 slide(f'''<div class="tag">2 · Pourquoi ils achètent ?</div><div class="mid" style="gap:44px;margin:auto 0">
<p class="big" style="font-size:44px;font-weight:500">Ce qui les fait acheter plus… ou moins</p>
{why('Les ménages','leur revenu disponible','ex. : une prime → un resto en plus',GP)}
{why('Les entreprises','les taux d\'intérêt et l\'usure','ex. : taux bas → on achète le four',VP)}
{why('L\'État','son budget annuel','attention : seulement ce qu\'il achète (pas les APL)',BP)}</div>''', F(3)),
 slide(f'''<div class="tag">3 · La boule de neige</div><div class="mid" style="gap:24px;margin:auto 0">
{box('La demande monte','#fff')}<div class="arrow">↓</div>{box('Les entreprises produisent plus',GP)}<div class="arrow">↓</div>{box('Les revenus montent',BP)}<div class="arrow">↓</div>{box('Les gens consomment plus',Y)}
<p class="txt" style="font-size:38px;font-weight:600;margin-top:10px">… et ça repart ↺ (dans les deux sens !)</p></div>''', F(4)),
 slide(f'''<div class="tag">À retenir</div><div class="mid" style="gap:60px;margin:auto 0">
<p class="big" style="font-size:76px">C'est la demande<br><span class="hl">qui fait tourner</span><br>l'économie.</p>
<p class="txt" style="font-size:40px">Quiz et lexique gratuits sur<br><b>macrofacile.fr</b></p>
{nextpost('B','Le paradoxe de l\'épargne').replace('Partie B/4','Bonus')}</div>''', F(5)),
]
# ---------- BONUS ----------
F = lambda n, t=5: foot('', n, t, bonus=True)
quizblock = f'<div style="background:{K};color:#fff;border-radius:30px;padding:16px 30px 20px;display:flex;align-items:center;justify-content:space-between;gap:20px;transform:rotate(-1deg)"><div style="display:flex;flex-direction:column;gap:6px"><span style="color:{Y};font-weight:700;font-size:30px">Teste-toi · quiz gratuit</span><span style="font-weight:600;font-size:42px;line-height:1.1">macrofacile.fr</span></div><span style="font-weight:700;font-size:64px;color:{Y}">→</span></div>'
P['bonus'] = [
 cover(0, 'Le paradoxe<br>de l\'épargne', dark=True).replace('white-space:nowrap">Le paradoxe','white-space:normal;text-align:center">Le paradoxe'),
 slide(f'''<div class="tag">Imagine…</div><div class="mid" style="gap:56px;margin:auto 0">
<p class="big" style="font-size:66px;margin-bottom:50px">Et si tout le monde<br><span style="text-decoration:underline;text-decoration-color:#FFD166;text-decoration-thickness:10px;text-underline-offset:12px;text-decoration-skip-ink:none">arrêtait de dépenser</span>&nbsp;?</p>
<div class="card" style="gap:16px;padding:40px 36px 44px"><p class="txt" style="font-size:42px;line-height:1.45">Les gens ont peur de l'avenir…<br>→ ils <span class="hl">épargnent plus</span><br>→ ils <span class="hl">consomment moins</span></p>
<p class="txt" style="font-size:32px">Ex. : Léa met 200 € de côté chaque mois<br>au lieu d'aller au resto</p></div>
<p class="txt" style="font-size:40px;text-align:left;padding-left:20px">Pour Léa, c'est prudent.<br>Logique.</p></div>{deco(jar(230),110,175,-5)}''', F(2)),
 slide(f'''<div class="tag">Sauf que…</div><div class="mid" style="gap:16px;margin:auto 0">
<p class="big" style="font-size:46px;margin-bottom:14px">… tout le monde fait pareil en même temps</p>
{row('down','La demande chute','ex. : le resto de Léa perd des clients',RP)}<div class="arrow">↓</div>
{row('usine','Les entreprises vendent moins','donc elles produisent moins',VP)}<div class="arrow">↓</div>
{row('menage','Licenciements','ex. : le resto licencie un serveur',OP)}<div class="arrow">↓</div>
{row('euro','Les revenus baissent','pour tout le pays',BP)}</div>''', F(3)),
 slide(f'''<div class="tag">Le paradoxe</div><div class="mid" style="gap:44px;margin:auto 0">
<p class="big" style="font-size:60px;margin-bottom:50px">Tout le monde voulait<br><span class="hl" style="white-space:nowrap">épargner plus…</span></p>
<div class="card" style="gap:18px;padding:40px 36px 44px"><p class="txt" style="font-size:44px">… mais avec des revenus en baisse,<br><b>l'épargne totale n'augmente pas.</b></p>
<p class="txt" style="font-size:38px">Elle peut même baisser.</p></div>
<p class="txt" style="font-size:34px;text-align:left;padding-left:20px">Ex. : Léa perd des heures<br>au travail → elle n'arrive plus<br>à mettre 200 € de côté</p></div>{deco(jar(230,False),100,215,5)}''', F(4)),
 slide(f'''<div class="tag">À retenir</div><div class="mid" style="gap:36px;margin:auto 0">
<p class="big" style="font-size:50px;margin-bottom:50px;line-height:1.4">Ce qui est bon pour une personne<br><span class="hl" style="white-space:nowrap">peut être mauvais pour tout le pays.</span></p>
{row('menage','Toi, tu épargnes','→ malin',GP)}{row('monde','Tout le monde épargne en même temps','→ la demande s\'effondre',RP)}
{quizblock}</div>''', F(5)),
]

for k, lst in P.items():
    for i, h in enumerate(lst, 1):
        open(f'{OUT}/{k}-{i}.html', 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{h}</body></html>')
print('ok')
