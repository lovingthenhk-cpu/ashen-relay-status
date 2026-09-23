#!/usr/bin/env python3
"""Render the public plan pages from local Markdown sources."""
from pathlib import Path
from html import escape
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parent
PAGES = [
    ("index.html", "概要"),
    ("world.html", "世界と攻略先"),
    ("gameplay.html", "プレイループ"),
    ("mods.html", "Mod採用表"),
    ("ideas.html", "旧案の採用台帳"),
    ("delivery.html", "次の作業と実装受入"),
    ("implementation.html", "実装ファイル"),
    ("completion.html", "完成工程"),
]

def nav_for(filename):
    return '<nav class="site-nav" aria-label="サイト内のページ">' + ''.join(
        f'<a href="{page}"' + (' aria-current="page"' if page == filename else '') + f'>{escape(label)}</a>'
        for page, label in PAGES
    ) + '</nav>'


md = MarkdownIt('commonmark').enable('table')
for filename, label in PAGES[1:]:
    body = md.render((ROOT / filename.replace('.html', '.md')).read_text())
    html = f'''<!doctype html>
<html lang="ja">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow, noarchive">
  <meta name="description" content="Ashen Relayの{escape(label)}。実装済み・計画・受入条件を区別して掲載。">
  <title>{escape(label)} — Ashen Relay</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    {nav_for(filename)}
    <header class="subpage-header"><p class="eyebrow">ASHEN RELAY · 公開計画</p><p class="subpage-lead">全工程は <a href="completion.html">完成工程</a>、元の原要求は <a href="gameplay.html">プレイループ</a> に掲載。</p></header>
    <article class="document">{body}</article>
    <footer><a href="index.html">概要へ戻る</a> · 更新日 2026-09-23 · 物語の核心は掲載しません。</footer>
  </main>
</body>
</html>
'''
    (ROOT / filename).write_text(html)
