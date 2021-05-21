import time
import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]

    return math.sqrt(sum_of_squares)



def cosine_similarity(vec1, vec2):
    upper=0.0
    for keys in vec1:
        if keys in vec2:
            upper += vec1[keys]*vec2[keys]
    return upper / (norm(vec1)*norm(vec2))

def build_semantic_descriptors(sentences):
    semantic_descriptor = {}
    
    for item in sentences:
        L = list(set(item))
        if len(L) > 1:
            for word in L:
                if word != "":
                    word = word.lower()
                    if word in semantic_descriptor:
                        for this in L:
                            if this != word:
                                if this in semantic_descriptor[word]:
                                    semantic_descriptor[word][this] += 1
                                else:
                                    semantic_descriptor[word][this] = 1
                    else:
                        dic = {}
                        for this in L:
                            if this != word:
                                if this in dic:
                                    dic[this] += 1
                                else:
                                    dic[this] = 1
                            semantic_descriptor[word] = dic
        
    return semantic_descriptor



def build_semantic_descriptors_from_files(filenames):
    text = ""

    for i in range(len(filenames)):
        text += open(filenames[i], "r", encoding="latin1").read()
        text = text.casefold()
        text += " "

    text = text.replace("!", ".")
    text = text.replace("?", ".")
    text = text.replace("\n", " ")
    text = text.replace(",", " ")
    text = text.replace("-", " ")
    text = text.replace("--", " ")
    text = text.replace(":", " ")
    text = text.replace(";", " ")
    text = text.split('.')

    final_out = []
    for i in range(len(text) - 1):
        final_out.append(text[i].split(" "))


    for i in final_out:
        for j in i:
            while ''in i:
                i.remove('')

    final_dict = build_semantic_descriptors(final_out)
    
    return final_dict



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

import time
start = time.time()
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt", "encyclo.txt"])
res = run_similarity_test("test.txt", sem_descriptors, cosine_similarity)
finish = time.time()
print(res, "of the guesses were correct")
print(finish - start)

