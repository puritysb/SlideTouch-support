"""Check published-page structure, local links and release-copy synchronization."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
import json

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path, self.ids, self.links, self.text = path, set(), [], []
        self.headings = self.mains = self.themes = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, (self.path, 'duplicate ID', a['id'])
            self.ids.add(a['id'])
        self.headings += tag == 'h1'
        self.mains += tag == 'main'
        self.themes += tag == 'body' and 'site-theme' in a.get('class', '').split()
        for attr in ('href', 'src', 'poster'):
            u = urlparse(a.get(attr, ''))
            if u.scheme or u.netloc or not u.path:
                continue
            target = Path('docs') / unquote(u.path.removeprefix('/SlideTouch-support/')) if u.path.startswith('/SlideTouch-support/') else self.path.parent / unquote(u.path)
            assert target.exists(), (self.path, 'missing path', target)
            if u.fragment:
                self.links.append((target / 'index.html' if target.is_dir() else target, unquote(u.fragment)))
    def handle_data(self, data):
        self.text.append(data)

content = json.loads(Path('scripts/site_content.json').read_text())
count = 0
for locale, copy in content.items():
    base = Path('docs') / ('' if locale == 'en' else locale)
    for name in ('index', 'features', 'releases', 'support', 'privacy'):
        p = base / (name + '.html')
        page = Page(p)
        page.feed(p.read_text())
        assert page.headings == page.mains == page.themes == 1, p
        if name != 'privacy':
            assert copy['status'] in ''.join(page.text), (p, 'release status drift')
        if name == 'releases':
            assert {'v1.2.0', 'v1.1.0', 'v1.0'} <= page.ids, p
        for target, fragment in page.links:
            linked = Page(target)
            linked.feed(target.read_text())
            assert fragment in linked.ids, (p, target, fragment)
        count += 1
print(f'PASS: {count} pages; release state, structure, IDs and local links')
