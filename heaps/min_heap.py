
from heap import *

class MinHeap(Heap):

	def __init__(self):
		super().__init__()

	def insert(self, el):
		if not self.is_full():
			self._count += 1
			self._data.insert(self._count, el)
			self.sift_up(self._count)

		else:
			raise HeapFullException('Error : heap is full')

	def delete(self):

		if not self.is_empty():
			temp = self._data[0]
			self._data[0] = self._data[self._count - 1]
			self.sift_down(0)
			self._count -= 1
			return temp
		else:
			raise HeapEmptyException('Error : heap is empty')
			
	def get_highest_priority(self):
		if not self.is_empty():
			return self._data[0]
		else:
			raise HeapFullException('Error : heap is full')

	def sift_up(self, index):
		parent_index = self.get_parent(index)
		el = self.get_at_index(index)

		if parent_index != -1:
			parent = self.get_at_index(parent_index)
			if parent > el:
				self.swap(index, parent_index)
				self.sift_up(parent_index)

	def sift_down(self, index):
		left_index = self.get_left_child(index)
		right_index = self.get_right_child(index)

		if left_index == -1 and right_index == -1: 
			return

		else:
			left = self.get_at_index(left_index)
			el = self.get_at_index(index)
			min_index = index

			if right_index == -1:
				if left < el: 
					min_index = left_index
					
			else:
				min_index =  left_index if (left < self.get_at_index(right_index)) else right_index

			self.swap(min_index, index)

def main():
	min_heap = MinHeap()

	for i in (3, 2, 1):
		min_heap.insert(i)

	print('the element is : %d'%(min_heap.delete()))
	print(min_heap.get_highest_priority())
	print('the element is : %d'%(min_heap.delete()))
	print(min_heap.get_highest_priority())
	print('the element is : %d'%(min_heap.delete()))
	# print(min_heap.get_highest_priority())
	

if __name__ == '__main__':
	main()