import time
import math


def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''

    sum_of_squares = 0.0  # floating point to handle large numbers
    for x in vec:
        sum_of_squares += vec[x] * vec[x]


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


def build_semantic_descriptors(sentences):
    final_out = {}
    for i in range(len(sentences)):
        for j in range(len(sentences[i])):
            if sentences[i] == []:
                continue
            if sentences[i][j] not in final_out:
                final_out[sentences[i][j]] = {}
            for k in range(len(sentences[i])):
                if sentences[i][j] != sentences[i][k]:
                    if sentences[i][k] in final_out[sentences[i][j]]:
                        final_out[sentences[i][j]][sentences[i][k]] += 1 
                    else:
                        final_out[sentences[i][j]][sentences[i][k]] = 1

    return final_out



def build_semantic_descriptors_from_files(filenames):
    text = ""

    for i in range(len(filenames)):
        text += open(filenames[i], "r", encoding="latin1").read()
        text = text.casefold()
        text += " "

    text = text.replace("!", ".")
    text = text.replace("?", ".")
    text = text.replace(",", "")
    text = text.replace("-", "")
    text = text.replace("--", "")
    text = text.replace(":", "")
    text = text.replace(";", "")
    text = text.replace("\n", " ")
    text = text.split('.')

    final_out = []
    for i in range(len(text) - 1):
        final_out.append(text[i].split(" "))


    for i in final_out:
        for j in i:
            while '' in i:
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


start = time.time()
sem_descriptors = build_semantic_descriptors_from_files(["wp.txt", "sw.txt", "encyclo.txt"])
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
'''