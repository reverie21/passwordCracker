# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import os
import random
import re
import sys
import time
from collections import deque
from itertools import permutations

## for each attempt and each password, remove all matching occurrences and return result
def addPassword(test_password, loginAttempt, test_index):
    result = ""
    pword_len = len(test_password)
    if test_index + pword_len < len(loginAttempt)+1 and test_password == loginAttempt[test_index : test_index+pword_len]:
        result = test_password
    return result

def deepCopy(myArray):
    newArray = []
    myArray = sorted(myArray, key=len, reverse=True)
    for val in myArray:
        if val != "":
            newArray.append(val)
    return newArray

def tryPassword(index, loginAttempt, foundArray, searchPasswords, allPasswords, mappedPwords, pwordIndex):
    print("\n\ncurrently at index ", index, "with foundArray ", foundArray)
    print("---looking for ", loginAttempt[index:index+5])
    print("---search array ( size ", len(searchPasswords),"): ", searchPasswords)
    match_count = 0
    if index == len(loginAttempt):
        return foundArray
    if len(searchPasswords) == 0:
        foundArray = []
    for pIndex, pword in enumerate(searchPasswords):
        if addPassword(pword, loginAttempt, index) != "":
            #print("> found ", pword, "with length ", len(pword))
            foundArray.append(pword)
            index += len(pword)
            currentPwordindex = allPasswords.index(pword)
            #searchPasswords = deepCopy(list(set(searchPasswords) | set(allPasswords[currentPwordindex:])))
            searchPasswords = deepCopy(allPasswords[pIndex:]) ## not correct!
            next_result = tryPassword(index, loginAttempt, foundArray, searchPasswords, allPasswords, mappedPwords, pIndex)
            match_count += 1
            #print("here! with index ", index, "and found array: ", foundArray, "and search params ", searchPasswords)
            break
    if match_count == 0:
        #print("len of found array is ", len(foundArray))
        if len(foundArray) > 0:
            last_match = foundArray.pop()
            index -= len(last_match)
            print("removing ", last_match, "from", searchPasswords)
            #print(len(searchPasswords))
            if len(searchPasswords) > 0 and last_match in searchPasswords:
                searchPasswords.remove(last_match)
            next_result = tryPassword(index, loginAttempt, foundArray, searchPasswords, allPasswords, mappedPwords, pwordIndex)
        else:
            foundArray = []
            #return []
    if "".join(foundArray) == loginAttempt:
        return foundArray
    else:
        return []

def findPasswords(passwords, loginAttempt):
    index = 0
    foundArray = []
    allPasswords = sorted(passwords, key=len, reverse=True)
    searchPasswords = sorted(passwords, key=len, reverse=True)
    mappedPwords = {}
    foundArray = tryPassword(index, loginAttempt, foundArray, searchPasswords, allPasswords, mappedPwords, 0)
    return foundArray


#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

def passwordCracker(passwords, loginAttempt):
    # Write your code here
    loginAttempt = loginAttempt.replace('\n', '')
    #print("passwords: ", passwords, "loginAttempt: ", loginAttempt)

    final_result="WRONG PASSWORD"
    tmp_result = findPasswords(passwords, loginAttempt)
    if len(tmp_result) != 0:
        final_result = " ".join(tmp_result)
        #final_result=" ".join(tmp_result)
    return final_result


def read_file(fname):
    fptr = open(fname, 'r')

    t = int(fptr.readline())

    for t_itr in range(t):
        #n = int(fptr.readline().strip())
        n = fptr.readline().strip()

        passwords = fptr.readline().strip().split()

        loginAttempt = fptr.readline()

        result = passwordCracker(passwords, loginAttempt)

        #fptr.write(result + '\n')
        print(result + '\n')

    fptr.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_file('input28a.txt') # input28a doesn't compile when deepCopy is set to index

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
