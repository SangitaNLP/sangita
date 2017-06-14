#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: djokester
Samriddhi Sinha,
IIT Kharagpur
"""


import hindi.tokenizer as tok 
import matplotlib.pyplot as plt

"""
:param text: A text based on which the Lexical Distribution plot is to be drawn
:type text: string
:param words: A list of words, whose Distribution across the text is plotted.
:type: list
:param lang: The ISO 639-1 Language Code of the language in which the text is based on.
:type: string
:return void 
"""

def dispersionPlot(text, words):
    
    tokens = tok.wordtokenize(text)

    print(words)
    x_length = len(tokens)
    y_length = len(words)
    x_list = []
    y_list = []
    for i in range(0 , x_length):
        for j in range(0 , y_length):
            if tokens[i] == words[j]:
                x_list.append(i+1)
                y_list.append(j)
    plt.plot(x_list, y_list, "b|", scalex=.1)
    plt.yticks(list(range(len(words))), words, color="b")
    plt.ylim(-1, len(words))
    plt.xlabel("Lexical Distribution")
    plt.show()
    
if __name__ == '__main__':
    
    text = "प्रदूषण आज के समय का सबसे बड़ा अभिशाप है जो हमारे विज्ञानं की देन है। प्रदूषण के बढ़ने से हमारे धरती पे बहुत सी समस्याएं पैदा हो गई जिसे अगर समय रहते न रोक गया तो वो दिन दूर नही जब धीरे-धीरे सब खतम हो जायेगा। प्रदुषण के तत्त्व मनुष्यों द्वारा उत्पन्न किया गया पदार्थ या वेस्ट मटेरियल होता है जो की प्राकृतिक संसाधन जैसे की वायु, जल और भूमि आदि को प्रदूषित करते है| प्रदूषण जहरीली गैस, कीटनाशक, शाकनाशी, कवकनाशी, ध्वनि, कार्बनिक मिश्रण, रेडियोधर्मी पदार्थ हो सकते है। दिन पर दिन वनो की कटाई, कारखानो का प्रदूषित धुआं, वाहनो का धुँआ हमारे पूरे वातावरण को दूषित करता जा रहा है। प्रदूषण कई तरह के होते है परन्तु इनमे से सबसे हानिकारक जल प्रदूषण, वायु प्रदूषण, और ध्वनि प्रदूषण है। नगरो का सारा कूड़ा करकट और मल जल में डाल दिया जाता है जिससे हमारे पीने का पानी अशुद्ध हो गया है और इसके सेवन से हमारे शरीर को अनेक तरह की बीमारियां लग रही है। वायु प्रदूषण हमारे द्वारा उत्पन की गई गसो से पूरी हवा में फ़ैल जाता है और वही दूषित हवा को हम श्वास के साथ अंदर लेते है और कई तरह की बिमारियों का शिकार बन जाते है। ध्वनि प्रदूषण का कारण बढ़ती जनसख्या है जिसके कारण शोरगुल बढ़ता जा रहा है जैसे की वाहनो का शोर, कारखानो में मशीनो का शोर इत्यादि । प्रदूषण पर नियंत्रण पाने के लिए संयुक्त प्रयास की आवश्यकता है जिससे की हम एक स्वस्थ्य और प्रदुषण मुक्त वातावरण पा सके।"
    words = ["है", "प्रदूषण"]
    dispersionPlot(text, words)
    