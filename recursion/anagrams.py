# program to print all the anagrams of a given word

def swap(my_list, start, begin):
	temp = my_list[begin]
	my_list[begin] = my_list[start]
	my_list[start] = temp

def print_anagrams(my_list, start, end):
	if start == end:
		print(''.join(my_list))
	else:
		for begin in range(start, end + 1):
			swap(my_list, start, begin)
			print_anagrams(my_list, start + 1, end)
			swap(my_list, start, begin)

print_anagrams(['A', 'B', 'C'], 0, 2)


