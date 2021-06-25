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