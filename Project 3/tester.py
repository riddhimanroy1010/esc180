# No need to thank me but if you really want to express your gratitude 
# feel free to get me some BBT once covid has passed :)
# Also don't even try looking at this code it's f****** disgusting

import socket, threading, json, contextlib, io, time
from random import *

synonyms = __import__("synonyms") #put your filename here (pls for the love of god run this shit in the same folder as your file (and for the love of jesus do not pyzo this))

HEADER = 16
DELAY = 0.0 #hehehehe
PORT = 5555
FORMAT = 'utf-8'
HOST_IP = '172.105.7.203' #hackers. Challenge accepted aight?

class Network:

    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = HOST_IP 
        self.addr = (self.host, PORT)
        self.id = self.connect()

    def connect(self):
        self.client.connect(self.addr)
        self.client.send(str.encode('controller'))
        received_message = self.client.recv(2048).decode(FORMAT)
        print(received_message)

    def send(self, function, data = ""):
        try:
            #print(function +":" + str(data))
            self.client.send(str.encode(function +":" + str(data)))
            cnt = 0
            while(True or cnt > 1000):
                cnt += 1
                try:    
                    msg_length = int(self.client.recv(HEADER).decode(FORMAT))
                    break
                except:
                    continue
            #print("MSG LENGTH: ", msg_length)
            temp = ""
            while(len(temp) < msg_length):
                temp += self.client.recv(4096).decode(FORMAT)
            return temp
        except socket.error as e:
            print(str(e))
            return False

    def get_sentences(self):
        return self.send("get_sentences")

    def get_dict(self):
         temp = self.send("get_dict")
         #print("LENGTH: ", len(temp))
         return json.loads(temp)

    def get_cos(self):
        return json.loads(self.send("get_cos"))

    def get_tests(self):
        return self.send("get_tests")
        

class client():

    def __init__(self):
        self.network = Network()

    def run(self):
        not_ended = True
        print("Hello! Welcome to mrmandarin's synonyms testing program!")

        while(not_ended):
            print("Here are your options:")
            print("1 - Check Build Semantic Descriptors (Subpart b + c)")
            print("2 - Continuously Check Build Semantic Descriptors")
            print("3 - Continuously Test Cosine Similarity (Subpart a)")       
            print("4 - Continuously Run Similarity Test (All subparts)")     
            print("5 - Exit")
            s = input()
            if(s == '5'):
                not_ended = False
            elif(s == '1'):
                self.check()
            elif(s == '2'):
                self.continuous_check()
            elif(s == '3'):
                self.continuous_cosine()
            elif(s == '4'):
                self.continuous_run()
            else:
                print("Dafuq you entered boii")

    def check(self):
        print('\n')
        sentences = self.network.get_sentences()
        mandarin_dict = self.network.get_dict()
        f = open("sample_case.txt", "w", encoding = "latin1")
        f.write(sentences)
        f.close()
        user_dict = synonyms.build_semantic_descriptors_from_files(["sample_case.txt"])
        good = True
        for word in mandarin_dict.keys():
            if(not good):
                break
            values = mandarin_dict[word]
            for value in values.keys():
                try:
                    if(mandarin_dict[word][value] != user_dict[word][value]):
                        print("VALUES NOT MATCHING!")
                        print("WORD BEING INDEXED: ", word)
                        print("WORD NOT MATCHING: ", value)
                        print('\n')
                        print("Mandarin's Dict: ", values)
                        print("Your Dict: ", user_dict[word])
                        print('\n')
                        good = False
                        break
                except:
                    print("Something went wrong!")
                    print(f"An error occured when trying to index [{word}][{value}]")
                    print('\n')
                    good = False
                    break
        if(good):
            for word in user_dict.keys():
                if(not good):
                    break
                values = user_dict[word]
                for value in values.keys():
                    try:
                        if(mandarin_dict[word][value] != user_dict[word][value]):
                            print("VALUES NOT MATCHING!")
                            print("WORD BEING INDEXED: ", word)
                            print("WORD NOT MATCHING: ", value)
                            print('\n')
                            print("Mandarin's Dict: ", values)
                            print("Your Dict: ", user_dict[word])
                            print('\n')
                            good = False
                            break
                    except:
                        print("Something went wrong!")
                        print(f"An error occured when trying to index [{word}][{value}]")
                        print('\n')
                        good = False
                        break
        if(good):
            print("ALL GOOD!")
        else:
            print("Here's the sentences:")
            print(sentences)
            print("Here's Mrmandarin's dict:")
            print(mandarin_dict)
            print('\n')
            print("Here's YOUR dict:")
            print(user_dict)
        return good

    def continuous_check(self):
        print("To exit, just quit the program. Fuck user usability.")
        cnt = 0
        while(True):
            if(self.check()):
                cnt += 1
                print("Number of test cases passed: ", cnt)
            else:
                break
        print(f"Well, you passed {cnt} cases...")

    def continuous_cosine(self):
        cnt = 0
        good = True
        while(good):
            sentences = self.network.get_sentences()
            mandarin_dict = self.network.get_dict()
            mandarin_cos = self.network.get_cos()
            #print(mandarin_dict)
            #print(mandarin_cos)
            words = mandarin_dict.keys()
            for word1 in words:
                if(good):
                    for word2 in words:
                        if(word2 in mandarin_cos[word1].keys()):
                            if(round(mandarin_cos[word1][word2], 5) != round(synonyms.cosine_similarity(mandarin_dict[word1], mandarin_dict[word2]), 5)):
                                print("SOMETHING DOESN'T MATCH!")
                                print(f"Cosine Similarity for {word1} and {word2} don't match!")
                                print('\n')
                                print("MRMANDARIN'S VALUE:", mandarin_cos[word1][word2])
                                print("YOUR VALUE:", synonyms.cosine_similarity(mandarin_dict[word1], mandarin_dict[word2]))
                                print('\n')
                                print("DICT1: ", mandarin_dict[word1])
                                print("DICK2: ", mandarin_dict[word2])
                                good = False
                                break
                else:
                    break
            if(good):
                cnt += 1
                print(f"Successful matches: {cnt}")

    def continuous_run(self):
        good = True
        cnt = 0
        print('\n')
        while(good):
            sentences = self.network.get_sentences()
            f = open("sample_case.txt", "w", encoding = "latin1")
            f.write(sentences)
            f.close()
            mandarin_dict = self.network.get_dict()
            get_tests = self.network.get_tests()
            f = open("sample_test.txt", "w", encoding = "latin1")
            f.write(get_tests)
            f.close()
            result = synonyms.run_similarity_test("sample_test.txt", synonyms.build_semantic_descriptors_from_files(["sample_case.txt"]), synonyms.cosine_similarity)
            if(int(result) != 100):
                print("HMMM SOMETHING SEEMS TO BE OFF")
                print("Can't really pinpoint why tbh but I'll provide you with the debugging info tho...")
                print('\n')
                print("Checkout sample_case.txt made in your folder for the sentences used")
                print("Checkout sample_test.txt for the testing of run_similarity_test (also in your folder now)")
                print('\n')
                print("Here's my dict if that helps: ")
                print(mandarin_dict)
                good = False
            else:
                cnt += 1
                print("Cases passed: ", cnt)
root = client()
root.run()
