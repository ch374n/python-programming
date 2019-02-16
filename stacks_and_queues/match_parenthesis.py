# program to perform parenthesis matching using stack

from stack import *


def is_matching(s):
	"""method to find whether given parenthesis is matching or not"""
	paren_set = {'{', '(', '['}
	paren_map = {'}' : '{', ')' : '(', ']' : '['}

	paren_stack = Stack()

	for character in s:
		if character in paren_set:
			paren_stack.push(Node(character))
		else:
			temp = paren_stack.pop()
			if temp is not None:
				if temp.get_data() != paren_map[character]:
					return False
			else:
				return False

	return paren_stack.is_empty()			

def main():
	print(is_matching('{{{[()]}}}()'))

main()