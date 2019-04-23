from collections import defaultdict
import numpy as np
import jieba

text = """
Hi, everyone! My name is Gang and I am gonna introduce you an amazing text-rank algorithm. What is this algorithm? It's 
a really good algorithm because its efficiency and robust. You can type your own text to get a text-rank of your own 
words, to see how brilliant this algorithm is. So, how does this algorithm work? It uses a concept that an algorithm 
is always an good algorithm as long as it is written by me. Make sense? No? OK, actually this text-rank algorithm uses
concept of NLP, which is Natural Language Processing, a significant algorithm nowadays in machine learning area.
Actually I don't know well about NLP, but I understand NLP algorithm is very cool. NLP algorithm help me design and 
implement this text rank algorithm. Now, can you guess the keywords of this stupid text? 
Is that like "Algorithm","text rank"? Do you believe this program can figure it out? Let's see!"""


'''
Test results:
------------------
Two keywords combination1: text rank
Three keywords combination1: text rank algorithm
Two keywords combination2: rank algorithm
Two keywords combination3: NLP algorithm
Two keywords combination4: good algorithm
Two keywords combination5: own text

Process finished with exit code 0
'''

"""confidence between word and word, dict"""


def get_word_confidence():
    global confidence_Dict
    global allWord
    stopwords = {line.strip(): 1 for line in open('./words/stopwords.txt', 'r', encoding='utf-8').readlines()}

    sentence_li = [i.lstrip().rstrip() for i in text.split('.')]

    co_tuple_dict = defaultdict(int)
    num_dict = defaultdict(int)
    for sentence in sentence_li:
        word_li = [i for i in jieba.cut(sentence) if not stopwords.get(i, None)]
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
    confidence_Dict = dict()
    for tuple_ab, num in co_tuple_dict.items():
        confidence_Dict[tuple_ab] = num / num_dict[tuple_ab[0]]

    allWord = num_dict.keys()
    # print(allWord)
    # print(len(allWord))
    return confidence_Dict, allWord


"""get textrank's idea"""


def get_matrix():
    global li_np
    li = []
    for word in allWord:
        li2 = []
        for word2 in allWord:
            cow = confidence_Dict.get((word, word2), 0)
            li2.append(cow / 4)
        li.append(li2)
        # print(sum(li2))
    # print(li)
    li_np = np.array(li)
    return li_np


"""initialize,converge"""


def calculate_converge_list():
    global M, U
    M = li_np.T
    U = [1 / len(allWord) for i in allWord]
    U0 = np.array(U)
    # print(U0)
    U_past = []
    while True:
        # U = np.dot(M, U)
        U = 0.85 * (np.dot(M, U)) + 0.15 * U0
        # print('Un: ', U)
        if str(U) == str(U_past):
            break
        U_past = U
        # print(U)

    # print('U converge to: ', U)
    # print(list(zip(allWord, U)))
    li = sorted(list(zip(allWord, U)), key=lambda x: x[1], reverse=True)
    # print(li)
    return li


'''
In this approach, I just try to combine any two words of the sorted (ranked) words.
'''


def get_combine_word():
    """combination of words"""
    i = 0
    j = 0
    for w1 in sorted_li[:10]:

        for w2 in sorted_li[:10]:
            if w1[0] + ' ' + w2[0] in text:
                i += 1
                print("Two keywords combination" + str(i) + ": " + w1[0] + ' ' + w2[0])
            for w3 in sorted_li[:10]:
                if w1[0] + ' ' + w2[0] + ' ' + w3[0] in text:
                    j += 1
                    print("Three keywords combination" + str(j) + ": " + w1[0] + ' ' + w2[0] + ' ' + w3[0])


if __name__ == '__main__':
    confidence_Dict, allWord = get_word_confidence()
    li_np = get_matrix()
    sorted_li = calculate_converge_list()
    get_combine_word()
 
