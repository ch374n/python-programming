# program to implement selection sort 

import time 
from functools import wraps

def calculate_time(sorting_func):
	@wraps(sorting_func)
	def wrapper(*args, **kwargs):
		"""wrapper function to calculate time"""
		t1 = time.time()
		func = sorting_func(*args, **kwargs)
		t2 = time.time()
		print(t2 - t1)
		return func
	return wrapper

def swap(array, i, j):
	temp = array[i]
	array[i] = array[j]
	array[j] = temp

@calculate_time
def selection_sort(array):
	"""selection sort method"""
	for i in range(len(array)):
		for j in range(i, len(array)):
			if array[i] > array[j]:
				swap(array, i, j)
	return array				


@calculate_time
def bubble_sort(array):
	"""bubble sorting method"""
	for i in range(len(array)):
		for j in range(len(array) - 1 - i):
			if array[j] > array[j + 1]:
				swap(array, j + 1, j)
	return array


@calculate_time
def insertion_sort(array):
	"""insertion sort method"""
	for i in range(1, len(array)):
		for j in range(i, 0, -1):
			if array[j] < array[j - 1]:
				swap(array, j, j - 1)
			else:
				break
	
	return array

@calculate_time
def shell_sort(array):
	"""shell sort method"""
	gap = len(array) / 2 + len(array) % 2 
	while gap >= 1:
		i = gap
		while i < len(array):
			k = i
			while k - gap >= 0:
				if array[k] < array[k - gap]:
					swap(array, k, k - gap)
				k = k - gap				
			i += 1
		gap -= 1
	return array


def split(array, list_1, list_2, mid):
	for i in range(len(array)):
		if i < mid:
			list_1.append(array[i])
		else:
			list_2.append(array[i])

def merge(array, list_1, list_2):
	first = 0
	second = 0
	k = 0
	while first < len(list_1) and second < len(list_2):
		if list_1[first] < list_2[second]:
			array[k] = list_1[first]
			first += 1
		else:
			array[k] = list_2[second]
			second += 1
		k += 1

	while first < len(list_1):
		array[k] = list_1[first]
		first += 1
		k += 1
	
	while second < len(list_2):
		array[k] = list_2[second]
		second += 1 
		k += 1

@calculate_time
def merging_sort(array):
	def merge_sort(array):
		"""Merge sort method"""
		mid = int(len(array) / 2) 
		if mid < 1:
			return 
		else:
			# make two list
			list_1 = []
			list_2 = []
			# split the list into two 
			split(array, list_1, list_2, mid)
				# make recursive call 
			merge_sort(list_1)
			merge_sort(list_2)
			# merge lists
			merge(array, list_1, list_2)

		return array
	return array

def partition(array, start, end):
	pivot = array[end]
	index = start - 1
	for i in range(start, end):
		if array[i] < pivot:
			index += 1
			array[index] = array[i]

	index += 1
	swap(array, index, end)
	return index


@calculate_time
def my_quick(array, start, end):
	def quick_sort(array, start, end):
		if start < end:
			pivot = partition(array, start, end)
			quick_sort(array, start, pivot - 1)
			quick_sort(array, pivot + 1, end)
		return array
	return array

# [90, 80, 70, 60, 50, 40, 30, 20, 10]

print(selection_sort([90, 80, 70, 60, 50, 40, 30, 20, 10]))

print(bubble_sort([90, 80, 70, 60, 50, 40, 30, 20, 10]))

print(insertion_sort([90, 80, 70, 60, 50, 40, 30, 20, 10]))

print(shell_sort([90, 80, 70, 60, 50, 40, 30, 20, 10]))

print(merging_sort([90, 80, 70, 60, 50, 40, 30, 20, 10]))

print(my_quick([90, 80, 70, 60, 50, 40, 30, 20, 10],  0, 8))

