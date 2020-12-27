'''Subtitle test cases'''
import unittest

from os.path import join, dirname

from subtitle_filter import Subtitles

DATA_DIR = join(dirname(__file__), 'data')

class SubtitleFilterFontTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_font_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_font_after.srt'))

    def test_subtitle_font(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)

class SubtitleFilterMusicTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_music_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_music_after.srt'))

    def test_subtitle_music(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)

class SubtitleFilterBracketsTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_parenthesis_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_parenthesis_after.srt'))

    def test_subtitle_brackets(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)

class SubtitleFilterItalicsTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_italics_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_italics_after.srt'))

    def test_subtitle_italics(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)

class SubtitleAllTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_example_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_example_after.srt'))

    def test_subtitle_all(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)

class SubtitleFilterNamesTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_names_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_names_after.srt'))

    def test_subtitle_names(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)

class SubtitleFilterSymbolsTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_symbols_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_symbols_after.srt'))

    def test_subtitle_symbols(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)

class SubtitleFilterAuthorTestCase(unittest.TestCase):

    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_author_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_author_after.srt'))

    def test_subtitle_author(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)


class SubtitleFilterCommaTestCase(unittest.TestCase):
    def setUp(self):
        self.subs_before = Subtitles(join(DATA_DIR, 'subtitle_commas_before.srt'))
        self.subs_after = Subtitles(join(DATA_DIR, 'subtitle_commas_after.srt'))

    def test_subtitle_commas(self):
        self.subs_before.filter()
        self.assertEqual(self.subs_before, self.subs_after)