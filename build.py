# -*- coding: utf-8 -*-
"""Construit le site installable (PWA) à partir de app/popote.html.

Usage : python build.py
Sortie : docs/index.html (+ icônes, manifest et service worker déjà présents dans docs/)
"""
import re, io, zlib, struct, math, os

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "app", "popote.html")
OUT_DIR = os.path.join(ROOT, "docs")
os.makedirs(OUT_DIR, exist_ok=True)

src = open(SRC, encoding="utf-8").read()
title = re.search(r"<title>(.*?)</title>", src).group(1)
body = re.sub(r"^\s*<title>.*?</title>\s*", "", src, count=1, flags=re.S)

HEAD = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="Menu de la semaine, liste de courses et carnet de prix pour la maison.">
<meta name="theme-color" content="#2F6B4F">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="{title}">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon-192.png" type="image/png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>
:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}
[hidden]{{display:none!important}}
img{{max-width:100%}}
</style>
</head>
<body>
"""
FOOT = """
<script>
if('serviceWorker' in navigator){window.addEventListener('load',()=>{navigator.serviceWorker.register('sw.js').catch(()=>{})})}
</script>
</body>
</html>
"""
open(os.path.join(OUT_DIR, "index.html"), "w", encoding="utf-8").write(HEAD + body + FOOT)


# ---- icônes PNG (sans dépendance externe) ----
def png(width, height, pixels):
    raw = b"".join(b"\x00" + bytes(row) for row in pixels)
    def chunk(tag, data):
        c = struct.pack(">I", len(data)) + tag + data
        return c + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", width, height, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))

def icon(size, rounded=True):
    bg = (47, 107, 79); white = (255, 255, 255); soft = (221, 235, 226)
    r = size * 0.22 if rounded else 0
    cx = cy = size / 2
    rows = []
    for y in range(size):
        row = []
        for x in range(size):
            # fond arrondi
            dx = max(abs(x - cx) - (cx - r), 0); dy = max(abs(y - cy) - (cy - r), 0)
            inside = (dx * dx + dy * dy) <= r * r if rounded else True
            if not inside:
                row += [0, 0, 0, 0]; continue
            col = bg
            # assiette : anneau blanc
            d = math.hypot(x - cx, y - cy * 1.04)
            if size * 0.30 <= d <= size * 0.36: col = white
            elif d < size * 0.30: col = soft
            # couverts stylisés : deux barres verticales de part et d'autre
            for bx in (size * 0.14, size * 0.86):
                if abs(x - bx) <= size * 0.025 and size * 0.28 <= y <= size * 0.72: col = white
            row += [col[0], col[1], col[2], 255]
        rows.append(row)
    return png(size, size, rows)

for name, s, rd in (("icon-192.png", 192, True), ("icon-512.png", 512, True), ("apple-touch-icon.png", 180, False)):
    open(os.path.join(OUT_DIR, name), "wb").write(icon(s, rd))

print("docs/index.html et icônes générés")
