#!/usr/bin/env python3
'''Script to Filter SDH tags from subtitles'''

import argparse

from subtitle_filter.libs.subtitle import Subtitles


def run(args):
    '''Main entry point of script'''
    subs = Subtitles(args.sub_fpath)
    subs.filter(
        rm_fonts=args.rm_fonts,
        rm_ast=args.rm_ast,
        rm_music=args.rm_music,
        rm_effects=args.rm_effects,
        rm_names=args.rm_names,
        rm_author=args.rm_author,
    )

    if args.print:
        subs.print()
        return

    subs.save(new_filepath=args.out_fpath)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(
        description='Filter subtitles to remove various SDH (Deaf or Hard-of-Hearing) tags.'
    )

    ap.add_argument(
        '-s',
        '--subtitle',
        dest='sub_fpath',
        type=str,
        help='Subtitle file to filter',
        required=True,
    )
    ap.add_argument(
        '-o',
        '--output',
        dest='out_fpath',
        type=str,
        help='Path to save filtered subtitle, omit to save inplace',
        default=None,
    )
    ap.add_argument(
        '-p',
        '--print-only',
        dest='print',
        action='store_true',
        default=False,
        help='Print output subtitles instead of saving to disk.',
    )
    ap.add_argument(
        '--keep-fonts',
        dest='rm_fonts',
        default=True,
        action='store_false',
        help='Do not remove font tags from subtitles.',
    )
    ap.add_argument(
        '--keep-ast',
        dest='rm_ast',
        default=True,
        action='store_false',
        help='Do not remove subtitles containing asterisks: (*).',
    )
    ap.add_argument(
        '--keep-music',
        dest='rm_music',
        default=True,
        action='store_false',
        help='Do not remove "♪" symbols and text contained within two "♪" symbols.',
    )
    ap.add_argument(
        '--keep-effects',
        dest='rm_effects',
        default=True,
        action='store_false',
        help='Do not remove text between and including parenthesis () or brackets []',
    )
    ap.add_argument(
        '--keep-names',
        dest='rm_names',
        default=True,
        action='store_false',
        help='Do not replace names in CAPITALS with "-" tags',
    )
    ap.add_argument(
        '--keep-author',
        dest='rm_author',
        default=True,
        action='store_false',
        help='Do not remove author tags, eg. Subtitles by some guy.',
    )

    arguments = ap.parse_args()

    run(arguments)
