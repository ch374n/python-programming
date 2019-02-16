# program to implement stack data structure using linked list 

from linked_list import *

class Stack:
	"""implementation of stack data structure"""
	MAX = 25
		
	def __init__(self):
		self.top = None
		self.counter = 0

	def push(self, node):
		"""method to push element onto stack"""
		if not self.is_full():
			if self.top is None:
				self.top = node
			else:
				node.set_next(self.top)
				self.top = node

			self.counter += 1


	def pop(self):
		"""method to pop element from the stack"""
		if not self.is_empty():
			temp = self.top
			self.top = self.top.get_next()
			self.counter -= 1
			return temp
		else:
			return None

	def peek(self):
		"""returns the top element of the stack"""
		return self.top

	def is_full(self):
		"""returns true if stack is full"""
		return self.size() == Stack.MAX

	def is_empty(self):
		"""returns true if stack is empty"""
		return self.size() == 0

	def size(self):
		"""returns size of stack"""
		return self.counter

def main():
	stack = Stack()
	stack.push(Node(20))
	stack.push(Node(30))
	stack.push(Node(40))
	stack.push(Node(50))

	print(stack.pop().get_data())
	print(stack.pop().get_data())
	print(stack.pop().get_data())
	
# main()