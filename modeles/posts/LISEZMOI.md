# Modèle des posts (carrousels 1080×1350)

`gen.py` contient le style commun (CSS, icônes, blocs, couverture, pastilles, bloc « Prochain post », pot « ÉPARGNE »)
et le contenu du thème LA DEMANDE comme exemple. Pour un nouveau thème : garder le haut du fichier, remplacer les listes `P['p1']`… `P['bonus']`.

- `python3 gen.py '#DDF5B5' slides` → une page HTML par slide (2e argument = dossier de sortie, 1er = couleur du thème)
- `node shot.js slides` → PNG de chaque slide (+ alerte si un élément dépasse)
- `python3 sheet.py slides` → planches de 5 slides pour tout montrer d'un coup

Les slides finales de chaque thème sont dans `archives/`. Règles de style : `modeles/REGLES.md`.
