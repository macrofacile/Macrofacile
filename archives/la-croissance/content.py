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
