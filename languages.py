import sys
import googletrans
from pprint import pprint
import argparse
import logging


def def_params():
    parser = argparse.ArgumentParser(
            description=
"""
Script to show possible language to translate in google
EXAMPLE: python languages.py
"""
    )
    parser.add_argument("-l", "--loghami", action="store_true", help="set debug", required=False)
    parser.add_argument("-k", "--keys", action="store_true", help="show only keys of language",required=False)
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
        print("args:", str(args))
    return args


def main():
    args=def_params()
    logging.debug('Only shown in debug mode')
    if args.keys:
        pprint(googletrans.LANGUAGES.keys()) #dzieki pretty-print ladnie drukuje
    else:
        pprint(googletrans.LANGUAGES)

if __name__ == "__main__":
    main()
