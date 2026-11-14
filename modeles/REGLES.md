# Macro facile ! · Règles du projet

Fiche de référence pour continuer le projet dans une nouvelle conversation.
À relire avant chaque nouveau thème.

## Le projet

- Compte Instagram + page Facebook **Macro facile !** (@macrofacile) : l'économie expliquée simplement, pour des gens qui découvrent.
- Site : **macrofacile.fr** (GitHub Pages, dépôt `macrofacile/Macrofacile`, domaine OVH). Onglets : Accueil, Quiz, Séries, Lexique, Question ?
- Téo écrit d'abord ses notes de cours (chapitre), puis on transforme en posts, quiz, lexique et reel.
- Thèmes publiés : **LE PIB** (bleu `#BFDFFF`, 5 parties + bonus « Réel et nominal ») · **LA DEMANDE** (pistache `#DDF5B5`, 4 parties + bonus « Le paradoxe de l'épargne »).

## Façon de travailler avec Téo

- Français, ton familier. Points avec flèches →, exemples concrets, **pas d'équations**.
- Toujours un **petit point avant un gros changement** (« dis-moi si tu es d'accord »).
- Montrer **toutes les slides d'un post d'un coup**, puis corriger slide par slide.
- Vérifier que chaque info est **vraie partout** (pas seulement en France) ou dire clairement « en France ».
- Penser au **débutant** : si une notion n'a pas été expliquée avant, elle ne va pas dans un quiz ou une slide.
- « Remonte le texte » = **plus d'espace entre le titre et le bloc en dessous** (pas déplacer tout le contenu).
- **À la fin de chaque thème : tout sauvegarder sur GitHub** (slides, modèles, règles mises à jour).

## Structure d'un thème

- **4 parties + bonus** en général (2 à 6 parties possibles). La dernière partie peut être le **récap** (« Partie 4/4 · Le récap »).
- **4 à 5 slides par post max** (lisibilité, motivation).
- **Un seul nom de thème** sur toutes les couvertures (ex. « LA DEMANDE »), comme « LE PIB ».
- Dernière slide de chaque partie : bloc noir **« Prochain post · Partie n/4 → titre »**.
- Dernière slide du récap → bloc « Prochain post · Bonus ». Dernière slide du bonus → bloc « Teste-toi · quiz gratuit macrofacile.fr ».
- Le récap ne doit **pas copier** la mise en page des posts : autre présentation (grille de cartes, tableau…).

## Style des slides (1080×1350, police Fredoka)

- Fond = **couleur pâle du thème**. Chaque thème a sa couleur.
- Logo Macro facile en haut à gauche (couverture), petit logo en bas à gauche (slides de contenu).
- **Couverture** : carte blanche centrée avec le nom du thème en MAJUSCULES (rester dans la zone visible de la grille Insta 3:4, donc pas trop large), pastille **jaune `#FFD166` bien arrondie « Partie n/4 »** (texte noir), pastille **corail `#FF6B6B` texte blanc** avec le sous-titre, petite main « swipe » en bas à droite.
- **Bonus** : couverture **noire**, carte du thème dans la couleur du thème, sticker jaune « BONUS », pastille corail. Les autres slides du bonus restent dans la couleur du thème, avec la pastille noire **« BONUS n/5 »** en bas à droite.
- Slides de contenu : étiquette blanche penchée en haut à gauche (titre), pastille noire en bas à droite « PARTIE n  x/5 » (mot PARTIE en jaune).
- Texte **noir** (jamais gris). Surligneur **jaune Macro `#FFD166`**. Soulignement = jaune Macro épais.
- Blocs pâles avec texte noir : vert `#BDEFC9`, violet `#DCD3FF`, bleu `#CDE6FF`, orange `#FFE0B8`, rouge `#FFC9C9`. Contour/ombre noire.
- **Un exemple concret simple sur chaque slide** (ex. : baguette, four de la boulangerie, vélos, Airbus, Léa et ses 200 € d'épargne).
- Rappeler de temps en temps le **mot clé du thème** (« la demande augmente »), sans en mettre partout.
- Flèches : → pour « ça entraîne » ; pour une **baisse**, pastille avec rond rouge et flèche ↓ (ne pas mélanger les deux).
- **Petites illustrations de temps en temps** (1 ou 2 par post max) dans le même style : contour noir, couleurs pastel (ex. pot « ÉPARGNE » plein / presque vide). Téo n'a pas aimé le cochon-tirelire.
- Bien remplir la slide (pas de grand vide en bas), aérer entre le titre et les blocs.
- **Pas d'emoji** sur le site. (Dans les légendes Insta, oui.)

## Légendes Insta

- Titre « LE THÈME · Partie n/4 », 2-3 lignes d'accroche, flèches →, « Swipe… 👉 », « Quiz et lexique gratuits sur macrofacile.fr ».
- Hashtags adaptés au thème (pas #PIB si ce n'est plus le PIB) : #économie #macroéconomie #apprendre #finance + 1 mot du thème.

## Publication

- Publier depuis **l'appli Instagram sur téléphone** avec « Also share on… Macro Facile » coché → part aussi sur Facebook. Depuis instagram.com sur PC, ça ne part **pas** sur Facebook.
- Une **musique** sur un carrousel peut bloquer le partage vers Facebook.
- Programmer : Facebook → page → **Planificateur** (cocher Facebook + Instagram). L'appli Insta de Téo n'a pas l'option.
- Heure : **9h en France = 19h à Sydney** (même jour) en hiver ; le décalage change fin mars.

## Site (macrofacile.fr)

- Source : `modeles/site/source-index.html` → construit avec `modeles/site/build-site.sh` → `index.html` à la racine.
- À chaque thème : ajouter les **nouveaux mots au lexique** (Téo valide la liste, il peut en retirer), un **quiz de 10 questions** (simples, vraies partout, pas de notion non expliquée, pas de doublon), la **série** dans l'onglet Séries, et mettre le quiz en avant sur l'accueil (carte « Nouveau » dans la couleur du thème).
- Titre du quiz La Demande : « La DEMANDE ».
- Pas d'annonce « Bientôt… » si ce n'est pas prévu.
- Le site met jusqu'à 10 min à se mettre à jour (⌘ + Maj + R).

## Reel

- Voir `modeles/reel/LISEZMOI.md`. Même modèle à chaque thème : titre du thème au centre, prof qui dépasse en bas avec sa bulle, **même temps pour chaque slide** (~4,5 s), musique douce sans voix.
