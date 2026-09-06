"""Regression for PDF links reusing a previously cached CV after --sync."""
import contextlib
import importlib.util
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from html.parser import HTMLParser
from urllib.parse import urlsplit

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/build_cv.py'
spec = importlib.util.spec_from_file_location('build_cv', SCRIPT)
build_cv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_cv)


class Links(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.hrefs = []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for key, value in attrs:
                if key == 'href' and urlsplit(value).path.startswith('data/CV_'):
                    self.hrefs.append(value)


class CVLinkCacheTest(unittest.TestCase):
    def test_sync_bypasses_fresh_cache_from_previous_release(self):
        self.check_sync_bypasses_cache('')

    def test_next_sync_bypasses_previously_versioned_cache(self):
        self.check_sync_bypasses_cache('?v=previous-release')

    def check_sync_bypasses_cache(self, suffix):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            data = root / 'data'
            data.mkdir()
            outputs = root / 'output/pdf'
            outputs.mkdir(parents=True)
            homepage = root / 'index.html'
            homepage.write_text(f'<a href="data/CV_en.pdf{suffix}">EN</a><a href="data/CV_zh.pdf{suffix}">ZH</a>')
            expected = {}
            for lang in ['en', 'zh']:
                (data / f'CV_{lang}.pdf').write_bytes(f'previous {lang} PDF bytes'.encode())
                expected[lang] = f'updated {lang} PDF bytes'.encode()
                (outputs / f'CV_{lang}.pdf').write_bytes(expected[lang])
            # A browser may reuse these fresh entries for the origin's max-age=600.
            cache = {href: (root / urlsplit(href).path).read_bytes()
                     for href in Links(homepage.read_text()).hrefs}
            with patch.object(build_cv, 'ROOT', root), \
                 patch.object(build_cv, 'compile_cv', side_effect=lambda engine, lang, out: outputs / f'CV_{lang}.pdf'), \
                 patch.object(build_cv.shutil, 'which', return_value='/test/tectonic'), \
                 patch('sys.argv', ['build_cv.py', '--sync']), contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(build_cv.main(), 0)
            hrefs = Links(homepage.read_text()).hrefs
            self.assertEqual(len(hrefs), 2)
            for href, lang in zip(hrefs, ['en', 'zh']):
                # Follow the updated homepage exactly: no test-added cache buster.
                shown = cache[href] if href in cache else (root / urlsplit(href).path).read_bytes()
                self.assertEqual(shown, expected[lang], f'{lang}: homepage click still displays the cached previous PDF')

            # Repeated refreshes keep stable URLs; changing one PDF versions only it.
            with contextlib.redirect_stdout(io.StringIO()):
                build_cv.refresh_cv_links(root)
                self.assertEqual(Links(homepage.read_text()).hrefs, hrefs)
                (data / 'CV_en.pdf').write_bytes(b'another English revision')
                build_cv.refresh_cv_links(root)
            next_hrefs = Links(homepage.read_text()).hrefs
            self.assertNotEqual(next_hrefs[0], hrefs[0])
            self.assertEqual(next_hrefs[1], hrefs[1])


if __name__ == '__main__':
    unittest.main()
