
class HeapFullException(Exception):
	pass

class HeapEmptyException(Exception):
	pass

class Heap:
	MAX = 50
	def __init__(self):
		self._data = []
		self._count = -1;

	def set_data(self, data): 
		self._data = data
		self._count = 6

	def get_left_child(self, index):
		left_index = 2 * index + 1 
		if left_index > self._count: 
			return -1
		else:
			return left_index

	def get_right_child(self, index):
		right_index =  2 * index + 2 

		if right_index > self._count:
			return -1
		else:
			return right_index

	def get_parent(self, index):
		parent_index = (index - 1) // 2

		if parent_index < 0:
			return -1
		
		return parent_index

	def is_empty(self):
		return self._count == -1

	def is_full(self):
		return self._count == Heap.MAX

	def get_at_index(self, index): 
		return self._data[index]

	def sift_up(self, index):
		raise NotImplementedError('method not implemented')
		
	def sift_down(self, index):
		raise NotImplementedError('method not implemented')

	def swap(self, i, j): 
		self._data[i], self._data[j] = self._data[j], self._data[i]