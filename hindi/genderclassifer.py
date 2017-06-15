#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""
import corpora.sentence as sents
import corpora.gender as gndr
import gensim
import tokenizer as tok
import logging
import re
import numpy as np
import pprint as pprint

def numericTagger(instr):
    lst = type([1, 2, 3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    num_match = re.compile(r'([०१२३४५६७८९]+[\.\,]*)+[०१२३४५६७८९]+|([-+]*\d+[\.\,]*)+\d+|([०१२३४५६७८९]+|\d+)')
    if type(instr) == lst:
        for index, item in enumerate(instr):
            if type(item) == tup:
                if num_match.search(str(item[0])):
                    instr[index] = (instr[index][1], 'num')
            else:
                if num_match.search(str(item)):
                    instr[index] = (instr[index], 'num')
    else: 
        if type(instr) == string:
            instr = tok.tokenize(instr)
            numericTagger(instr)
        else:
            print("not supported")

    return instr

def defaultTagger(instr):
    lst = type([1, 2, 3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    if type(instr) == lst:
        for index, item in enumerate(instr):
            if type(item) != tup:
                instr[index] = (instr[index], 'any')
    else: 
        if type(instr) == string:
            instr = tok.tokenize(instr)
            defaultTagger(instr)
        else:
            print("not supported")
    return instr

def lookupTagger(instr):
    lst = type([1, 2, 3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    gndrlst = gndr.drawlist()
    words = []
    genders = []
    for item in gndrlst:
        words.append(item.split("\t")[0])
        if(len(item.split("\t"))>2):
            genders.append("any")
        else:
            genders.append(item.split("\t")[1])
        
    tokens = set(words)
    
    if(type(instr) == lst):
        for index,item in enumerate(instr):
            if(type(item) == tup):
                if item in tokens:
                    tag = genders[words.index(item)]
                    instr[index] = (instr[index][1],tag)
            else:
                if(type(item) != tup):
                    if item in tokens:
                        tag = genders[words.index(item)]
                        instr[index] = (instr[index], tag)
                
    else: 
        if(type(instr) == string):
            instr = tok.tokenize(instr)
            lookupTagger(instr)
            
        else:
            print("not supported")

    return(instr)

def Tagger(instr):
    
    instr = lookupTagger(instr)
    instr = numericTagger(instr)
    instr = defaultTagger(instr)

    return(instr)

def genderencode(genderTag):
    """
    One-hot encoding for the gender tag to be appended 
    at the end of the word-vectors.
    Dimension = 2. 
    """
    if genderTag == 'm':
        code = [1,0]
    if genderTag == 'f':
        code = [0,1]
    if genderTag == 'any':
        code = [1,1]
    if genderTag == 'num':
        code = [0,0]
    return code



sentences = sents.drawlist()
sentences = [tok.tokenize(i) for i in sentences]

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
model = gensim.models.Word2Vec(sentences, min_count=1)

def modify(token):
    """
    Modify tuples from (token, tag) to (token, array) format
    """
    arr = model.wv[token[0]]
    token = [arr, genderencode(token[1])]
    return token

lst = []
for sent in sentences:
    sent = Tagger(sent)
    for word in sent:
        if(word[0].isalpha()==False):
            word = modify(word)
            lst.append(word)

with open("gender.py","w") as f:
    f.write("vectors = ")
    pprint(lst, stream=f)