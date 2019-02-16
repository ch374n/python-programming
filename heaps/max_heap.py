
from heap import *

class MaxHeap(Heap):

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
			self._data[0] = self._data[self._count]
			# self.sift_down(0)
			self.percolate_down(0)
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
			if parent < el:
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
			max_index = index

			if right_index == -1:
				if left > el: 
					max_index = left_index
					
			else:
				max_index =  left_index if (left > self.get_at_index(right_index)) else right_index

			self.swap(max_index, index)

	def percolate_down(self, parent_index):
			left_index = self.get_left_child(parent_index)
			right_index = self.get_right_child(parent_index)
		
			if left_index == -1 and right_index == -1:
				return 

			else:
				left = self.get_at_index(left_index)
				el = self.get_at_index(parent_index)
				max_index = parent_index

				if right_index == -1:
					if left > el: 
						max_index = left_index
						
				else:
					max_index =  left_index if (left > self.get_at_index(right_index)) else right_index

				self.swap(max_index, parent_index)
				
			if left_index != -1:
				self.percolate_down(left_index)

			if right_index != -1:
				self.percolate_down(right_index)

	def sort_data(self):
		result = []
		while self._count >= 0:
			result.append(self.delete())

		return result

	def heap_sort(self):
		parent_index = self.get_parent(self._count)

		while parent_index >= 0:
			self.percolate_down(parent_index)
			parent_index -= 1

		print(self.sort_data())

	def printall(self): 
		for el in self._data:
			print(el)

def main():
	max_heap = MaxHeap()

	# for i in (3, 2, 1):
	# 	max_heap.insert(i)
	max_heap.set_data([1, 2, 3, 4, 5, 6, 11])

	max_heap.heap_sort()

if __name__ == '__main__':
	main()


	