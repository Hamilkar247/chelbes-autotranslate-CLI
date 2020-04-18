#!/usr/bin/env python

import sys
import googletrans

def main():
    if len(sys.argv) < 2 :
        print(googletrans.LANGUAGES)
    elif sys.argv[1] == "-k":
        print(googletrans.LANGUAGES.keys())

if __name__ == "__main__":
    main()
