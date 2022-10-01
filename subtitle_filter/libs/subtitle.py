'''Module containing Subtitle and Subtitles classes'''
import os
import re
import codecs

AUTHOR_STRINGS = (
    'synced and corrected by',
    'sync and corrections by',
    'subtitles by',
    'encoded and released by',
    'opensubtitles.org',
    'please rate this subtitle',
    'captioning sponsored by',
    'captioned by',
)


class Subtitle:
    '''Subtitle contents object
        (invidual subtitle entry)
    '''

    def __init__(self):
        self._index = None
        self._contents = ''
        self.start = None
        self.end = None

    def __str__(self):
        return '{}\n{} --> {}\n{}\n'.format(
            self._index, self.start, self.end, self._contents
        )

    def __eq__(self, other):
        if self.__str__() == other.__str__():
            return True
        return False

    def _contents_to_list(self):
        if isinstance(self._contents, str):
            self._contents = self._contents.split('\n')

    def _contents_to_str(self):
        if isinstance(self._contents, list):
            self._contents = '\n'.join(self._contents)

    @property
    def index(self):
        '''Returns the index number for subtitle, or False if index is not assigned'''
        if self._index is None:
            return False
        return self._index

    @index.setter
    def index(self, index):
        self._index = int(index)

    @property
    def contents(self):
        '''Returns the contents lines for the subtitle'''
        return self._contents

    @contents.setter
    def contents(self, item):
        if self._contents:
            self._contents += '\n{}'.format(item)
        else:
            self._contents = '{}'.format(item)

    def _filter_empty(self):
        '''Removes empty quotes from contents list,
            Converts self.index to 0
        '''
        # Set index as 0 for later deletion
        if not self.contents:
            self.index = 0

    @property
    def lines(self):
        '''Subtitle entry as a newline separated list'''
        return [
            str(self._index),
            '{} --> {}'.format(self.start, self.end),
            *self._contents.split('\n'),
        ]

    @staticmethod
    def _remove_comma_space(matchobj):
        return matchobj.group(0).replace(' ,', ',')

    @staticmethod
    def _add_comma_space(matchobj):
        return matchobj.group(0).replace(',', ', ')

    def fix_comma_spaces(self):
        '''Fixes comma space seperation'''
        for _ in re.findall(r'[A-Za-z]+\s+,', self._contents):
            self._contents = re.sub(
                r'[A-Za-z]+\s+,', self._remove_comma_space, self._contents
            )
        for _ in re.findall(r'[A-Za-z]+,[A-Za-z]+', self._contents):
            self._contents = re.sub(
                r'[A-Za-z]+,[A-Za-z]+', self._add_comma_space, self._contents
            )

    def remove_font_colours(self):
        '''Removes <font> tags from contents'''
        self._contents = re.sub(
            r'\<font(.*)\>(.*)\</font\>', '', self._contents, flags=re.DOTALL
        )
        self._filter_empty()

    def remove_asterisks(self):
        '''Removes lines if there is an asterisk lurking about'''
        if '*' in self._contents:
            self.index = 0

    def remove_music(self):
        '''Removes music symbols from contents'''
        # Remove music symbol behaving as parenthesis
        self._contents = re.sub(r'♪(.*)♪', '', self._contents, flags=re.DOTALL)
        # Remove behaving as inline
        self._contents_to_list()
        for idx, _ in enumerate(self._contents):
            if any(symbol in self._contents[idx] for symbol in ['#', '♪']):
                self._contents[idx] = ''
        self._contents_to_str()
        self._filter_empty()

    def remove_sound_effects(self):
        '''Removes text in between parenthesis and square brackets'''
        # Remove single line brackets
        self._contents_to_list()
        for idx, _ in enumerate(self._contents):
            self._contents[idx] = re.sub(
                r'[\(\[][\S ]*[\)\]][\s:]*', '', self._contents[idx]
            )
        self._remove_lone_symbols()
        self._contents_to_str()
        # Remove multi-line brackets
        self._contents = re.sub(r'[\(\[][\S\s]*[\)\]][\s:]*', '', self._contents)
        self._filter_empty()

    def replace_names(self):
        '''Replace names in all caps'''
        # Care is taken here to preserve genuine sentences with a colon.
        names = re.findall(r'([A-Z0-9 ]+ *: *|[A-Z]{1}[a-z]+ *: *)', self._contents)
        if len(names) > 1:
            # Replace names with '- '
            self._contents = re.sub(
                r'([A-Z0-9 ]+ *: *|[A-Z]{1}[a-z]+ *: *)', '- ', self._contents
            ).lstrip()
        else:
            # Replace name with empty string.
            self._contents = re.sub(
                r'([A-Z0-9 ]+ *: *|[A-Z]{1}[a-z]+ *: *)', '', self._contents
            ).lstrip()
        self._filter_empty()

    def remove_author(self):
        '''Removes "Subtitles by" subtitle entries etc'''
        for author_str in AUTHOR_STRINGS:
            if author_str in self._contents.lower():
                self.index = 0
                break

    def fix_italics(self):
        '''Fixes lone <i> or </i> tags, and removes empty <i> tags, and empty dashes'''
        if '<i>' in self._contents and '</i>' not in self._contents:
            self._contents += '</i>'
        if '</i>' in self._contents and '<i>' not in self._contents:
            self._contents = '<i>' + self._contents
        self._contents = re.sub(
            r'<i>[\_\-\‐\?#\s¶]*</i>', '', self._contents, flags=re.DOTALL
        )
        self._remove_lone_symbols()

    def _remove_lone_symbols(self):
        self._contents_to_list()
        for idx, _ in enumerate(self._contents):
            self._contents[idx] = re.sub(r'^[\_\-\‐\?#\s¶]*$', '', self._contents[idx])
            self._contents[idx] = re.sub(
                r'^[\_\-\‐\?#\s¶]*<i>[\_\-\‐\?#\s¶]*$', '<i>', self._contents[idx]
            )
            self._contents[idx] = re.sub(
                r'^[\_\-\‐\?#\s¶]*</i>[\_\-\‐\?#\s¶]*$', '</i>', self._contents[idx]
            )
        # Removes empty strings
        self._contents = list(filter(None, self._contents))
        # Set index as 0 for later deletion
        if len(self.contents) == 0:
            self.index = 0
        self._contents_to_str()


class Subtitles:
    '''Content filtering object for subtitles file'''

    EXTENSIONS = ['.srt']

    def __init__(self, fpath):
        if not os.path.exists(fpath):
            raise IOError('{} does not exist'.format(fpath))
        if not os.path.isfile(fpath):
            raise IOError('{} is not a file'.format(fpath))
        self._fullpath = fpath
        if self.ext not in self.EXTENSIONS:
            raise IOError(
                '{} is not valid subtitle file: {}'.format(self._fullpath, self.ext)
            )
        self._line_list = self._get_line_list()
        self.subtitles = self._parse_subs()

    def __eq__(self, other):
        if len(self.subtitles) != len(other.subtitles):
            return False
        for idx, _ in enumerate(self.subtitles):
            if self.subtitles[idx] != other.subtitles[idx]:
                return False
        return True

    @property
    def filepath(self):
        '''Filepath of mediafile'''
        return self._fullpath

    @property
    def ext(self):
        '''Extension of mediafile'''
        _, ext = os.path.splitext(self._fullpath)
        return ext

    def _get_line_list(self):
        with codecs.open(
            self.filepath, 'r', encoding='utf-8-sig', errors='ignore'
        ) as fdata:
            line_list = fdata.readlines()
        line_list_filtered = [x.rstrip() for x in line_list]
        return line_list_filtered

    def _parse_subs(self):
        sub_list = [Subtitle()]
        for line in self._line_list:
            # If the index has not yet been created in latest sublist item
            if not sub_list[-1].index:
                try:
                    sub_list[-1].index = int(line)
                except ValueError:
                    continue
            # Time line
            elif sub_list[-1].start is None:
                if ' --> ' in line:
                    sub_list[-1].start, sub_list[-1].end = line.split(' --> ')
                else:
                    continue
            # New subtitle entry
            elif not line:
                sub_list.append(Subtitle())
            # Contents
            else:
                sub_list[-1].contents = line
        return sub_list

    def filter(self, **kw):
        '''Filters subtitles to remove SDH items'''
        # Filter contents
        if kw.get('rm_fonts', True):
            any(map(lambda sub: sub.remove_font_colours(), self.subtitles))
        if kw.get('rm_ast', True):
            any(map(lambda sub: sub.remove_asterisks(), self.subtitles))
        if kw.get('rm_music', True):
            any(map(lambda sub: sub.remove_music(), self.subtitles))
        if kw.get('rm_effects', True):
            any(map(lambda sub: sub.remove_sound_effects(), self.subtitles))
        if kw.get('rm_names', True):
            any(map(lambda sub: sub.replace_names(), self.subtitles))
        if kw.get('rm_author', True):
            any(map(lambda sub: sub.remove_author(), self.subtitles))
        if kw.get('fix_commas', True):
            any(map(lambda sub: sub.fix_comma_spaces(), self.subtitles))
        any(map(lambda sub: sub.fix_italics(), self.subtitles))
        # Remove filtered items from list
        self.subtitles[:] = [sub for sub in self.subtitles if sub.index]
        # Reassign indices
        for idx, sub in enumerate(self.subtitles):
            sub.index = idx + 1

    def print(self):
        '''Prints all subtitle entries'''
        for sub in self.subtitles:
            print(sub)

    def save(self, new_filepath=None):
        '''Saves subtitle object to disk,
        omit new_filepath to save inplace
        '''
        if new_filepath is not None:
            self._fullpath = new_filepath
        with open(self._fullpath, 'w', encoding='utf-8') as fp:
            for sub in self.subtitles:
                fp.write(str(sub) + '\n')
