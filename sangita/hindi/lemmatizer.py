#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 23:28:21 2017

@author: samriddhi
"""
import re
import sangita.hindi.tokenizer as tok
import sangita.hindi.corpora.lemmata as lt

def numericLemmatizer(instr):
    lst = type([1,2,3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    
    num_match = re.compile(r'([०१२३४५६७८९]+[\.\,]*)+[०१२३४५६७८९]+|([-+]*\d+[\.\,]*)+\d+|([०१२३४५६७८९]+|\d+)')
    
    if(type(instr) == lst):
        for index,item in enumerate(instr):
            if(type(item) == tup):
                if num_match.search(str(item[0])):
                    instr[index] = (instr[index][1], instr[index][1])
            else:
                if num_match.search(str(item)):
                    instr[index] = (instr[index], instr[index][1])
                
                    
    else: 
        if(type(instr) == string):
            instr = tok.tokenize(instr)
            numericLemmatizer(instr)
        else:
            print("not supported")

    return(instr)

def defaultLemmatizer(instr):

    lst = type([1,2,3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    

    if(type(instr) == lst):
        for index,item in enumerate(instr):
            if(type(item) != tup):
                instr[index] = (instr[index], instr[index])
                
    else: 
        if(type(instr) == string):
            instr = tok.tokenize(instr)
            defaultLemmatizer(instr)
            
        else:
            print("not supported")

    return(instr)

def lookupLemmatizer(instr):
    
    lst = type([1,2,3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    
    lemmatalist = lt.drawlist()
    words = []
    lemma = []
    for item in lemmatalist:
        words.append(item.split("\t")[0])
        lemma.append(item.split("\t")[1])
        
    tokens = set(words)
    
    if(type(instr) == lst):
        for index,item in enumerate(instr):
            if(type(item) == tup):
                if item in tokens:
                    tag = lemma[words.index(item)]
                    instr[index] = (instr[index][1],tag)
            else:
                if(type(item) != tup):
                    if item in tokens:
                        tag = lemma[words.index(item)]
                        instr[index] = (instr[index], tag)
                
    else: 
        if(type(instr) == string):
            instr = tok.tokenize(instr)
            lookupLemmatizer(instr)
            
        else:
            print("not supported")

    return(instr)

def Lemmatizer(instr):
    
    instr = lookupLemmatizer(instr)
    instr = numericLemmatizer(instr)
    instr = defaultLemmatizer(instr)

    return(instr)

if __name__ == '__main__':
    input_str = 'पुंछ में हुई मुठभेड़ के बारे में एक सरकारी अधिकारी ने बताया कि १३वीं सिख लाईट इनफेंट्री द्वारा लश्कर-ए - ताइबा गुट के आतंकियों को नियंत्रण-रेखा पर चुनौती देने पर मुठभेड़ रात ११.४५ बजे शुरू हुई।'
    print(lookupLemmatizer(input_str))
    print(numericLemmatizer(input_str))
    print(defaultLemmatizer(input_str))
    print(Lemmatizer(input_str))
  