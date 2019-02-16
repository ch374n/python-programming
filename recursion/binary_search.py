def binary_search_recursive(arr, start, end, el):
	mid = int((start + end) / 2)

	if start < end:
		if arr[mid] == el:
			return mid
		elif arr[mid] > el:
			return binary_search_recursive(arr, start, mid - 1, el)
		else:
			return binary_search_recursive(arr, mid + 1, end, el)
	else:
		return -1
print(binary_search_recursive([i for i in range(10, 100, 10)], 0, 8, 20))