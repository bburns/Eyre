
"""
eyre.py
Analyze characters and places in stories.
Author: Brian Burns <bburns.km@gmail.com>
Date: 2014-02-27
"""

import sys
import string
import re

inputfile = "ghost.txt"
allow = string.letters
dictfile = "linuxwords.txt"


def readWords(filename):
    
    "Read unique words from a file"
    
    wordset = set()
    #. handle errors - with open(filename, 'r') as f: for line in f: 
    f = open(filename, 'r')
    for line in f.readlines():
        line = line.strip()
        line = line.lower()
        line = re.sub('[^%s ]' % allow, '', line)
        words = line.split()
        for word in words:
            wordset.add(word)
    words = list(wordset)
    words.sort()
    return words

    
def main():
    
    "Main entry point"

    # get unique words
    print 'reading text...'
    words = readWords(inputfile)
    print words[0:5]
    print
    
    # get dictionary words
    print 'reading dictionary...'
    dictionary = readWords(dictfile)
    print dictionary[0:5]
    print
    dictionary = set(dictionary) # make a hash
    
    # get words not in dictionary
    print 'extracting names (and misspellings)...'
    names = []
    for word in words:
        if word not in dictionary:
            names.append(word)
    print names
    print
    

if __name__ == '__main__':
    ret = main()
    sys.exit(ret)

