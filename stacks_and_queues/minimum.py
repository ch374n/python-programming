# program to find out minimum element in stack at any instance

from stack import *

class MinimumStack:
	def __init__(self):

		self.stack_1 = Stack()
		self.stack_2 = Stack()

	def push(self, node):

		self.stack_1.push(node)

		obj = self.stack_2.peek()
		if obj is not None:
			if node.get_data() < obj.get_data():
				self.stack_2.push(node)
			else:
				self.stack_2.push(obj)
		else:
			self.stack_2.push(node)

	def pop(self):

		self.stack_2.pop()
		return self.stack_1.pop().get_data()

	def get_minimum(self):
		return self.stack_2.peek().get_data()

	def peek(self):
		return self.stack_1.peek().get_data()
def main():
	stack = MinimumStack()
	stack.push(Node(40))
	stack.push(Node(30))
	stack.push(Node(20))
	stack.push(Node(10))

	print(stack.get_minimum())
	print(stack.pop())
	print(stack.get_minimum())
	
main()

