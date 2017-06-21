#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""

import corpora.lemmata as lemma
import tokenizer as tok
def endsplit(a_string, suffix):
    if a_string.endswith(suffix):
        return a_string[:-len(suffix)]
    return a_string

    

def stemmer(string, min_count):
    lemmata = lemma.drawlist()
    lemmata = [i.split("\t") for i in lemmata]
    inflections = [(i[0].split(i[1]))[len(i[0].split(i[1]))-1] for i in lemmata]
    
    inflections = list(set(list(filter(None, inflections))))
    inflections = [i for i in inflections if len(i)<5]
    #inflections = [i for i in inflections if len(i)<min_count] 
    print(inflections)
    
    if isinstance(string, str):
        words = tok.wordtokenize(string)
        for index,item in words:
            temp = []
            for inflection in inflections:
                temp.append(endsplit(item, inflection))
                temp = set(temp)
            words[index] = ((temp))
            minlength = min(len(s) for s in stringlist)
            return minlength
        