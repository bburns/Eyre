
"""
eyre.py
Analyze characters and places in stories.
Author: Brian Burns <bburns.km@gmail.com>
Date: 2014-02-27
"""

import sys
import string
import re
print string.letters

inputfile = "alice.txt"
allowed = string.letters
# allowed = string.letters + " '\\-"
dictfile = "linuxwords.txt"

# regexp = "[^%s][^ %s]" % (string.letters, allowed)



def readWords(filename, lower=True):
    
    "Read unique words from a file"
    
    wordset = set()
    #. handle errors - with open(filename, 'r') as f: for line in f: 
    f = open(filename, 'r')
    for line in f.readlines():
        line = line.strip()
        if lower: line = line.lower()
        line = re.sub('[^%s ]' % allowed, '', line)
        # line = re.sub(regexp, '', line)
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
    # words = readWords(inputfile, False)
    print words[0:5]
    print
    
    # get dictionary words
    print 'reading dictionary...'
    dictionary = readWords(dictfile)
    # dictionary = readWords(dictfile, False)
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

