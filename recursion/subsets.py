# program to find all possible subsets of a given set 
# {1, 2, 3}

def print_subsets(temp):
	if not all([el is None for el in temp]):
		print('{', end = '')
		for el in temp:
			if el is not None:
				print(el, end = ',')
		print('}')			


def find_subsets(arr, temp, pointer):
	if pointer > len(arr) - 1:
		print_subsets(temp)
	else:
		temp[pointer] = None
		find_subsets(arr, temp, pointer + 1)
		temp[pointer] = arr[pointer]
		find_subsets(arr, temp, pointer + 1)


find_subsets([1, 2, 3, 4, 5], [None, None, None, None, None], 0)

	# This is how recursion tree would work 
	#			{}
	#		   / 
	# 		 {}
	# 		/ \ {3}
	# 	 {}     {2}
	#    /	\  / 
	# {}	 {2}
	#			\ {2, 3}
	#
	#			 {1}
	#  \         /
	#   \    {1} 
	#    \	/	\ {1, 3}
	#     {1} 		  {1, 2}
	#         \		 / 
	#          {1, 2}
	#				\ {1, 2, 3}
