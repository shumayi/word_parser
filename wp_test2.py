#
# wp_test.py
#
# Test Module for word_parser class

from wp import *

if __name__ == "__main__":

	file_name = raw_input("Please enter the input file name with .txt extension: ")

	# Open the read file
	with open(file_name, 'r') as rf:
		file_data = rf.read().strip().split('\n')

	print "The parsed sentence(s): "

	for data in file_data:
		parser = Parser(data)

		result = parser.word_parser()

		with open(file_name + '_output.txt', 'a') as wf:
			wf.write(result + '\n')

		print result
		print 