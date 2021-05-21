#1a
def word_counts():
    out = {}
    f = open("mydata.txt", encoding = "latin-1")
    text = f.read().split(" ")
    for word in text:
        if word == "":
            continue
        if word in out:
            continue
        elif word not in out:
            out[word] = text.count(word)
    return out

#1b
def top10(L):
    return sorted(L, reverse=True)[ : 10]

#print(top10([1, 20, 30, 9, 2, 5, 69, 420, 421, 422, 423, 42069, 62420])) 

#1c
def top10_words():
    return sorted(word_counts(), key = word_counts().get, reverse= True)[ : 10]

print(top10_words())

#3
import urllib.request
def num_results(term):       #term means the search term, which should be a string, assumes one word without spaces
    f = urllib.request.urlopen('https://ca.search.yahoo.com/search?p=' + term + '&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8')
    page = f.read().decode("utf-8")
    f.close()
    all_instances = []
    for a in range(len(page) - 8):
        if page[a:a+7] == 'results':
            all_instances.append(page[a-14:a])
    for b in range(len(all_instances)):
        count = 0
        for c in range(len(all_instances[b])):
            if all_instances[b][c].isdigit() == True:
                count += 1
        if count/len(all_instances[b]) > 0.5:
            num_str = ''
            for d in range(len(all_instances[b])):
                if all_instances[b][d].isdigit() == True:
                    num_str = num_str + all_instances[b][d]
            return int(num_str) 

#print(num_results("uoft"))