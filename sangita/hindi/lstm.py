#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""

import sangita.hindi.corpora.sentence as sent
import sangita.hindi.tokenizer as tok
import gensim
import logging
import numpy as np
import re
import sangita_data.hindi.sentences.loadsent as sents
import sangita_data.hindi.posVectors.poslist as ps
import operator 
from keras.models import Sequential
from keras.layers import LSTM, Dense

def decode(lst):
    tags = ['ECH', 'NST', 'QO', 'RP', 'WQ', 'NN', 'UNK', 'DEM', 'NEG', 'SYM', 'PRP', 'INJ', 'RDP', 'PSP', 'VM', 'VAUX', 'RB', 'QF', 'CC', 'INTF', 'JJ', 'QC', 'NNP']
    temp = []
    for i in lst:
        index = i.tolist().index(max(i.tolist()))
        temp.append(tags[index])
    return temp
    
def tagger(sentence):
    sentences = sent.drawlist()
    sentences2 = sents.drawlist()
    sentences2.append(sentence)
    sentences = sentences + sentences2
    sentences = [tok.wordtokenize(i) for i in sentences]
    sentence = tok.wordtokenize(sentence)

    pos = ps.drawlist()
    vector = [i[0] for i in pos]
    tags = [i[1] for i in pos]
    
    y_test = np.array(tags[:200]).reshape((200, 23))
    y_train = np.array(tags[200:]).reshape((len(tags)-200, 23))
    x_train = np.array(vector[200:]).reshape((len(tags)-200, 1,  30))
    x_test = np.array(vector[:200]).reshape((200, 1,  30))
    
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    model = gensim.models.Word2Vec(sentences, size =30,  min_count=1)

    pred = []
    for word in sentence:
        pred.append(model.wv[word].tolist())
    
    predictions = np.array(pred).reshape((len(pred),1,30))
    print(x_test.shape)
    print(y_train.shape)
    print(x_train.shape)
    
    model = Sequential()
    model.add(LSTM(32, return_sequences = True, input_shape = (1, 30)))
    model.add(LSTM(32, return_sequences = True))
    model.add(LSTM(32))
    model.add(Dense(23,activation = 'softmax'))
    model.compile(loss = "categorical_crossentropy", optimizer = "rmsprop", metrics = ['accuracy'])
    model.fit(x_train, y_train, batch_size= 64 , epochs = 5, validation_data = (x_test,y_test))
    
    out = model.predict(predictions)
    tag = decode(out)
    for index, item in enumerate(sentence):
        sentence[index] = (item, tag[index])
    
    return(sentence)

if __name__ == '__main__':
    input_str = 'आपके इसी प्रेम को ध्यान में रख कर हम आपको विश्वास दिलाते हैं की इन्टरनेट के हर कोने से खोज कर हम आपके लिए बेहतरीन और उन्न्दा किस्म की पुस्तके मुफ्त उपलब्ध कराते रहंगे | हर दिन एक बेहतरीन पुस्तक आपकी राह देखेगी |'
    print(tagger(input_str))