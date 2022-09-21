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
    for val in myArray:
        newArray.append(val)
    return newArray

def tryPassword(index, loginAttempt, foundArray, searchPasswords, allPasswords):
    #print("currently at index ", index, "with foundArray ", foundArray)
    #print("---looking for ", loginAttempt[index:index+5])
    #print("---there are ", len(searchPasswords), "passwords to search (", len(allPasswords), "total)")
    match_count = 0
    if index == len(loginAttempt):
        return foundArray
    if len(searchPasswords) == 0:
        return []
    for pword in searchPasswords:
        if addPassword(pword, loginAttempt, index) != "":
            foundArray.append(pword)
            index += len(pword)
            searchPasswords = deepCopy(allPasswords)
            next_result = tryPassword(index, loginAttempt, foundArray, searchPasswords, allPasswords)
            match_count += 1
            break
            #time.sleep(5)
    if match_count == 0:
        if len(foundArray) > 0:
            last_match = foundArray.pop()
            index -= len(last_match)
            #print("removing ", last_match, "from", searchPasswords)
            if len(searchPasswords) > 0 and last_match in searchPasswords:
                searchPasswords.remove(last_match)
            next_result = tryPassword(index, loginAttempt, foundArray, searchPasswords, allPasswords)
            #time.sleep(2)
        else:
            return []
    return foundArray

def findPasswords(passwords, loginAttempt):
    index = 0
    foundArray = []
    allPasswords = sorted(passwords, key=len)
    searchPasswords = sorted(passwords, key=len)
    foundArray = tryPassword(index, loginAttempt, foundArray, searchPasswords, allPasswords)
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
    read_file('input19.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
