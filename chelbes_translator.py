import googletrans
import os
import sys
import argparse
import logging


def def_params():
    parser = argparse.ArgumentParser(
            description=
"""
Script to translate sentence with google
EXAMPLE: python chelbes_translator -f pl -to eng -s \"polska dla polaków\" -l
"""
    )
    #action="store_true" sprawia że potem już nie musze podawać liczby/stringa do tego argumentu
    parser.add_argument("-l", "--loghami", action="store_true", help="set debug", required=False)
    parser.add_argument("-f", "--fromlang", help="source language sentence", required=True)
    parser.add_argument("-t", "--tolang", help="destination language sentence", required=True)
    parser.add_argument("-s", "--sentence", help="sentence to translate", required=True)
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
        print("args:" + str(args))
    return args


def translateChelbes(translator, sentence, lang_from, lang_to):
    resultOfTrans = translator.translate(sentence, src=lang_from, dest=lang_to)
    return resultOfTrans.text


def main():
    args=def_params()
    logging.debug('Only shown in debug mode')
    logging.debug("args.sentence: "+args.sentence)
    logging.debug("args.fromlang: "+args.fromlang)
    sentence = args.sentence
    lang_from = args.fromlang
    lang_to = args.tolang
    translator = googletrans.Translator()
    translate_text = translateChelbes(translator, sentence, lang_from, lang_to)
    print(translate_text)


if __name__ == "__main__":
    main()

