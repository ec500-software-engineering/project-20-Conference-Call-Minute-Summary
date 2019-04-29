from collections import defaultdict
import numpy as np
import jieba

text1 = """
Hi, everyone! My name is Gang and I am gonna introduce you an amazing text-rank algorithm. What is this algorithm? It's 
a really good algorithm because its efficiency and robust. You can type your own text to get a text-rank of your own 
words, to see how brilliant this algorithm is. So, how does this algorithm work? It uses a concept that an algorithm 
is always an good algorithm as long as it is written by me. Make sense? No? OK, actually this text-rank algorithm uses
concept of NLP, which is Natural Language Processing, a significant algorithm nowadays in machine learning area.
Actually I don't know well about NLP, but I understand NLP algorithm is very cool. NLP algorithm help me design and 
implement this text rank algorithm. Now, can you guess the keywords of this stupid text? 
Is that like "Algorithm","text rank"? Do you believe this program can figure it out? Let's see!"""

"""confidence between word and word, dict"""
# text = open('./words/text.txt','r',encoding='utf-8').read()
#text = text1


class TextRank():
    def __init__(self,txtin):
        self.text = txtin
        self.confidence_Dict = dict()
        self.allWord = ""
        self.li_np = np.array(0)
        self.M = ""
        self.U = ""
        self.li = ""

    def get_word_confidence(self):
        # global confidence_Dict
        # global allWord
        stopwords = {line.strip(): 1 for line in open('./words/stopwords.txt', 'r', encoding='utf-8').readlines()}

        sentence_li = [i.lstrip().rstrip() for i in self.text.split('.')]

        co_tuple_dict = defaultdict(int)
        num_dict = defaultdict(int)
        for sentence in sentence_li:

            word_li = [i for i in jieba.cut(sentence) if not stopwords.get(i, None)]
            # print(word_li)
            for i in range(word_li.count(' ')):
                if ' ' in word_li:
                    word_li.remove(' ')
                if '\n' in word_li:
                    word_li.remove('\n')
            # print(word_li)
            for index in range(100):
                new_word_li = word_li[index:index + 5]
                if len(new_word_li) == 5:
                    for a in new_word_li:
                        num_dict[a] += 1
                        for b in new_word_li:
                            if a != b:
                                co_tuple_dict[(a, b)] += 1

        # print(co_tuple_dict)
        # print(num_dict)
        self.confidence_Dict = dict()
        for tuple_ab, num in co_tuple_dict.items():
            self.confidence_Dict[tuple_ab] = num / num_dict[tuple_ab[0]]

        self.allWord = num_dict.keys()
        # print(allWord)
        # print(len(allWord))
        # return self.confidence_Dict, self.allWord


    """get textrank's idea"""


    def get_matrix(self):
        # global li_np
        li = []
        for word in self.allWord:
            li2 = []
            for word2 in self.allWord:
                cow = self.confidence_Dict.get((word, word2), 0)
                li2.append(cow / 4)
            li.append(li2)
            # print(sum(li2))
        # print(li)
        self.li_np = np.array(li)
        # return li_np


    """initialize,converge"""


    def calculate_converge_list(self):
        # global M, U
        self.M = self.li_np.T
        self.U = [1 / len(self.allWord) for i in self.allWord]
        U0 = np.array(self.U)
        # print(U0)
        U_past = []
        while True:
            # U = np.dot(M, U)
            self.U = 0.85 * (np.dot(self.M, self.U)) + 0.15 * U0
            # print('Un: ', U)
            if str(self.U) == str(U_past):
                break
            U_past = self.U
            # print(U)

        # print('U converge to: ', U)
        # print(list(zip(allWord, U)))
        self.li = sorted(list(zip(self.allWord, self.U)), key=lambda x: x[1], reverse=True)
        # print(li)
        # return li


    '''
    In this approach, I just try to combine any two words of the sorted (ranked) words.
    '''


    def get_combine_word(self):
        """combination of words"""
        i = 0
        j = 0
        k = 0
        wordlist = []
        # print(sorted_li)
        sorted_li = self.li
        print("Ranked keywords of this article:\n")
        for w1 in sorted_li[:10]:
            for w2 in sorted_li[:10]:
                if w1[0] + ' ' + w2[0] in self.text:
                    i += 1
                    print("Two keywords combination " + str(i)
                          + ": " + w1[0] + ' ' + w2[0])
                    wordlist.append(("Two keywords combination " + str(i)
                          + ": " + w1[0] + ' ' + w2[0]))
                for w3 in sorted_li[:10]:
                    if w1[0] + ' ' + w2[0] + ' ' + w3[0] in self.text:
                        j += 1
                        print("Three keywords combination " + str(j)
                              + ": " + w1[0] + ' ' + w2[0] + ' ' + w3[0])
                        wordlist.append(("Three keywords combination " + str(j)
                              + ": " + w1[0] + ' ' + w2[0] + ' ' + w3[0]))
                    for w4 in sorted_li[:20]:
                        if w1[0] + ' ' + w2[0] + ' ' + w3[0] + ' ' + w4[0] in self.text:
                            k += 1
                            print("Four keywords combination " + str(j)
                                  + ": " + w1[0] + ' ' + w2[0] + ' '
                                  + w4[0] + ' ' + w3[0])
        return wordlist

# if __name__ == '__main__':
#     confidence_Dict, allWord = get_word_confidence()
#     li_np = get_matrix()
#     sorted_li = calculate_converge_list()
#     out_path = './words/keywords.txt'
#     file = open(out_path, 'w')
#     for i in get_combine_word():
#         file.write(i + '\n')
#     file.close()
