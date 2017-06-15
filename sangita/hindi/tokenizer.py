#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""

import re 
punctuations ='([?@[\\]<=>^_`{|}~!"#$%&\'()*+,-./:;])' #modify this string to add  more instances
"""
'?@[\\]<=>^_`{|}~!"#$%&\'()*+,-./:;]' the entire punctuation and common symbols set
[ ] helps a single character present in a set
"""

instance = re.compile(punctuations)

def tokenize(string, removePunctuations = False):
    """
    A simple tokenizer that tokenizes based on punctuations.
    An option for removing the punctuations is also provided.
    r'\1' backreferences to the text matched (here the punctuation)
    r' \1 ' helps seperate the punctuation marks from the rest of the text
    r' ' replaces the matched text (here punctuation) with a space, thereby eliminating it. 
    
    :param string: Input string that is to be tokenized 
    :type string: str
    :param removePunctuations: Wether the user wants the symbols to be removed in the list of tokens
    :type removePunctuations: bool
    
    :return: A list of tokens
    :rtype: list
    """
    if removePunctuations == False:
        tokens = instance.sub(r' \1 ', string).strip().split()
    
    if removePunctuations == True:
        tokens = instance.sub(r'  ', string).strip().split()
   
    return(tokens)


def wordtokenize(string):
    """
    A Word Tokenizer that splits up a text into words.
    ([०१२३४५६७८९]+\.)+[०१२३४५६७८९]+ : Captures Decimals in Hindi Numerals
    ([-+]*\d+\.)+\d+ : Captures Decimals in Arabic Numerals
    ([^\.!?",;:।\s\(\)_+=/]+) : Captures Words
    (([^\!?",;:।\s\(\)_+=/]+\.){2,}[^\!?",;:।\s\(\)_+=/]+) : Captures Abbreviations and simple URLs
    
    :param string: Input string that is to be tokenized 
    :type string: strtokens
        
    :return: A list of word
    :rtype: list
    """
    word = r'([०१२३४५६७८९]+[\.\,]*)+[०१२३४५६७८९]+|([-+]*\d+[\.\,]*)+\d+|(([^\!?",;:।\s\(\)_+=/]+\.){2,}[^\!?",;:।\s\(\)_+=/]+)|([^\.!?",;:।\s\(\)_+=/]+)'
    words = [] 
    for m in re.finditer(word, string):
        words.append(m.group())
    return(words)

def sentencetokenize(string):
    """
    A sentence tokenizer that splits up a text into sentences
    [^॥।\.?!] : Is the basic set of Delimiters that mark the end of a sentence
    :param string: Input string that is to be tokenized 
    :type string: str
        
    :return: A list of sentences
    :rtype: list
    """
    delim = re.compile(r'([^।\.?!॥]|[॥।\.?!](?=\s*\"))+\s*[॥।\.?!]{1}\s*')
    sents = []
    for m in re.finditer(delim, string): 
        sents.append(m.group())
    return(sents)

if __name__ == '__main__':
    input_str = 'Hey there! Wassup? \n Nice Meeting You.\t Have a nice day.'
    print(tokenize(input_str))
    print(tokenize(input_str,True))
    print(wordtokenize(input_str))
    
