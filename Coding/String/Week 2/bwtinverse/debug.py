#!/usr/bin/env python
'''
A solution to a programming assignment for the Bioinformatics Algorithms (Part 1) on Coursera.
The associated textbook is Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The course is run on Coursera and the assignments and textbook are hosted on Stepic
Problem Title: Inverse Burrows-Wheeler Transform Problem
Assignment #: 10
Problem ID: B
URL: https://stepic.org/Bioinformatics-Algorithms-2/The-First-Last-Property-and-Inverting-the-Burrows-Wheeler-Transform-299/step/10
'''


def inverse_burrows_wheeler(bwt):
    '''Returns the inverse transform of the Burrows-Wheeler Transform bwt.'''

    # Enumerate the character order for repeat characters in the BWT and its sorted version.
    enumerated_bwt = enumerate_word(bwt)
    enumerated_sort = enumerate_word(sorted(bwt))
    enumerated_sort1 = sorted(enumerated_bwt)
    print(enumerated_bwt)
    print(enumerated_sort)
    #print(enumerated_sort1)

    # Construnct a mapping between the enumerated characters at each index of the enumerated BWT and sort.
    inverse_dict = {enumerated_bwt[i]:enumerated_sort[i] for i in range(len(bwt))}
    print(inverse_dict)
    # Construct the inverse BWT by a traversal through the inverse map.
    inverse_bwt = ''
    current_char = enumerated_bwt[0]
    for i in range(len(bwt)):
        current_char = inverse_dict[current_char]
        inverse_bwt += current_char[0]

    # Shift the inverse BWT back one to get the correct starting point (since the inverse must end in '$').
    return inverse_bwt[1:]+inverse_bwt[0]


def enumerate_word(word):
    '''
    Enumerates like characters in the order of their appearance for the given word.
    i.e. 'abcbba' returns ['a0', 'b0', 'c0', 'b1', 'b2', 'a1']
    '''

    # Initialize the character count and enumerated character list.
    char_count = {}
    enumerated = []

    # Enumerate like characters.
    for ch in word:
        if ch not in char_count:
            char_count[ch] = 0
        else:
            char_count[ch] += 1
        enumerated.append(ch+str(char_count[ch]))

    return enumerated


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    bwt = input()

    # Construct the Inverse Burrows-Wheeler Transform.
    inverse_bwt = inverse_burrows_wheeler(bwt)

    # Print and save the answer.
    print(inverse_bwt)

if __name__ == '__main__':
    main()
