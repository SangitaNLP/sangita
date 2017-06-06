#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""

def numberTagger(instr):
    lst = type([1,2,3])
    string = type("Hello")
    
    if(type(instr) == lst):
        print("list")
    else: 
        if(type(instr) == string):
            print("string")
        else:
            print("not supported")

