# # program to demonstrate run length encoding and decoding of string
# # aaabbbcddefff

import string

def run_length_encode(string):

	current_char = string[0]
	count = 0
	result = ""
	for s in string:
		if current_char == s:
			count += 1
		else:
			result += str(count) + current_char
			current_char = s
			count = 1

	result += str(count) + current_char

	return result 

def run_length_decode(my_string):
	dig = ""
	result = ""
	for letter in my_string:
		if not letter.strip(string.digits):
			dig += letter
		else:
			for i in range(int(dig)):
				result += letter
				dig = ""
	return result

my_string = run_length_encode("aaabbbcddefffhi")
print(my_string)



print(run_length_decode(my_string))


