# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import os
import random
import re
import sys
from collections import deque

## for each attempt and each password, remove all matching occurrences and return result
def removePassword(password, loginAttempt):
    #print("+removing ", password, " from ", loginAttempt)
    result = loginAttempt.replace(password, "")
    #print("+tmp result: *", result, "*")
    return result

def removeAllPasswords(passwords, loginAttempt):
    final_result = ""
    tmp_result = ""
    found_password = []
    for password in passwords:
        password = password.replace('\n', "")
        tmp_result = removePassword(password, loginAttempt)
        if tmp_result != loginAttempt:
            found_password.append(password)
            #print("found ", password)
            #print("now found password list: ", found_password, " which has length ", len(found_password))
        else:
            #print("did not find ", password)
            pass
        #final_result.append(tmp_result)
        final_result = final_result + tmp_result + "\n"
        loginAttempt = tmp_result
    if len(loginAttempt) != 0:
        #print("removing found passwords because remaining login was: *", loginAttempt, "* which has a length of ", len(loginAttempt))
        found_password = []
    return found_password

def rotatePasswords(passwords, loginAttempt, attemptNum):

    passwordsq = deque(passwords)
    # from collections import deque
    # items = deque([1, 2])
    # items.append(3)        # deque == [1, 2, 3]
    # items.rotate(1)        # The deque is now: [3, 1, 2]
    passwordsq.rotate(1)
    foundPasswords = removeAllPasswords(passwordsq, loginAttempt, attemptNum)
    for i in range(len(passwords)):
        if len(foundPasswords) == 0:
            passwordListTry = passwordsq.rotate(1)
            foundPasswords = (passwordListTry, loginAttempt, attemptNum)
        else:
            break
    return foundPasswords

def findPasswordOrder(passwords, loginAttempt):
    finalOrder = []
    indexHash = {}
    for password in passwords:
        passwordIndex = re.finditer(password, loginAttempt)
        for pi in passwordIndex:
            #print("password ", password, "found at index", pi.start())
            indexHash[pi.start()] = password
    orderedIndexList = sorted(indexHash.keys())
    for oi in orderedIndexList:
        finalOrder.append(indexHash[oi])
    # d_swap = {v: k for k, v in d.items()}
    return finalOrder

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
    tmp_result = removeAllPasswords(passwords, loginAttempt)
    if len(tmp_result) != 0:
        final_result = " ".join(findPasswordOrder(tmp_result, loginAttempt))
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
