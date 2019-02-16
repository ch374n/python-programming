# program to implement queue using two stacks 
from stack import *

class Queue:
	"""class to implement queue using two stacks"""
	def __init__(self):
		self.stack_1 = Stack()
		self.stack_2 = Stack()

	def enqueue(self, node):
		if self.stack_2.is_empty():
			self.stack_1.push(node)
		else:
			el = self.stack_2.pop()
			while el is not None:
				self.stack_1.push(el)
				el = self.stack_2.pop()
			self.stack_1.push(node)

	def dequeue(self):
		if self.stack_1.is_empty():
			return self.stack_2.pop().get_data()
		else:
			el = self.stack_1.pop()
			while el is not None:
				self.stack_2.push(el)
				el = self.stack_1.pop()
			return self.stack_2.pop().get_data()
def main():
	queue = Queue()
	for i in range(10, 50, 10):
		queue.enqueue(Node(i))

	print(queue.dequeue())
	
main()



