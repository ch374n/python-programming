# program to implement binary search

def binary_search(arr, start, end, el):
	mid = int((start + end) / 2)

	while start < end:
		if arr[mid] == el:
			return mid
		elif arr[mid] > el:
			end = mid - 1
		else:
			start = mid + 1
		mid = int((start + end) / 2)

	return -1

# 10, 20, 30, 40, 50, 60, 70, 80, 90 


print(binary_search([i for i in range(10, 100, 10)], 0, 8, 20))

