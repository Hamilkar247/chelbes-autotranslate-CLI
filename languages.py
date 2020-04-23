#!/usr/bin/env python

import sys
import googletrans
from pprint import pprint
import argparse

def main():
    if len(sys.argv) < 2 :
        pprint(googletrans.LANGUAGES) #dzieki pretty-print ladnie drukuje
    elif sys.argv[1] == "-k":
        pprint(googletrans.LANGUAGES.keys())

if __name__ == "__main__":
    main()
