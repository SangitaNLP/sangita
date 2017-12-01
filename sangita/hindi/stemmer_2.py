import corpora.lemmata as lemma
import tokenizer as tok
import os

def endsplit(a_string,suffix):
	if a_string.endswith(suffix):
		return a_string[:-len(suffix)]
	return a_string	

def stemmer(string,mincount):
	lemmata = lemma.drawlist()
	lemmata = [i.split('\t') for i in lemmata]
	inflections = []
	for i in lemmata:
		x = len(os.path.commonprefix(i))
		inflections.append((i[0])[x:])
		inflections.append((i[1])[x:])
	inflections = set(inflections) - set([''])
	if isinstance(string,str):
		words = tok.wordtokenize(string)
		for index,item in enumerate(words):
			temp=[]
			for inflection in inflections:
				temp.append(endsplit(item,inflection))
			words[index] = set(temp)
		return words		
