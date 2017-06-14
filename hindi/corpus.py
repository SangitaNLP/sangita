#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""
import sangita.hindi.corpora.sentence as sent
import sangita.hindi.corpora.word as wrd

def sentences():
    """
    A simple corpus viewer that returns a list of sentences.  
    :param : None/Void
    :return: A list of sentences.
    :rtype: list
    """
    sent_list = sent.drawlist()
    sent_list = list(filter(None, sent_list))
    return sent_list

def words():
    """
    A simple corpus viewer that returns a list of words.  
    :param : None/Void
    :return: A list of words.
    :rtype: list
    """
    word_list = wrd.drawlist()
    word_list = list(filter(None, word_list))
    return word_list

if __name__ == '__main__':
    sents = sentences()
    print(sents)
    wordlst = words()
    print(wordlst)
    
