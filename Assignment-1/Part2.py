#!/usr/bin/env python3  
# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : Stephanie Yen
# Created Date: March 2022
# version ='1.0'
# ---------------------------------------------------------------------------
""" PART 2: ARRAYS & STRINGS
    Functions that perform operations on array and string inputs, and respective tests """  

def isStringPermutation(s1, s2): 
    ''' Takes in two Strings, returns a Boolean denoting whether the first is a permutation of the second. '''
    
    # Sanity checks
    if (s1 is None) or (s2 is None):
        return None # assumption
    if (len(s1) != len(s2)): # permutations must be of the same length
        return False

    # Iterate over s1 to store the freq of every char in a dictionary
    charFreqDict = {}
    for c in s1:
        charFreqDict[c] = charFreqDict.get(c, 0) + 1    # increment freq

    # Iterate over s2 to verify whether every char in s1 is present in s2
    for c in s2:
        if c in charFreqDict: # c is in s1 at least one time
            charFreqDict[c] = charFreqDict.get(c) - 1    # decrement freq if found
            if (charFreqDict.get(c) == 0):
                del charFreqDict[c] # remove c from the hash map when all occurrences have been found
        else: # there is a char in s2 that does not exist in s1
            return False

    # The length of charFreqDict should be 0
    return True

def pairsThatEqualSum(inputArray, targetSum):
    ''' 
    Returns an array of pairs where each pair contains two numbers from the input array and
    the sum of each pair equals the target integer.

        Parameters: 
            inputArray (list): Array of integers
            targetSum (int): Target number
        
        Returns: 
            (list): Array of pairs that sum to targetSum 
    ''' 
    targetDict = {} 
    pairs = [] 

    # Iterate over inputArray to map each value to its addend (to get targetSum)
    for i in range(len(inputArray)): 
        targetDict[inputArray[i]] = targetSum - inputArray[i]

    # Iterate over inputArray to find each possible pair
    for i in range(len(inputArray)): 
        targetNumber = targetDict.get(inputArray[i])
        if targetNumber in inputArray:
            if (targetNumber, inputArray[i]) not in pairs: # avoid duplicates (order does not matter)
                pairs.append((inputArray[i], targetNumber))
    
    return pairs


# ----- TESTS -----

def main(): 
    print("Testing isStringPermutation()")
    print(isStringPermutation("asdf", "fsda")) # True
    print(isStringPermutation("asdf", "fsa")) # False
    print(isStringPermutation("asdf", "fsax")) # False
    print(isStringPermutation("asdf", None))   # None
    print(isStringPermutation("", "")) # assume this should return True

    print("Testing pairsThatEqualSum()")
    print(pairsThatEqualSum([1, 2, 3, 4, 5], 5)) # [(1, 4), (2, 3)]
    print(pairsThatEqualSum([1, 2, 3, 4, 5], 1)) # []
    print(pairsThatEqualSum([1, 2, 3, 4, 5], 7)) # [(2, 5), (3, 4)]

if __name__ == "__main__": 
    main()