#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""
import re
import sangita.hindi.tokenizer as tok
import sangita.hindi.corpora.gender as gndr

def numericTagger(instr):
    lst = type([1,2,3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    
    num_match = re.compile(r'([०१२३४५६७८९]+[\.\,]*)+[०१२३४५६७८९]+|([-+]*\d+[\.\,]*)+\d+|([०१२३४५६७८९]+|\d+)')
    
    if(type(instr) == lst):
        for index,item in enumerate(instr):
            if(type(item) == tup):
                if num_match.search(str(item[0])):
                    instr[index] = (instr[index][1],'any')
            else:
                if num_match.search(str(item)):
                    instr[index] = (instr[index], 'any')
                
                    
    else: 
        if(type(instr) == string):
            instr = tok.tokenize(instr)
            numericTagger(instr)
            
        else:
            print("not supported")

    return(instr)

def defaultTagger(instr):

    lst = type([1,2,3])
    tup = type(("Hello", "Hi"))
    string = type("Hello")
    

    if(type(instr) == lst):
        for index,item in enumerate(instr):
            if(type(item) != tup):
                instr[index] = (instr[index], 'any')
                
    else: 
        if(type(instr) == string):
            instr = tok.tokenize(instr)
            defaultTagger(instr)
            
        else:
            print("not supported")

    return(instr)
    

    

def lookupTagger(instr):
    
    lst = type([1,2,3])
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


if __name__ == '__main__':
    input_str = 'पुंछ में हुई मुठभेड़ के बारे में एक सरकारी अधिकारी ने बताया कि १३वीं सिख लाईट इनफेंट्री द्वारा लश्कर-ए - ताइबा गुट के आतंकियों को नियंत्रण-रेखा पर चुनौती देने पर मुठभेड़ रात ११.४५ बजे शुरू हुई।'
    print(lookupTagger(input_str))
    print(numericTagger(input_str))
    print(defaultTagger(input_str))
    print(Tagger(input_str))
  