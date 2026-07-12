'''I/O test cases'''
import copy
import unittest
import tempfile

from os.path import join, dirname

from subtitle_filter import Subtitles

DATA_DIR = join(dirname(__file__), 'data')

class SubtitleFilterFontTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_music_before.srt'))

    def test_subtitle_save(self):
        subs = copy.deepcopy(self.subs_before)
        subs.filter(rm_music=False)
        with tempfile.TemporaryDirectory() as dirpath:
            fpath = join(dirpath, 'test.srt')
            subs.save(fpath)
            subs_after = Subtitles(fpath)
        self.assertEqual(self.subs_before, subs_after)


class SubtitleLegacyEncodingTestCase(unittest.TestCase):

    CONTENTS = '1\n00:00:01,000 --> 00:00:02,000\nCafé naïve résumé\n'

    def test_latin1_read_and_convert(self):
        with tempfile.TemporaryDirectory() as dirpath:
            # Legacy subtitle encoded as ISO-8859-1 / cp1252, not utf-8
            legacy_fpath = join(dirpath, 'legacy.srt')
            with open(legacy_fpath, 'w', encoding='cp1252') as fp:
                fp.write(self.CONTENTS)

            # Reading should not raise UnicodeDecodeError
            subs = Subtitles(legacy_fpath)
            self.assertEqual(subs.subtitles[0].contents, 'Café naïve résumé')

            # Saving re-emits the file as utf-8
            out_fpath = join(dirpath, 'out.srt')
            subs.save(out_fpath)
            with open(out_fpath, 'r', encoding='utf-8') as fp:
                self.assertIn('Café naïve résumé', fp.read())