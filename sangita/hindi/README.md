# Hindi Natural Language Processing Tools
Contains folders and files related to Natural Language Processing tasks in Hindi. 

# Corpus
Contains linguistic data file like words and their POS tags, lemmas, and gender data. They can be manipulated with the ***corpus submodule***

[//]: <> (Include an explaination of the code.)

# Indian Tokenizer
The base of the Indian tokenizer remains same across all languages. They are slightly modified and included under the respective language modules to suit language specific needs. There are three types of tokenizers that have been included.

1. The Simple Tokenizer
2. The Word Tokenizer
3. The Sentence Tokenizer

[//]: <> (Show Code Examples.) 

# Gender Tagger
The standard gender tagger which we are using is a Dictionary lookup tagger which is backed off by a numeric tagger as well as a default tagger. 

There are three tags 
1. m: male, 
2. f: female, 
3. any: includes both/neither of m and f 

So basically the ***Tagger*** first looks for matches in the Corpus via the ***lookupTagger()***. Then it calls out the ***numericTagger()*** to tag Hindi as well as Arabic Numbers.The remaining untagged words are tagged by the ***defaultTagger()*** as "any". 

Examples:

```python
>>> import sangita.hindi.gender as gender
>>> gender.Tagger("राजद के विज्ञापन में लालू प्रसाद की बड़ी तस्वीर के साथ ही धनिक लाल मंडल ( पूर्व राज्यपाल ), तस्लीमुद्दीन ( केंद्रीय मंत्री ), गुलाम सरवर ( बिहार विधान सभा के पूर्व अध्य ), अति पिछड़ी जातियों के सांसदों और विधायकों की फोटो छपीं हैं।")
[('राजद', 'm'), ('के', 'any'), ('विज्ञापन', 'm'), ('में', 'any'), ('लालू', 'm'), ('प्रसाद', 'any'), ('की', 'any'), ('बड़ी', 'f'), ('तस्वीर', 'f'), ('के', 'any'), ('साथ', 'm'), ('ही', 'any'), ('धनिक', 'm'), ('लाल', 'any'), ('मंडल', 'any'), ('(', 'any'), ('पूर्व', 'any'), ('राज्यपाल', 'm'), (')', 'any'), (',', 'any'), ('तस्लीमुद्दीन', 'm'), ('(', 'any'), ('केंद्रीय', 'any'), ('मंत्री', 'any'), (')', 'any'), (',', 'any'), ('गुलाम', 'm'), ('सरवर', 'm'), ('(', 'any'), ('बिहार', 'm'), ('विधान', 'any'), ('सभा', 'f'), ('के', 'any'), ('पूर्व', 'any'), ('अध्यक्ष', 'any'), (')', 'any'), (',', 'any'), ('अति', 'any'), ('पिछड़ी', 'f'), ('जातियों', 'f'), ('के', 'any'), ('सांसदों', 'm'), ('और', 'any'), ('विधायकों', 'm'), ('की', 'any'), ('फोटो', 'any'), ('छपीं', 'f'), ('हैं।', 'any')]
```

```python
# A look at the constituent taggers
>>> import sangita.hindi.gender as gender

>>> gender.lookupTagger("हर चरण के बाद लोगों की सांसे थमने लगतीं।")
[('हर', 'any'), ('चरण', 'm'), ('के', 'any'), ('बाद', 'm'), ('लोगों', 'any'), ('की', 'any'), ('सांसे', 'f'), ('थमने', 'any'), 'लगतीं।']

>>> gender.defaultTagger("हर चरण के बाद लोगों की सांसे थमने लगतीं।")
[('हर', 'any'), ('चरण', 'any'), ('के', 'any'), ('बाद', 'any'), ('लोगों', 'any'), ('की', 'any'), ('सांसे', 'any'), ('थमने', 'any'), ('लगतीं।', 'any')]

>>> gender.numericTagger("२००४ 2 8 99")
[('२००४', 'any'), ('2', 'any'), ('8', 'any'), ('99', 'any')]
```

# Lemmatizer
The lemmatizer is based on a dictionary lookup method backed off by a numeric and a default lemmatizer
```python
>>> import sangita.hindi.lemmatizer as lem

>>> print(lem.lookupLemmatizer('पुंछ में हुई मुठभेड़ के बारे में एक सरकारी अधिकारी ने बताया कि १३वीं सिख लाईट इनफेंट्री द्वारा लश्कर-ए - ताइबा गुट के आतंकियों को नियंत्रण-रेखा पर चुनौती देने पर मुठभेड़ रात ११.४५ बजे शुरू हुई।'))
[('पुंछ', 'पुंछ'), ('में', 'में'), ('हुई', 'हो'), ('मुठभेड़', 'मुठभेड़'), ('के', 'के'), ('बारे', 'बारे'), ('में', 'में'), ('एक', 'एक'), ('सरकारी', 'सरकारी'), ('अधिकारी', 'अधिकारी'), 'ने', ('बताया', 'बता'), ('कि', 'कि'), '१३वीं', ('सिख', 'सिख'), ('लाईट', 'लाईट'), ('इनफेंट्री', 'इनफेंट्री'), ('द्वारा', 'द्वारा'), ('लश्कर', 'लश्कर'), '-', ('ए', 'ए'), '-', ('ताइबा', 'ताइबा'), ('गुट', 'गुट'), ('के', 'के'), ('आतंकियों', 'आतंकी'), ('को', 'को'), ('नियंत्रण', 'नियंत्रण'), '-', ('रेखा', 'रेखा'), ('पर', 'पर'), ('चुनौती', 'चुनौती'), ('देने', 'दे'), ('पर', 'पर'), ('मुठभेड़', 'मुठभेड़'), ('रात', 'रात'), '११', '.', '४५', ('बजे', 'बज'), ('शुरू', 'शुरू'), 'हुई।']

>>> print(lem.Lemmatizer('पुंछ में हुई मुठभेड़ के बारे में एक सरकारी अधिकारी ने बताया कि १३वीं सिख लाईट इनफेंट्री द्वारा लश्कर-ए - ताइबा गुट के आतंकियों को नियंत्रण-रेखा पर चुनौती देने पर मुठभेड़ रात ११.४५ बजे शुरू हुई।'))
[('पुंछ', 'पुंछ'), ('में', 'में'), ('हुई', 'हो'), ('मुठभेड़', 'मुठभेड़'), ('के', 'के'), ('बारे', 'बारे'), ('में', 'में'), ('एक', 'एक'), ('सरकारी', 'सरकारी'), ('अधिकारी', 'अधिकारी'), ('ने', 'ने'), ('बताया', 'बता'), ('कि', 'कि'), ('१३वीं', '३'), ('सिख', 'सिख'), ('लाईट', 'लाईट'), ('इनफेंट्री', 'इनफेंट्री'), ('द्वारा', 'द्वारा'), ('लश्कर', 'लश्कर'), ('-', '-'), ('ए', 'ए'), ('-', '-'), ('ताइबा', 'ताइबा'), ('गुट', 'गुट'), ('के', 'के'), ('आतंकियों', 'आतंकी'), ('को', 'को'), ('नियंत्रण', 'नियंत्रण'), ('-', '-'), ('रेखा', 'रेखा'), ('पर', 'पर'), ('चुनौती', 'चुनौती'), ('देने', 'दे'), ('पर', 'पर'), ('मुठभेड़', 'मुठभेड़'), ('रात', 'रात'), ('११', '११'), ('.', '.'), ('४५', '४५'), ('बजे', 'बज'), ('शुरू', 'शुरू'), ('हुई।', 'हुई।')]
```

POS Tagger
Lookup POS Tagger that learns a few rules from textual data and tries to predict unkown cases on the basis of the rules
```python
>>> import sangita.hindi.postagger as pos
>>> import sangita.hindi.tokenizer as tokenizer

>>> print(pos.tagger(tokenizer.tokenize("पालगी भईया कहते हुए धूलीचन्द पांव छूआ और सामने खड़े होकर भीखनरायन की दीन - दशा को चकित होकर निहारने लगा ।")))
('पालगी', 'NN'), ('भईया', 'NN'), ('कहते', 'VM'), ('हुए', 'VAUX'), ('धूलीचन्द', 'NNP'), ('पांव', 'NN'), ('छूआ', 'VM'), ('और', 'CC'), ('सामने', 'NST'), ('खड़े', 'JJ'), ('होकर', 'VM'), ('भीखनरायन', 'NNP'), ('की', 'PSP'), ('दीन', 'NN'), ('-', 'SYM'), ('दशा', 'NN'), ('को', 'PSP'), ('चकित', 'JJ'), ('होकर', 'VM'), ('निहारने', 'VM'), ('लगा', 'VAUX'), ('।', 'SYM')]
```