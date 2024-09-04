'''
selection sort algorithim

search each iteration for the next smallest element

worst: O(n^2)
best: O(n^2)
avg: O(n^2)

space: O(1)
'''

def selectionSort(array):
	size = len(array)
    
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			# select the minimum element in every iteration
			if array[j] < array[min_index]:
				min_index = j
		# swapping the elements to sort the array
		(array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSort(arr)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
