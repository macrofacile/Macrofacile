#!/bin/bash
# Construit la version GitHub Pages du site à partir de /home/claude/site/index.html
set -e
SRC=/home/claude/site/index.html; DST=/home/claude/macrofacile
python3 - "$SRC" "$DST/index.html" <<'PY'
import sys
src=open(sys.argv[1],encoding='utf8').read()
src=src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
head=('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
      '<meta name="description" content="Quiz et lexique gratuits pour comprendre l’économie simplement. Par Macro facile !">\n'
      '<meta property="og:title" content="Macro facile ! · Quiz et lexique">\n'
      '<meta property="og:description" content="Teste-toi sur l’économie : quiz, lexique et séries, expliqués simplement.">\n'
      '<meta name="theme-color" content="#121212">\n')
i=src.index('</style>')+len('</style>')
out=head+src[:i]+'\n</head>\n<body>\n'+src[i:]+'\n</body>\n</html>\n'
open(sys.argv[2],'w',encoding='utf8').write(out)
PY
echo "macrofacile.fr" > "$DST/CNAME"
touch "$DST/.nojekyll"
printf '# Macro facile !\n\nQuiz, lexique et séries pour comprendre l’économie simplement.\n\nSite : https://macrofacile.fr · Instagram : [@macrofacile](https://www.instagram.com/macrofacile/)\n' > "$DST/README.md"
