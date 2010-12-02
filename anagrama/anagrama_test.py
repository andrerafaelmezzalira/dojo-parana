#!/usr/bin/env python
# -*- coding=utf-8 -*- 

import unittest

def test_anagram(palavra1, palavra2, chars):
    palavras = sorted(list(palavra1+palavra2))
    chars = sorted(list(chars))
    return palavras == chars

def read_word_list(file_name):
    fp = open(file_name)
    return [x.strip() for x in fp]

def test_pairs(word_list, chars):
    r = []
    for word1 in word_list:
        for word2 in word_list:
            if test_anagram(word1, word2, chars):
		r.append( [word1, word2] )
    return r

class AnagramaTest(unittest.TestCase):
    def test_anagram_test(self):
        self.assertTrue(test_anagram('a', 'b', 'ab'))
        self.assertFalse(test_anagram('a', 'x', 'ab'))
        self.assertTrue(test_anagram('ab', 'cd', 'abcd'))
        self.assertTrue(test_anagram('ac', 'bd', 'abcd'))

    def test_anagram_letras_repetidas(self):
        self.assertTrue(test_anagram('aab', 'bbc', 'aabbbc'))
        self.assertFalse(test_anagram('aab', 'bbc', 'abc'))
        self.assertFalse(test_anagram('aab', 'bcc', 'aabbbc'))

    def test_read_word_list(self): 
        self.assertEquals(read_word_list('wordlist.txt'), ['a', 'b'])

    def test_word_list(self):
        word_list = ['aab','bbc','ac']
        self.assertEquals(test_pairs(word_list,'xyz'), [])
        self.assertEquals(test_pairs(word_list, 'ccaa'),[['ac', 'ac']]) 

if __name__ == '__main__':
   unittest.main()
