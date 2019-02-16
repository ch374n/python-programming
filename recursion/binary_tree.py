
from circular_queue import *

class Node:
	"""Node structure for a class"""

	def __init__(self, data):
		self.data  = data
		self.left  = None
		self.right = None
	
	def set_left(self, node):
		self.left = node

	def set_right(self, node):
		self.right = node

	def get_data(self):
		return self.data

	def get_left(self):
		return self.left

	def get_right(self):
		return self.right

class BinaryTree:
	"""class representing binary tree"""

	def __init__(self, root):
		self.root = root

	def get_root(self):
		return self.root

	def add_node(self, root, node):
		if self.root is None:
			self.root = node
		else:
			if root.get_data() == node.get_data():
				return
			else:
				if root.get_data() < node.get_data():
					if root.get_right() is None:
						root.set_right(node)
					else:
						self.add_node(root.get_right(), node)
				else:
					if root.get_left() is None:
						root.set_left(node)
					else:
						self.add_node(root.get_right(), node)



	def breadth_first(self):

		queue = CircularQueue()

		if self.root is None:
			return
		else:
			queue.enqueue(self.root)
			while not queue.is_empty():
				node = queue.pop()
				print('%d -->'%(node.get_data()))

				if node.get_left() is not None:
					queue.enqueue(node.get_left())

				if node.get_right() is not None:
					queue.enqueue(node.get_right())

def main():
	tree = BinaryTree(Node('A'))
	
	tree.add_node(Node('B'))	
	tree.add_node(Node('C'))	
	tree.add_node(Node('D'))	
	tree.add_node(Node('E'))	
	tree.add_node(Node('F'))	
	tree.add_node(Node('G'))	

	tree.breadth_first()

main()