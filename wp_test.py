#
# wp_test.py
#
# Test Module for word_parser class

from wp import *

if __name__ == "__main__":

    # sentence1 = 'I love you, smootie88but*I love/you more, Ice Cream'
    # sentence2 = 'The following is a list comprehension with so_on being\'s used as a short-cut just in the example to represent the actual remaining lists that you want to combine.'

    sentence = raw_input('Please enter the sentence you want to parse: ')

    parser = Parser(sentence)

    print "The parsed sentence: "
    print parser.word_parser()
