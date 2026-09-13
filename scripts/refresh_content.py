"""Render localized subpages from site_content.json; preserve shared head/nav/footer.

Run from the repository root. Release states are editorial facts: verify ASC
before updating them; never infer release from a version number in source code.
"""
from pathlib import Path
from html import escape as e
import json
import re

CONTENT = json.loads(Path('scripts/site_content.json').read_text())


def paragraph(text):
    return f'<p>{e(text)}</p>'


def bullets(items):
    return '<ul>' + ''.join(f'<li>{e(t)}</li>' for t in items) + '</ul>'


def status(c):
    return f'<aside class="release-note"><strong>{e(c["checked"])}</strong>{paragraph(c["status"])}<a href="releases.html">{e(c["releaseLink"])} →</a></aside>'


def write_page(path, content, description):
    old = path.read_text()
    head = old.split('</head>', 1)[0] + '</head>'
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m[1] + e(description, quote=True), head)
    nav = re.search(r'<nav class="navbar">.*?</nav>', old, re.S)[0]
    footer = re.search(r'<footer>.*?</footer>', old, re.S)[0]
    prefix = '' if path.parent == Path('docs') else '../'
    path.write_text(head + '\n<body class="site-theme">\n' + nav + '\n<main>\n' + content + '\n</main>\n' + footer + f'\n<script src="{prefix}lang-switcher.js"></script>\n</body>\n</html>\n')


for locale, c in CONTENT.items():
    base = Path('docs') / ('' if locale == 'en' else locale)
    prefix = '' if locale == 'en' else '../'
    media = prefix + 'media/1.2/'
    release = f'<section class="releases"><div class="container"><div class="section-header"><h1>{e(c["releases"])}</h1>{paragraph(c["history"])}</div>'
    release += f'<p class="fineprint">{e(c["checked"])}</p>{paragraph(c["status"])}'
    for version, title, body in [('1.2.0', c['pending'], bullets(c['new'])), ('1.1.0', c['available'], bullets(c['old'])), ('1.0', '1.0 · 2026-02-11', paragraph(c['initial']))]:
        release += f'<article class="release-entry" id="v{version}"><div class="release-header"><h2 class="release-version">{e(title)}</h2></div>{body}</article>'
    release += f'<a class="primary" href="https://apps.apple.com/app/id6758996914">{e(c["store"])} ↗</a></div></section>'
    write_page(base / 'releases.html', release, c['history'] + '. ' + c['status'])

    features = f'<section class="features-detail"><div class="container"><div class="section-header"><h1>{e(c["features"])}</h1>{paragraph(c["featureIntro"])}</div>{status(c)}'
    images = [media + locale + '-poster.jpg', media + locale + '-app-compare.jpg', prefix + f'screenshots/feature-richtext-{locale}.jpg', prefix + f'screenshots/feature-select-{locale}.jpg', prefix + f'screenshots/feature-edit-{locale}.jpg', prefix + f'screenshots/feature-export-1-{locale}.jpg']
    for i, ((title, body), src) in enumerate(zip(c['cards'], images)):
        caption = c['current'] if i < 2 else c['legacy']
        features += f'<article class="feature-detail-item"><div class="feature-detail-text"><span class="feature-number">{i+1:02}</span><h2>{e(title)}</h2>{paragraph(body)}</div><figure><a class="feature-detail-visual" href="{src}"><img src="{src}" alt="{e(title)}" loading="lazy"></a><figcaption class="fineprint">{e(caption)}</figcaption></figure></article>'
    features += '</div></section>'
    features += f'<section class="proof-section" id="text-edit-example"><div class="container"><h2>{e(c["proof"])}</h2>{paragraph(c["proofIntro"])}<div class="content-proof">'
    for suffix, label in [('input', c['before']), ('edited', c['after'])]:
        src = media + locale + '-' + suffix + '.jpg'
        features += f'<figure><a href="{src}"><img src="{src}" alt="{e(label)}" width="1440" height="810" loading="lazy"></a><figcaption>{e(label)}</figcaption></figure>'
    features += f'</div><p class="fineprint">{e(c["proofNote"])}</p><p><a href="index.html#demo">{e(c["demo"])} →</a></p></div></section>'
    write_page(base / 'features.html', features, c['featureIntro'])

    support = f'<section class="page"><div class="container"><div class="page-card"><h1>{e(c["support"])}</h1>{status(c)}<h2>{e(c["requirements"])}</h2>{bullets(c["req"])}<h2>{e(c["faq"])}</h2><div class="faq-list">'
    for question, answer in c['qa']:
        support += f'<details class="faq-item"><summary>{e(question)}</summary>{paragraph(answer)}</details>'
    support += f'</div><h2>{e(c["contact"])}</h2>{paragraph(c["contactBody"])}<p><a href="https://github.com/puritysb/SlideTouch-support/issues">GitHub Issues ↗</a> · <a href="mailto:puritysb@gmail.com">puritysb@gmail.com</a></p>{paragraph(c["privacyIntro"])}<p><a href="privacy.html">'+({'en':'Privacy policy','ko':'개인정보 처리방침','ja':'プライバシーポリシー'}[locale])+'</a></p></div></div></section>'
    write_page(base / 'support.html', support, c['contactBody'])

    path = base / 'privacy.html'
    old = path.read_text()
    section = re.search(r'<section class="page">.*?</section>', old, re.S)[0]
    section = re.sub(r'<p data-support-privacy>.*?</p>', '', section, flags=re.S)
    section = re.sub(r'</div>\s*</div>\s*</section>', lambda m: f'<p data-support-privacy>{e(c["supportPrivacy"])}</p></div></div></section>', section)
    # Existing privacy pages use a compact section; require the insertion to succeed.
    assert 'data-support-privacy' in section, path
    write_page(path, section, c['privacyMeta'])
