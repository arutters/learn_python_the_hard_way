from nose.tools import *
from ex48 import lexicon
from ex48.parser import *

def test_peek():
    # test a single word
    word = "bear"
    lexicon_scan = lexicon.scan(word)
    word_type = peek(lexicon.scan)
    assert_equal('noun', word_type)

    # test multiple words
    words = "bear is east"
    lexicon_scan = lexicon_scan(words)
    word_type = peek(lexicon.scan)
    assert_equal('noun', word_type)

def test_match():
    # test a single word
    word = "bear"
    lexicon_scan = lexicon.scan(word)
    assert_equal("bear", match(lexicon_scan, 'noun')[1])
    assert_equal(None, match(lexicon_scan, 'noun'))

    # test multiple words