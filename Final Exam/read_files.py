import os
filenames = os.listdir("diseases") # Obtain a list of the files in the folder
                                   # diseases
f = open("diseases/" + filenames[0]) # Open the first file in the folder diseases
#print(text0[:2000])  # Output the first 2000 characters in the file we opened


def text_processor(text):
    text = text.lower()
    text = text.replace(",", ".").replace("!", ".").replace("?", ".").replace("-", ".").replace(" ", ".").replace("\n", ".").replace("\n\n", ".")
    new_text = text.split(".")
    return new_text

def most_common_frequent_word(files):
    common_words = {}
    for file in files:
        f = open(file).read()
        words = text_processor(f)
        word_dict = {}
        for word in words:
            if word not in word_dict:
                word_dict[word] = words.count(word)
        freq_word = sorted(word_dict, key = word_dict.get, reverse= True)[0]
        i = 0
        while freq_word == "":
            freq_word = sorted(word_dict, key = word_dict.get, reverse= True)[i]
            i += 1
        i = 0
        if freq_word not in common_words:
            common_words[freq_word] = 0
            common_words[freq_word] += 1
        else:
            common_words[freq_word] += 1
    return sorted(common_words, key = common_words.get, reverse= True)[0]
    

print(most_common_frequent_word(["diseases/" + "RNA_virus.html",
                                "diseases/" + "Virus.html",
                                "diseases/" + "Yeast.html"]))
