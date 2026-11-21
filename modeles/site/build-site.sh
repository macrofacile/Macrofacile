#!/bin/bash
# Construit la version GitHub Pages du site à partir de /home/claude/site/index.html
set -e
SRC=/home/claude/site/index.html; DST=${DST:-/home/claude/macrofacile}
python3 - "$SRC" "$DST/index.html" <<'PY'
import sys
src=open(sys.argv[1],encoding='utf8').read()
src=src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
head=('<!doctype html>\n<html lang="fr">\n<head>\n<meta charset="utf-8">\n'
      '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
      '<meta name="description" content="Quiz et lexique gratuits pour comprendre l’économie simplement. Par Macro facile !">\n'
      '<meta property="og:title" content="Macro facile ! L’économie, sans prise de tête">\n'
      '<meta property="og:description" content="Teste-toi sur l’économie : quiz, lexique et séries, expliqués simplement.">\n'
      '<meta property="og:type" content="website">\n'
      '<meta property="og:url" content="https://macrofacile.fr/">\n'
      '<meta property="og:image" content="https://macrofacile.fr/og-image.png">\n'
      '<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="630">\n'
      '<meta name="twitter:card" content="summary_large_image">\n'
      '<link rel="icon" href="/favicon.ico" sizes="any">\n'
      '<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">\n'
      '<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n'
      '<meta name="theme-color" content="#121212">\n')
i=src.index('</style>')+len('</style>')
out=head+src[:i]+'\n</head>\n<body>\n'+src[i:]+'\n</body>\n</html>\n'
open(sys.argv[2],'w',encoding='utf8').write(out)
PY
echo "macrofacile.fr" > "$DST/CNAME"
touch "$DST/.nojekyll"
printf '# Macro facile !\n\nQuiz, lexique et séries pour comprendre l’économie simplement.\n\nSite : https://macrofacile.fr · Instagram : [@macrofacile](https://www.instagram.com/macrofacile/)\n' > "$DST/README.md"
