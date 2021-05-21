'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math
import time
from typing import final


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Prosentence_countect 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    numerator = 0
    dena = 0
    for key1,val1 in vec1.items():
        numerator += val1*vec2.get(key1,0.0)
        dena += val1*val1
    denb = 0
    for val2 in vec2.values():
        denb += val2*val2
    return numerator/math.sqrt(dena*denb)

def sanitize(sentences):
    for sentence in sentences:
        for word in sentence:
            word = word.casefold()

def build_semantic_descriptors(sentences):
    final_out = {}
    word_count = 0 #unique word counter
    sentence_count = 0 #sentence counter

    while sentence_count < len(sentences):
        sentence = sentences[sentence_count]
        if sentence == []:
            sentence_count += 1
        elif sentence[word_count] not in final_out:
            cur_sentence_num = sentence_count
            cur_word = sentence[word_count]
            final_out[cur_word] = {}
            word_in_sentence = 0 #word within sentence counter
            while word_in_sentence < len(sentence) and sentence_count < len(sentences):
                cur_sentence = sentences[sentence_count]
                sentence = cur_sentence
                if cur_word in cur_sentence:
                    if cur_sentence[word_in_sentence] != cur_word:
                        if cur_sentence[word_in_sentence] not in final_out[cur_word]:
                            final_out[cur_word][cur_sentence[word_in_sentence]] = 1
                        else:
                            final_out[cur_word][cur_sentence[word_in_sentence]] += 1
                    word_in_sentence += 1
                    if word_in_sentence == len(cur_sentence):
                        sentence_count += 1
                        word_in_sentence = 0
                else:
                    sentence_count += 1
                #print(sentence_count, cur_word)
            print(cur_word)
            if sentence_count == len(sentences):
                sentence_count = cur_sentence_num
                word_count += 1
            if word_count >= len(sentences[sentence_count]):
                sentence_count += 1
                word_count = 0
        else:
            if word_count < len(sentence):
                word_count += 1
            if word_count == len(sentence):
                word_count = 0
                sentence_count += 1
    return final_out



def build_semantic_descriptors_from_files(filenames):
    text=""
    L = []
    for i in range (len(filenames)):
        text += open(filenames[i], "r", encoding="utf-8").read().lower()
        text +=" "
    text = text.replace("!",".").replace("?",".").replace(","," ").replace("-"," ").replace("--"," ").replace(":"," ").replace(";"," ")
    text = text.split(".")
    for i in range (len(text)-1):
        L.append(text[i].split(" "))

    while [''] in L:
        L.remove([''])

    for i in L:
        for j in i:
            while ''in i:
                i.remove('')
    ans=build_semantic_descriptors(L)
    return ans
    #build_semantic_descriptors(text)


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):

    output = choices[0]
    max = 0
    word = word.lower()
    for i in range (len(choices)):
        choices[i] = choices[i].lower()
    if word not in semantic_descriptors:
        return output
    for a in range (len(choices)):

        if choices[a] not in semantic_descriptors:
            similarity = -1
        else:

            similarity = similarity_fn(semantic_descriptors[word], semantic_descriptors[choices[a]])
        if a == 0:
            max = similarity
        if similarity > max:
            max = similarity
            output = choices[a]
    return output


def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    correct_counter = 0.0
    f = open(filename, "r", encoding="latin1").read()
    f = f.casefold()
    f = f.split("\n")
    list = []
    for item in f:
        if item != "":

           list.append(item.split())
    for testing in list:
        if most_similar_word(testing[0], testing[2:], semantic_descriptors, similarity_fn) == testing[1]:
            correct_counter += 1

    return correct_counter/len(list)*100



'''
start = time.time()
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
print(res, "of the guesses were correct")
finish = time.time()
taken = finish - start
print("\n")
print(taken)
'''
start = time.time()
print(build_semantic_descriptors([["i", "am", "a", "sick", "man"], ["i", "am", "a", "spiteful", "man"], ["i", 'am', 'an', 'unattractive', 'man'], ['however', 'i', 'know', 'nothing', 'at', 'all', 'about', 'my', 'disease', 'and', 'do', 'not', 'know', 'for', 'certain', 'what', 'ails', 'me']]))
finish = time.time()
taken = finish - start
print("\n")
print(taken)
