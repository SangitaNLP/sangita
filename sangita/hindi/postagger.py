#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""


import sangita.hindi.tokenizer
import sangita.hindi.corpora.unigrampos as unigram 
import sangita.hindi.corpora.bigrampos as bigram 
import sangita.hindi.corpora.trigrampos as trigram
import sangita.hindi.corpora.bigramrules as birules
import sangita.hindi.corpora.trigramrules as trirules

def bigramFinder(rule):
    bi = birules.drawlist()
    rules = [i[0] for i in bi]
    index = rules.index(rule)
    return index
    
def NoneTagger(lst):
    for index, item  in enumerate(lst):
        lst[index] = (item, None)
    return lst

def UnigramTagger(lst):
    pos = unigram.drawlist()
    tokens = [i[0] for i in pos]
    tags = [i[1][0][0] for i in pos]
    for index, item  in enumerate(lst):
        word = item[0]
        if word in tokens:
            tag = tags[tokens.index(word)]
            lst[index] = (word, tag)
    return lst

def BigramTagger(lst):
    pos = bigram.drawlist()
    tokens = [i[0] for i in pos]
    tags = [i[1] for i in pos]
    for index, item  in enumerate(lst):
        word = item[0]
        if word in tokens:
            tag = tags[tokens.index(word)]
            if index > 0:
                for i in tag:
                    if(i[0][0] == lst[index-1][1]):
                        lst[index] = (word, i[0][1])    
    return lst

def TrigramTagger(lst):
    pos = trigram.drawlist()
    tokens = [i[0] for i in pos]
    tags = [i[1] for i in pos]
    for index, item  in enumerate(lst):
        word = item[0]
        if word in tokens:
            tag = tags[tokens.index(word)]
            if index > 1:
                for i in tag:
                    if(i[0][0] == lst[index-2][1] and i[0][1] == lst[index-1][1]):
                        lst[index] = (word, i[0][2])    
    return lst

def RuleTagger(lst):
    bi = birules.drawlist()
    tri = trirules.drawlist()
    for words in lst:
        if words[1] == None:
            index = lst.index(words)
            suggestions = []
            if index > 0 and index<(len(lst)-1):
                if(lst[index-1][1] != None and lst[index+1][1]!= None):
                    for rule in tri:
                        if(lst[index-1][1] == rule[0][0] and lst[index+1][1] == rule[0][2]):
                            biIndex1 = bigramFinder([rule[0][0], rule[0][1]])
                            count1 = bi[biIndex1][1]
                            biIndex2 = bigramFinder([rule[0][1], rule[0][2]])
                            count2 = bi[biIndex2][1]
                            suggestions.append([rule[0], count1 + count2 - rule[1], 1])
            if index<(len(lst)-2):
                if(lst[index+1][1] != None and lst[index+2][1]!= None):
                    for rule in tri:
                        if(lst[index+1][1] == rule[0][1] and lst[index+2][1] == rule[0][2]):
                            biIndex1 = bigramFinder([rule[0][0], rule[0][1]])
                            count1 = bi[biIndex1][1]
                            biIndex2 = bigramFinder([rule[0][1], rule[0][2]])
                            count2 = bi[biIndex2][1]
                            suggestions.append([rule[0], rule[1], 0])
            if index>(1):
                if(lst[index-1][1] != None and lst[index-2][1]!= None):
                    for rule in tri:
                        if(lst[index-2][1] == rule[0][0] and lst[index-1][1] == rule[0][1]):
                            biIndex1 = bigramFinder([rule[0][0], rule[0][1]])
                            count1 = bi[biIndex1][1]
                            biIndex2 = bigramFinder([rule[0][1], rule[0][2]])
                            count2 = bi[biIndex2][1]
                            suggestions.append([rule[0], rule[1], 2])
            if len(suggestions) != 0:
                count = [i[1] for i in suggestions]
                index = (count.index(max(count)))
                tag = suggestions[index][0][suggestions[index][2]]
                print(suggestions)
                print(lst[lst.index(words)][0])
                lst[lst.index(words)] = (lst[lst.index(words)][0],tag)
            
    return lst

def tagger(lst):
    #if isinstance(lst) == str:
    #    lst = tokenizer.tokenize(lst)
    lst = NoneTagger(lst)
    lst = UnigramTagger(lst)
    lst = BigramTagger(lst)
    lst = TrigramTagger(lst)
    lst = RuleTagger(lst)
    return lst

if __name__ == "__main__":
    print(UnigramTagger(NoneTagger(tokenizer.tokenize("पालगी भईया कहते हुए धूलीचन्द पांव छूआ और सामने खड़े होकर भीखनरायन की दीन - दशा को चकित होकर निहारने लगा ।"))))
    print(BigramTagger(UnigramTagger(NoneTagger(tokenizer.tokenize("पालगी भईया कहते हुए धूलीचन्द पांव छूआ और सामने खड़े होकर भीखनरायन की दीन - दशा को चकित होकर निहारने लगा ।")))))
    print(TrigramTagger(BigramTagger(UnigramTagger(NoneTagger(tokenizer.tokenize("पालगी भईया कहते हुए धूलीचन्द पांव छूआ और सामने खड़े होकर भीखनरायन की दीन - दशा को चकित होकर निहारने लगा ।"))))))
    print(RuleTagger(UnigramTagger(NoneTagger(tokenizer.tokenize("मुझे इस जीवन से प्यार है मैं इस जीवन को यथासंभव लंबे समय तक जीना चाहता हूं।")))))
    print((UnigramTagger(NoneTagger(tokenizer.tokenize("मुझे इस जीवन से प्यार है मैं इस जीवन को यथासंभव लंबे समय तक जीना चाहता हूं।")))))
