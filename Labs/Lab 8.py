''' Problem 1 '''

f = open("mydata.txt")
text = f.read()
for line in text.split("\n"):
    if "lol" in line.casefold():
        print(line)
f.close()


def dict_to_str(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other.
    For example, dict_to_str({1:2, 5:6}) should return "1, 2\n5, 6".
    (the order of the key-value pairs doesn’t matter and can be different
    every time).
    """
    for keys, values in d.items():
        print(keys, values)

def dict_to_str_sorted(d):
    """Return a str containing each key and value in dict d. Keys and
    values are separated by a comma. Key-value pairs are separated
    by a newline character from each other, and are sorted in
    ascending order by key.
    For example, dict_to_str_sorted({1:2, 0:3, 10:5}) should
    return "0, 3\n1, 2\n10, 5". The keys in the string must be sorted
    in ascending order."""
    keys = sorted(d.keys())
    for key in keys:
        print(str(key) + ',' , str(d.get(key)))

'''Problem 4a '''
words = open("dict.txt")
words_dict = {}
keys = []
values = []
for line in words:
    for i in range(1, len(line)):
        if (line[i] and line[i - 1]) == " ":
            if line[i + 1: len(line) - 1] not in words_dict:
                words_dict[line[0: i - 1]] = []
            words_dict[line[0: i - 1]].append(line[i + 1: len(line) - 1])
            break        
''' Problem 4b '''
phones = open("phones.txt")
phones_dict = {}
for line in phones:
    for i in range(len(line)):
        if line[i] == "\t":
            if line[i + 1: len(line) - 1] not in phones_dict:
                phones_dict[line[i + 1: len(line) - 1]] = []
            phones_dict[line[i + 1: len(line) - 1]].append(line[0:i])
print(phones_dict)
''' Problem 4c '''
def vowel_counter(word):
    ''' 
        To approximate the number
        of syllables in a word, we will count the number of vowel phones in a word, 
        counting consecutive vowel phones as one vowel.
    '''
    vowels = phones_dict["vowel"]
    vowel_counter = 0
    word_phones = words_dict[str(word)]
    for word in word_phones:
        for char in word:
            if char.isdigit():
                word = word.replace(char, "")
        word_phones = word
    for words in word_phones.split(" "):
        if words in vowels:
            vowel_counter += 1
    return vowel_counter

print(vowel_counter("AARON"))

def word_counter(text):
    words = text.split(" ")
    return len(words)

def sentence_counter(text):
    sentences = text.split(".").split("?").split("!")
    return len(sentences)
''' Problem 5 '''
def readibility(text):
    word_count = word_counter(text)
    sentence_count = sentence_counter(text)
    words = text.split(" ")
    for word in words:
        pass

