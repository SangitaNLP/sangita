#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""
def sentences():
    
    """
    A simple corpus viewer that returns a list of sentences.  
    :param : None/Void
    :return: A list of sentences.
    :rtype: list
    """
    file = open("corpora/sentence.txt")
    string = file.read()
    sent_list = string.split("\n")
    sent_list = list(filter(None, sent_list))
    return(sent_list)

def words():
    
    """
    A simple corpus viewer that returns a list of words.  
    :param : None/Void
    :return: A list of words.
    :rtype: list
    """
    
    file = open("corpora/word.txt")
    string = file.read()
    word_list = string.split("\n")
    word_list = list(filter(None, word_list))
    return(word_list)

if __name__ == '__main__':
    sents = sentences()
    print(sents)
    wordlst = words()
    print(wordlst)
    