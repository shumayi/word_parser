#
# word_parser.py
#
# PP 1.4: In the programming language of your choice, write a program that 
# parses a sentence and replaces each word with the following: first letter, 
# number of distinct characters between first and last character, and last letter.  
# For example, Smooth would become S3h.  Words are separated by spaces or 
# non-alphabetic characters and these separators should be maintained in their 
# original form and location in the answer.

import re

class Parser(object):

    def __init__(self, string = ''):
        """ Initializes a string object """
        self.__string = string

    def convert_string(self, word_arr):
        """ 
            Replace each word with the following parse format:
            first letter, number of distinct characters between 
            first and last character, and last letter.
        """
        parsed = []

        for i in word_arr:
            if len(i) < 3:
                parsed.append(i)
            elif len(i) == 3:
                i = i[0] + '1' + i[-1]
                parsed.append(i)
            else:
                letter = set(i[1:-1])
                i = i[0] + str(len(letter)) + i[-1]
                parsed.append(i)

        return parsed

    def word_parser(self):
        """
            Parse the given sentence into the format that we wanted
        """
        sentence = self.__string
        word_arr = []
        separator_arr = []
        parsed_string = []

        # Use regex to get the words
        word_arr = re.findall(r"[a-zA-Z_]+", sentence)

        # Parse the words to the format that we wanted
        word_arr = self.convert_string(word_arr)

        # Use regex to get the separators
        separator_arr = re.findall(r"[^a-zA-Z_]+", sentence)

        word_arr_len = len(word_arr)
        separator_arr_len = len(separator_arr)

        # If the sentence begins with a word, we append the word elements first,
        # then follow by a separator, keep doing this until we reach the end of the list
        if sentence[0].isalpha():
            for a, b in zip(word_arr, separator_arr):
                parsed_string.append(a + b)

            if word_arr_len > separator_arr_len:
                parsed_string.append(word_arr[-1])
            elif word_arr_len < separator_arr_len:
                parsed_string.append(separator_arr[-1])

        # If the sentence begins with a seperator, we append the seperator element first,
        # then follow by a word, keep doing this until we reach the end of the list
        else:
            for a, b in zip(word_arr, separator_arr):
                parsed_string.append(b + a)

            if word_arr_len > separator_arr_len:
                parsed_string.append(word_arr[-1])
            elif word_arr_len < separator_arr_len:
                parsed_string.append(separator_arr[-1])

        return ''.join(parsed_string)