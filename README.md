# subtitle-filter
[![Build Status](https://travis-ci.com/mattlyon93/filter-subs.svg?branch=master)](https://travis-ci.com/mattlyon93/filter-subs) [![Coverage Status](https://coveralls.io/repos/github/mattlyon93/filter-subs/badge.svg?branch=master)](https://coveralls.io/github/mattlyon93/filter-subs?branch=master) [![PyPI version](https://badge.fury.io/py/subtitle-filter.svg)](https://badge.fury.io/py/subtitle-filter)

Filter `.srt` subtitle files to remove SDH (Deaf or Hard-of-Hearing) entries and other tags.

## Installation
```
pip install subtitle-filter
```

## Usage
`subtitle-filter` can be used either as a script or a module.

By default, this module filters the following (in order):

1. Removes font tags and text contained within, e.g. `<font color="#DF01D7">Hey\</font>` is removed.
2. Removes subtitle entries containing asterisks: `*`.
3. Removes subtitle lines containing `♪`.
4. Removes sound effects: text contained with and including parenthesis `(BANG)` and brackets `[boom]`.
5. Replaces names with dashes, e.g. `GARY: Hey` or `Gary: Hey` to `- Hey`.
6. Removes author tags e.g. `XoXo Subtitles by PwnedDude967 XoXo`.
7. Removes lone `?` and `-` symbols.

### Script Usage
Bring up the help display:
```bash
filter-subtitles.py -h
```

Filter a subtitle in place (overwrites original subtitle) with default options.
```bash
filter-subtitles.py -s /path/to/sub.srt
```

Instead of saving to disk, print the output.
```bash
filter-subtitles.py -s /path/to/sub.srt -p
```

Save the output to a different filepath.
```bash
filter-subtitles.py -s /path/to/sub.srt -o /path/to/outsub.srt
```

Custom filter flags.
```
--keep-fonts          Do not remove font tags and text contained within.
--keep-ast            Do not remove subtitles containing asterisks: (*).
--keep-music          Do not lines containing 1 or more "♪" symbols.
--keep-effects        Do not remove text between and including parenthesis
                        () or brackets []
--keep-names          Do not replace names in CAPITALS with "-" tags
--keep-author         Do not remove author tags, eg. Subtitles by some guy.
```

### Module Usage
Filter a subtitle in place (overwrites original subtitle) with default options
```python
from subtitle_filter import Subtitles

subs = Subtitles('/path/to/sub.srt')
subs.filter()
subs.save()
```
Instead of saving to disk, print the output.
```python
subs.print()
```
Save the output to a different filepath.
```python
subs.save('/path/to/newsub.srt')
```

Use custom filter flags.
```python
subs.filter(
    rm_fonts=True,
    rm_ast=False,
    rm_music=True,
    rm_effects=True,
    rm_names=False,
    rm_author=False,
)
```
