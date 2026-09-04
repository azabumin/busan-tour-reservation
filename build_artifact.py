# -*- coding: utf-8 -*-
"""
index.html -> dist/busan-artifact.html

Artifact(웹 게시)용 파일을 만듭니다.
게시 시스템이 <!doctype>/<html>/<head>/<body> 를 스스로 씌우므로 그 부분만 벗겨냅니다.
index.html 을 고친 뒤 이 스크립트를 다시 돌리면 게시본도 최신이 됩니다.

    python build_artifact.py
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'index.html')
DST_DIR = os.path.join(HERE, 'dist')
DST = os.path.join(DST_DIR, 'busan-artifact.html')

s = io.open(SRC, encoding='utf-8').read()

# <title> 은 게시본에서 짧은 이름으로
title = '釜山旅行デスク'

style = re.search(r'<style>.*?</style>', s, re.S).group(0)
body = re.search(r'<body>(.*?)</body>', s, re.S).group(1)

out = '<title>' + title + '</title>\n' + style + '\n' + body.strip() + '\n'

if not os.path.isdir(DST_DIR):
    os.makedirs(DST_DIR)
io.open(DST, 'w', encoding='utf-8').write(out)

for tag in ('<!DOCTYPE', '<html', '<head>', '<body>'):
    assert tag not in out, 'wrapper tag left in output: ' + tag
print('built:', DST, len(out), 'chars')
