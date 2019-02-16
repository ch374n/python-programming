# ----------------------------------------------------------------------------------------------------------------------------------------------------------

class Node:
	''' Implementation of Node '''
	def __init__(self, data):
		self.data = data
		self.next = None

	def set_next(self, node):
		self.next = node

	def get_next(self):
		return self.next
		
	def get_data(self):
		return self.data

# -------------LINKED LIST CLASS DEFINITION----------------------------------------------------------------------------------------------------------------

class Linkedlist:
	''' Implementation of singly linked list '''

	def __init__(self, head):
		self.head = head
		
	def add_node(self, node):
		if not self.head:
			self.head = node
		else:
			cursor = self.head
			while cursor.get_next():
				cursor = cursor.get_next()
			cursor.set_next(node)

	def iterate(self):
		''' Method to iterate over each element of linked list '''
		if not self.head:
			return
		else:
			cursor = self.head
			while cursor:
				print("%d ---> "%(cursor.get_data()), end ='\t')
				cursor = cursor.get_next()
			print('\n')

	def get_length(self):
		''' Method to get count of elements in the linked list '''
		counter = 0
		if not self.head:
			return counter
		else:
			cursor = self.head
			while cursor:
				counter += 1
				cursor = cursor.get_next()
			return counter 

	def get_nth(self, n):
		''' Method to get nth element in the linked list '''
		if not self.head:
			return None
		else:
			if self.get_length() < n:
				return None
			else:
				cursor = self.head
				for counter in range(n - 1):
					cursor = cursor.get_next()
				return cursor

	def insert(self, data, position):
		''' Method to insert data at any location in linked list '''
		if self.get_length() + 1 < position:
			return

		if position == 0:
			self.head = data

		else:
			node = self.get_nth(position - 1)
			cursor = node.get_next()
			node.set_next(data)
			node.get_next().set_next(cursor)			

	def insert_sorted(self, data):
		''' Method to insert data in sorted linked list '''
		if not self.head:
			self.head = data
		else:
			cursor = self.head
			prev   = None
			while cursor and cursor.get_data() < data.get_data():
				prev = cursor 
				cursor = cursor.get_next()
			prev.set_next(data)
			prev.get_next().set_next(cursor)

	def append_list(self, dest):
		''' Method to append second list at end of first list '''
		pass

	def front_back_split(self):
		''' Method to split list into two different linked list '''
		if not self.head:
			return None, None
		else:
			faster = self.head
			slower = self.head
			while faster:
					faster = faster.get_next()
					if not faster:
						break
					faster = faster.get_next()
					if faster:
						slower = slower.get_next()
			list2 = slower.get_next()
			slower.set_next(None)
			return Linkedlist(self.head), Linkedlist(list2)

	def remove_duplicates(self):
		''' Method to remove duplicates from sorted list '''
		if not self.head:
			return None
		else:
			back = self.head
			front = back.get_next()
			while front:
				if back.get_data() == front.get_data():
					back.set_next(front.get_next())
					front.set_next(None)
					front = back.get_next()
					continue
				back  = back.get_next()
				front = front.get_next()

	def merge_lists(self, list1, list2):
		'''  Method to merge two sorted list '''
		if not list1 and not list2:
			return None

		if not list1:
			return list2

		elif not list2:
			return list1

		else:
			if(list1.head.get_data() < list2.head.get_data()):
				cursor = list1.head
				q = list2.head
			else:
				cursor = list2.head
				q = list1.head
			temp = cursor
			p = cursor.get_next()
			while q and p:
				if q.get_data() < p.get_data():
					cursor.set_next(q)
					q = q.get_next()
				else:
					cursor.set_next(p)
					p = p.get_next()
				cursor = cursor.get_next()

			while q:
				cursor.set_next(q)
				q = q.get_next()
				cursor = cursor.get_next()

			while p:
				cursor.set_next(p)
				p = p.get_next()
				cursor = cursor.get_next()

		return Linkedlist(temp)				

	def reverse_list(self): 
		''' method to reverse singly linked list using iterative approach '''
		if not self.head or not self.head.get_next():
			return self.head
		else:
			front = self.head 
			back  = None
			temp  = front.get_next()

			while True:
				front.set_next(back)
				back = front
				front = temp
				if not front:
					break
				temp = temp.get_next()
			self.head = back

# ----------MAIN METHOD-------------------------------------------------------------------------------------------------------------------

def main():

	my_list = Linkedlist(Node(10))
	my_list.add_node(Node(20))
	my_list.add_node(Node(30))
	my_list.add_node(Node(40))
	my_list.add_node(Node(50))
	my_list.add_node(Node(60))
	my_list.iterate()
	# print('The length of linked list is : %d'%(my_list.get_length()))
	# print('second element of linked list is : %d'%(my_list.get_nth(3).get_data()))
	# my_list.insert(Node(10), 6)
	# my_list.iterate()

	# my_list.insert_sorted(Node(14))
	# my_list.iterate()


	# list1, list2 = my_list.front_back_split()
	# print('List 1 : ')
	# list1.iterate()
	# print('List 2 : ')
	# list2.iterate()

	# my_list.remove_duplicates()
	
	# list3 = my_list.merge_lists(list1, list2)
	# list3.iterate()

	print(Linkedlist.reverse_list.__doc__)
	my_list.reverse_list()
	my_list.iterate()

# -----------------------------------------------------------------------------------------------------------------------------

main()

