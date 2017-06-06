#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""
import re

def numericTagger(instr):
    lst = type([1,2,3])
    string = type(("Hello", "Hi"))
    tup = ("Hello")
    
    num_match = re.compile(r'([०१२३४५६७८९]+\.)+[०१२३४५६७८९]+|([-+]*\d+\.)+\d+')
    
    if(type(instr) == lst):
        for item in instr:
            if(type(item) == tup):
                if num_match.search(item[0]):
                    item[1] == 'any'
                
            
        print("list")
    else: 
        if(type(instr) == string):
            print("string")
        else:
            print("not supported")

