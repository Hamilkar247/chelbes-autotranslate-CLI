#!/usr/bin/env python

import googletrans
import os
import sys

def translateChelbes(translator: googletrans.Translator, only_text: str, lang_from: str, lang_to: str) -> str:
    resultOfTrans = translator.translate(only_text, src=lang_from, dest=lang_to)
    return resultOfTrans.text

def main():
    #print('Number of arguments:', len(sys.argv), ' arguments.')
    #print(googletrans.LANGUAGES.keys())
    sentence = sys.argv[3:]
    lang_from = sys.argv[1]
    lang_to = sys.argv[2]
    result=" ".join(sentence)
    translator = googletrans.Translator()
    translate_text = translateChelbes(translator, result, lang_from, lang_to)
    print(translate_text)

if __name__ == "__main__":
    main()


