
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



	def depth_first(self, root):
		if root is None:
			return 
		else:
			self.depth_first(root.get_left())
			print('%c ->'%(root.get_data()))
			self.depth_first(root.get_right())

	def breadth_first(self):
		queue = CircularQueue()

		if self.root is None:
			return

		else:
			queue.enqueue(self.root)
			while not queue.is_empty():
				node = queue.dequeue()
				print(node.get_data())
				if not node.get_left():
					queue.enqueue(node.get_left())
				if not node.get_right():
					queue.enqueue(node.get_right())

	def mirror_tree(self):
		"""method to mirror all nodes of a tree"""


	def minimum_value(self):
		"""method to find minimum value in binary tree"""
		if not self.root:
			return
		else:
			cursor = self.root
			while cursor.get_left():
				cursor = cursor.get_left()

			return cursor.get_data()

	def find_depth(self, root):
		"""method to find depth of binary tree"""
		if not self.root:
			return 0
		elif not self.root.get_left() and not self.root.get_right():
			return 0		
		else: 
			l = self.find_depth(root.get_left()) + 1
			r = self.find_depth(root.get_right()) + 1
			return max(l, r)

def main():
	tree = BinaryTree(Node('C'))
	
	tree.add_node(tree.get_root(), Node('D'))	
	tree.add_node(tree.get_root(), Node('B'))	
	# tree.add_node(tree.get_root(), Node('D'))	
	# tree.add_node(tree.get_root(), Node('E'))	
	# tree.add_node(tree.get_root(), Node('F'))	
	# tree.add_node(tree.get_root(), Node('G'))	

	# tree.depth_first(tree.get_root())
	tree.breadth_first()
	# print(tree.minimum_value())
	# print(tree.find_depth(tree.get_root()))

main()