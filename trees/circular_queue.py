# rewriting circular_queue

class QueueOverflowException(Exception):
	pass

class QueueUnderflowException(Exception):
	pass

class CircularQueue:
	MAX = 5
	def __init__(self):
		self._front = -1
		self._rear  = -1
		self.data   = []

	def enqueue(self, el):
		if not self.is_full():
			if self._front == -1 and self._rear == -1:
				self._front, self._rear = 0, 0
			elif self._rear == CircularQueue.MAX - 1:
				self._rear = 0
			else:
				self._rear += 1
			self.data.insert(self._rear, el)
		else:
			raise QueueOverflowException('Queue is full...')

	def dequeue(self):
		if not self.is_empty():
			el = self.data[self._rear]
			if self._front == self._rear:
				self._front, self._rear = -1, -1
			elif self._front == CircularQueue.MAX - 1:
				self._front = 0
			else:
				self._front += 1
			return el
		else:
			raise QueueUnderflowException('Queue is empty...')

	def is_full(self):
		if self._front == 0 and self._rear == CircularQueue.MAX - 1:
			return True
		elif self._rear + 1 == self._front:
			return True
		else:
			return False

	def is_empty(self):
		if self._front == -1 and self._rear == -1:
			return True

def main():
	queue = CircularQueue()
	queue.enqueue(20)
	queue.enqueue(30)
	queue.enqueue(41)
	queue.enqueue(51)
	queue.enqueue(61)
	print(queue.dequeue())

if __name__ == '__main__':
	main()