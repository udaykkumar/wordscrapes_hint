#!/usr/bin/python
# -*- coding: utf-8 -*-


from itertools import permutations


def load():
    wdict = {}
    #f = open('./english-words/words_alpha.txt', 'r')
    f = open('dictionary.txt', 'r')
    for word in f:
         wdict[  str(word.lower().strip()) ] = word.lower().strip()
    return wdict

def permute(word, wsize):
    finallist = []
    print "Loading dictionary "
    wordsDict= load()
    print "Loading dictionary Done size ", len( wordsDict )
    #print wordsDict

    print "Searching for possible permutations of word " , word , " for size ", wsize
    permList = permutations(word, wsize);
    for perm in list(permList):
        lowerword = (''.join(perm));
        lowerword = str(lowerword.lower());
        if lowerword in wordsDict.keys() :
            print "Found Something in dictionay ", lowerword
            finallist.append( lowerword )
        #else :
        #    print "Found Nothing in dictionay ", lowerword

    return finallist

def main():
    word="EEITRH"
    wordsize=4
    matchinglist = permute( word, wordsize)
    matchinglist = list(dict.fromkeys( matchinglist  ))
    for w in matchinglist:
        if w[1] == 'e' and w[3] == 'e':
            print w

if __name__ == "__main__":
    # execute only if run as a script
    main()
