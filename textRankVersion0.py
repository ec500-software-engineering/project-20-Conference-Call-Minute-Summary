from collections import defaultdict
import numpy as np
import jieba

text = """
Hi, everyone! My name is Gang and I am gonna introduce you an amazing text-rank algorithm. What is this algorithm? It's 
a really good algorithm because its efficiency and robust. You can type your own text to get a text-rank of your own 
words, to see how brilliant this algorithm is. So, how does this algorithm work? It uses a concept that an algorithm 
is always an good algorithm as long as it is written by me. Make sense? No? OK, actually this text-rank algorithm uses
concept of NLP, which is Natural Language Processing, a significant algorithm nowadays in machine learning area."""


"""confidence between word and word, dict"""

def get_word_confidence():

    global co_dict
    global word_all
    stopwords = {line.strip(): 1 for line in open('./data/stopwords.txt', 'r', encoding='utf-8').readlines()}

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
        #print(word_li)
        for index in range(100):
            new_word_li = word_li[index:index + 5]
            if len(new_word_li) == 5:
                for a in new_word_li:
                    num_dict[a] += 1
                    for b in new_word_li:
                        if a != b:
                            co_tuple_dict[(a, b)] += 1

    #print(co_tuple_dict)
    #print(num_dict)
    co_dict = dict()
    for tuple_ab, num in co_tuple_dict.items():
        co_dict[tuple_ab] = num / num_dict[tuple_ab[0]]

    word_all = num_dict.keys()
    #print(word_all)
    #print(len(word_all))
    return co_dict, word_all

"""get textrank's idea"""

def get_square_matrix():
    
    global li_np
    li = []
    for word in word_all:
        li2 = []
        for word2 in word_all:
            cow = co_dict.get((word, word2), 0)
            li2.append(cow / 4)
        li.append(li2)
        # print(sum(li2))
    #print(li)
    li_np = np.array(li)
    return li_np

"""initialize,converge"""

def calculate_converge_list():
    global M, U
    M = li_np.T
    U = [1 / len(word_all) for i in word_all]
    U0 = np.array(U)
    #print(U0)
    U_past = []
    while True:
        # U = np.dot(M, U)
        U = 0.85 * (np.dot(M, U)) + 0.15 * U0
        # print('Un: ', U)
        if str(U) == str(U_past):
            break
        U_past = U
        # print(U)

    #print('U converge to: ', U)
    #print(list(zip(word_all, U)))
    li = sorted(list(zip(word_all, U)), key=lambda x: x[1], reverse=True)
    #print(li)
    return li

'''
In this approach, I just try to combine any two words of the sorted (ranked) words.
'''

def get_combine_word():
    """combination of words"""
    for w1 in sorted_li[:10]:
        for w2 in sorted_li[:10]:
            if w1[0] + ' ' + w2[0] in text:
                print(w1[0] + ' ' + w2[0])
            for w3 in sorted_li[:10]:
                if w1[0] + ' ' + w2[0] + ' ' + w3[0] in text:
                    print(w1[0] + ' '+ w2[0] + ' ' + w3[0])


if __name__ == '__main__':
    co_dict, word_all = get_word_confidence()
    li_np = get_square_matrix()
    sorted_li = calculate_converge_list()
    get_combine_word()
