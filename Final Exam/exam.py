'''I pledge my honour that I am submitting the exam no more than three hours after I first looked at the exam questions.'''
'''Start Time: 11am Local time (EST+8, GMT+3), Expected End time: 2pm Local time'''

# ESn180 Final Examination, Fall 2020
#
# Aids allowed: the ESC180 website, a Python IDE. You must *not* use any other
# notes or internet website. You may must not communicate about the exam except
# to ask questions on Piazza.
#
# You may ask questions on the course Piazza. Please make your question private
# if it must disclose part of the solution. Otherwise, please make it public.
# Please check Piazza occasionally in case there are announcements or
# clarifications.
#
# You have 2.5 hours to work on the exam, and 30 minutes to submit it. You may
# keep writing the exam during the submission window, but it is your
# responsibility to make sure that the exam is submitted before the submission
# window closes. Late submissions will only be accepted from students who
# have been preapproved for a time extension through accessibility services.
#
# To be eligible to receive partial credit, you must submit a file which does
# not produce an error when read into Python. Any code that you know produces
# errors must be commented out. By themselves, comments/docstrings will not
# earn any points. However, they may help TAs in deciding how to award
# partial credit.
#
# Unless otherwise specified, you may import math and numpy, but not other
# modules.
#

################################################################################

#    Problem 1 (25 pts)
#
#    Up to 5 points will be awarded for making progress toward a correct
#    solution.
#
#    Assume you are given a list of filenames of text files. Assume
#    that the text files only contain the punctuation
#    [".", ",", "!", "?", "-"].
#    The files may also contain the newline character "\n".
#
#    For each file, there is a word that occurs in that file the most often --
#    the most frequent word. We want to find the word that is the most frequent
#    word in the most files.
#    Write a function that takes in a list of file names, and returns the word
#    that is the most frequent word in the most files. You can assume that there
#    are no ties: each file has one word that is the most frequent, and there
#    is one word that is the most frequent word in the most files.
#    For example, the function might be called as follows:
#
#    most_common_frequent_word(["diseases/" + filenames[0],
#                                "diseases/" + filenames[1],
#                                "diseases/" + filenames[2])
#    If the most frequent word in filesnames[0] is "a", the most frequent word in
#    filenames[1] is "the", and the most frequent word in filenames[2] is
#    "the", most_common_frequent_word should return "the"                               .
#    A non-word, such as "<a", would be considered a valid word for the files
#    given to you.
#
#    The words "Dog" and "dog" should be considered to be the same when computing
#    the frequency of words. The words "dogs" and "dog" should be considered
#    to be different.
#
#    You are encouraged to use helper functions.
#
#    For this problem, you may *not* import any Python modules.

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

################################################################################

#    Problem 2 (20 pts)
#
#    This problem will be auto-graded.
#
#
#    Recall that links in an html file are given in the format
#    <a href = "http://engsci.utoronto.ca">EngSci homepage</a>
#    Write a function that takes in the text of an html file, and returns a dictionary
#    whose keys are the link texts (e.g. "EngSci homepage") and whose values are
#    the corresponding URLs (e.g., "http://engsci.utoronto.ca"). You can assume
#    that link texts do not repeat.
#    Sample call:
#     get_links('<a href = "http://engsci.utoronto.ca">EngSci homepage</a>')
#    should return {"EngSci homepage": "http://engsci.utoronto.ca"}


def get_links(html_text):
    html_slices = []
    for i in range(2, len(html_text)):
        if html_text[i - 2: i] == "<a":
            j = i
            while html_text[j - 2 : j] != "a>":
                j += 1
            html_slices.append(html_text[i - 2: j])
            j = 0
    links = {}
    for i in range(len(html_slices)):
        link = ""
        name = ""
        for j in range(2, len(html_slices[i])):
            if html_slices[i][j - 2: j] == "= ":
                k = j
                while html_slices[i][k] != ">":
                    k += 1
                link += html_slices[i][j + 1 : k - 1]
                j = k + 1
                k = 0
            if html_slices[i][j] == ">":
                k = j
                while html_slices[i][k - 3: k] != "</a":
                    if k + 1 < len(html_slices[i]):
                        k += 1
                name += html_slices[i][j + 1 : k - 3]
                j = k + 1
                k = 0
        links[name] = link
        link = ""
        name = ""
    return links
print(get_links('<a href = "http://engsci.utoronto.ca">EngSci homepage</a> blah blah <b> bleep bleep bloop bloop ignore me<\b> <a href = "http://ece.utoronto.ca">ECE homepage</a>'))
    

###############################################################################

#   Problem 3 (10 pts)
#
#    Without using for-loops or while-loops, write  function for which
#    the tight asymptotic bound on the runtime complexity is O((n^2)*log(n)).
#    You may create helper functions, as long as they also do not use while-
#    and for-loops.
#    Justify your answer in a comment. The signature of the function must be
''' Start of Q3 sol'''
L = [6, 5, 4, 3, 2, 1]
#lets say that len(L) = n

def f(n):
    global L
    if n == 0:
        return False
    L = sorted(L) #O(nlogn) since I presume that python's built in sorting uses mergesort
    m = L[n] 
    if n == m:
        return True
    elif n != m:
        f(n - 1)
'''
    This function essentially checks whether a range of numbers from n - 0 is in a list, L. 
    With each run, it decreases n, and searches the next largest element to try and find a match.
    Sorted takes nlogn time. If this were to run once, then it would simply be nlogn. 
    However, I'm making this program run n-times, searching the entire list
    for the factorial. In the worst case, the factorial simply isn't there and thus, f must run n times. Therefore, 
    overall, it has tight asymptotic bound of O((n*nlog(n))
'''
''' End of Q3 sol'''
###############################################################################
###############################################################################
#  Problem 4 (15 pts)
#
#  This problem will be auto-graded.
#
#
#  It is possible to combine the numbers 1, 5, 6, 7 with arithemtic operations
#  to get 21 as follows: 6/(1-5/7).
#
#  Write a function that takes in a list of three numbers and a target number, and
#  returns a string that contains an expression that uses all the numbers
#  in the list once, and results in the target. Assume that the task is possible
#  without using parentheses.
#
#  For example, get_target_noparens([3, 1, 2], 7) can return "2*3+1" or "1+2*3"
#  (either output would be fine).
#
# I cant think of any other way other than brute forcing this with combinations
# First try and rule out some basics such as operations where theyre all the same such as all addition and all
# subtraction and so on. Then go into individual combinations for each possible result and this is doable by hand since theyre's only
# 3 of them.
def get_target_noparens(nums, target):
    oper = ["+", "-", "*", "/"]
    v1 = 0
    v2 = 0

    if len(nums) == 1:
        if nums[0] == target:
            return target
    elif sum(nums) == target:
        return str(str(nums[0]) + "+" + str(nums[1]) + "+" + str(nums[2]))
    elif nums[0] * nums[1] * nums[2] == target:
        return str(str(nums[0]) + "*" + str(nums[1]) + "*" + str(nums[2]))
    #math.prod threw an error but it works fine in my code. What do?
    elif nums[0] - nums[1] - nums[2] == target:
        return str(str(nums[0]) + "-" + str(nums[1]) + "-" + str(nums[2]))
    elif nums[0] / nums[1] / nums[2] == target:
        return str(str(nums[0]) + "/" + str(nums[1]) + "/" + str(nums[2]))
    else:
        # There are at most 2 operations for each expression. Therefore, you can decompose it into v1 (op2)  v2
        # v1 = (one of 3 nums) (op1) (another one of 3 nums)
        # to generate v1, need to have 3 nested for loops, which run combinations with various operations (op1)
        # then repet and check the same for each possible v1 with the remaining number and any of the other operations
        for n1 in nums:
            for n2 in nums:
                for n3 in nums:
                    if n1 != n2 and n2 != n3 and n3 != n1:
                        for op1 in oper:
                            if op1 == "+":
                                v1 = n1 + n2
                                for op2 in oper:
                                    if op2 == "+":
                                        v2 = v1 + n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "-":
                                        v2 == v1 - n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "*":  
                                        v2 = v1 * n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "/":
                                        v2 = v1 / n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                            elif op1 == "-":
                                v1 == n1 - n2
                                for op2 in oper:
                                    if op2 == "+":
                                        v2 = v1 + n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "-":
                                        v2 == v1 - n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "*":
                                        v2 = v1 * n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "/":
                                        v2 = v1 / n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                            elif op1 == "*":
                                v1 = n1 * n2
                                for op2 in oper:
                                    if op2 == "+":
                                        v2 = v1 + n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "-":
                                        v2 == v1 - n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "*":
                                        v2 = v1 * n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "/":
                                        v2 = v1 / n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                            elif op1 == "/":
                                v1 = n1/n2
                                for op2 in oper:
                                    if op2 == "+":
                                        v2 = v1 + n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "-":
                                        v2 == v1 - n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "*":
                                        v2 = v1 * n3 
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))
                                    elif op2 == "/":
                                        v2 = v1 / n3
                                        if v2 == target:
                                            return str(str(n1) + str(op1) + str(n2) + str(op2) + str(n3))

################################################################################
#  Problem 5 (15 pts)
#
#  Up to 3 pts will be awarded for making progress toward a solution.
#
#  Now, write the function get_target which returns a string that contains an
#  expression that uses all the numbers in the list once, and results in the
#  target. The expression can contain parentheses. Assume that the task is
#  possible.
#  For example, get_target([1, 5, 6, 7], 21) can return "6/(1-5/7)"

def get_target(nums, target):
    out = ""

    product = 1
    for num in nums:
        product *= num

    if len(nums) == 1:
        if nums[0] == target:
            return nums[0]

    if sum(nums) == target: #can do this since addition and multiplication are commutative so order does not matter
        for i in range(len(nums)):
            if i == 0:
                out += str(nums[i])
            else:
                out +=  "+" + str(nums[i])
        return out 
    elif product == target: 
        for i in range(len(nums)):
            if i == 0:
                out += str(nums[i])
            else:
                out +=  "*" + str(nums[i])
        return out

    elif len(nums) == 2:
        if nums[1] - nums[0] == target:
            return str(str(nums[1]) + "-" + str(nums[0]))
        elif nums[0] - nums[1] == target:
            return str(str(nums[0]) + "-" + str(nums[1]))
        elif nums[1] / nums[0] == target:
            return str(str(nums[1]) + "/" + str(nums[0]))
        elif nums[0] / nums[1] == target:
            return str(str(nums[0]) + "/" + str(nums[1]))

    elif len(nums) == 3:
        return get_target_noparens(nums, target)

''' 
    To go beyond this, we can use the exec() function like prof once showed us to find
    all possible combinations of letters. In this case, we'd do arithmetic operations.
    This would basically be Q4 but in exec form.
'''
################################################################################

