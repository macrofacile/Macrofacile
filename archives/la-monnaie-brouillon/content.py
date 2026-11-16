
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
{moment('18h','Elle met 100 € de côté','pour ses vacances cet été','garder pour plus tard',VP)}</div>''', F(3)),
 slide(f'''<div class="tag">Le soir</div><div class="mid" style="gap:10px;margin:60px 0 auto">
{moment('19h','Un crédit pour une voiture','la banque lui prête 10 000 €, elle rembourse chaque mois','les banques',Y)}
<p class="txt" style="font-size:40px;margin-top:-20px">… avec un peu plus à rembourser :<br><b>les intérêts</b></p>
<div style="display:flex;justify-content:center;margin-top:30px;transform:rotate(-3deg)"><svg width="520" viewBox="0 0 300 140" fill="none" stroke="#121212" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"><path d="M20 96 V74 c0-8 6-12 14-14 l30-6 l26-26 c6-6 12-8 20-8 h70 c10 0 16 4 22 12 l20 26 l40 8 c8 2 12 8 12 16 v14 Z" fill="#FF9E9E"/><path d="M98 52 l18-18 h40 v18 Z M168 34 h18 l14 18 h-32 Z" fill="#CDE6FF"/><circle cx="76" cy="100" r="20" fill="#121212"/><circle cx="76" cy="100" r="7" fill="#fff" stroke="none"/><circle cx="226" cy="100" r="20" fill="#121212"/><circle cx="226" cy="100" r="7" fill="#fff" stroke="none"/></svg></div></div>''', F(4)),
 slide(f'''<div class="tag">À retenir</div><div class="mid" style="gap:60px;margin:auto 0">
<p class="big" style="font-size:60px">La monnaie est partout<br><span class="hl">dans ta journée.</span></p>
<p class="txt" style="font-size:40px">Payer, comparer, garder…<br>et les banques la font circuler.</p>
{nextpost('B','Pourquoi un billet vaut 20 € ?').replace('Partie B/3','Bonus')}</div>''', F(5)),
]

# ---------- BONUS ----------
F = lambda n, t=5: foot('', n, t, bonus=True)
P['bonus'] = [
 cover(0, 'Pourquoi un billet<br>vaut 20 € ?', dark=True).replace('white-space:nowrap">Pourquoi','white-space:normal;text-align:center">Pourquoi'),
 slide(f'''<div class="tag">Imagine…</div><div class="mid" style="gap:44px;margin:auto 0">
<p class="big" style="font-size:60px;margin-bottom:20px">Un billet de 20 €,<br>c'est juste… <span style="{UL}">du papier</span>.</p>
<div style="display:flex;justify-content:center">{billet(360)}</div>
<div class="card"><p class="txt" style="font-size:40px">Il coûte quelques centimes à fabriquer.<br><b>Alors pourquoi tout le monde l'accepte ?</b></p></div></div>''', F(2)),
 slide(f'''<div class="tag">Avant</div><div class="mid" style="gap:36px;margin:auto 0">
<p class="big" style="font-size:56px;margin-bottom:20px">Autrefois, la monnaie<br><span class="hl">valait son poids en métal</span></p>
{row('euro','Des pièces en or ou en argent','leur valeur, c\'était le métal',OP)}
<p class="txt" style="font-size:38px">Aujourd'hui, plus du tout.<br>Alors d'où vient sa valeur ?</p></div>''', F(3)),
 slide(f'''<div class="tag">La réponse : la confiance</div><div class="mid" style="gap:30px;margin:auto 0">
<p class="big" style="font-size:50px;margin-bottom:20px">Tu acceptes un billet de 20 €…<br><span class="hl">parce que tu sais que le boulanger<br>l'acceptera aussi</span></p>
{row('menage','« Fiduciaire » vient du latin fiducia','= confiance',VP)}
{row('etat','La banque centrale','veille à ce que sa valeur reste stable',BP)}</div>''', F(4)),
 slide(f'''<div class="tag">Et sans confiance ?</div><div class="mid" style="gap:28px;margin:auto 0">
<p class="big" style="font-size:54px;margin-bottom:16px">La monnaie <span class="hl">ne vaut plus rien</span></p>
{row('monde','Ex. : le Zimbabwe, en 2008','les prix explosent, les billets ne valent plus rien',RP)}
{row('menage','Les gens refusent la monnaie','ils préfèrent des dollars… ou le troc',OP)}
{quizblock}</div>''', F(5)),
]

