import pytest
import googletrans
from chelbes_translator import translateChelbes


def test_translateChelbesOneWordPLENG():
    sentence="Polska"
    translator = googletrans.Translator()
    lang_from = 'pl'
    lang_to = 'en'
    result = translateChelbes(translator, sentence, lang_from, lang_to)
    assert result.lower() == "poland"


def test_translateChelbesOneWordENGPL():
    sentence="England"
    translator = googletrans.Translator()
    lang_from = 'en'
    lang_to = 'pl'
    result = translateChelbes(translator, sentence, lang_from, lang_to)
    assert result.lower() == "anglia"


def test_translateChelbesSentencePLENG():
    sentence="To jest mój kot"
    translator = googletrans.Translator()
    lang_from = 'pl'
    lang_to = 'en'
    result = translateChelbes(translator, sentence, lang_from, lang_to)
    assert result.lower() == "this is my cat"


def test_translateChelbesSentenceENGPL():
    sentence="I have a dog"
    translator = googletrans.Translator()
    lang_from = 'en'
    lang_to = 'pl'
    result = translateChelbes(translator, sentence, lang_from, lang_to)
    assert result.lower() == "mam psa"


#def test_translateChelbesOneWordPLENG
#def test_translateChelbesOneWordPLENG
#def test_translateChelbesOneWordPLENG
#def test_translateChelbesOneWordPLENG
#def test_translateChelbesOneWordPLENG
#def test_translateChelbesOneWordPLENG
#def test_translateChelbesOneWordPLENG
