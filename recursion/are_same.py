# program to find out whether two binary trees are similar or not

from binary_tree import *

 
def are_same(root_1, root_2):
	if root_1 is None and root_2 is None:
		return True

	if root_1 is None and root_2 is not None:
		return False

	if root_1 is not None and root_2 is None:
		return False	

	else:
		if root_1.get_data() == root_2.get_data():
			return are_same(root_1.get_left(), root_2.get_left()) and are_same(root_1.get_right(), root_2.get_right())

	return False

def main():
	bin_1 = BinaryTree(Node('A'))
	bin_1.add_node(bin_1.get_root(), Node('B'))
	bin_1.add_node(bin_1.get_root(), Node('C'))
	bin_1.add_node(bin_1.get_root(), Node('D'))


	bin_2 = BinaryTree(Node('A'))
	bin_2.add_node(bin_2.get_root(), Node('B'))
	bin_2.add_node(bin_2.get_root(), Node('C'))
	bin_2.add_node(bin_2.get_root(), Node('D'))

	print(are_same(bin_1.get_root(), bin_2.get_root()))

main()