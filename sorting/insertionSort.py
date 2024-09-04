'''
insertion sort algorithim

insert next element into sorted section of array

worst: O(n^2)
best: O(n)
avg: O(n^2)

space: O(1)
'''

def insertionSort(array):
    size = len(array)
    for i in range(1, size):
        insert_index = i
        current_value = array[i]
        for j in range(i-1, -1, -1):
            # third param in range means it sorts backwards

            if array[j] > current_value:
                array[j+1] = array[j]
                insert_index = j
            else:
                break

        array[insert_index] = current_value
        size = len(array)
    

arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
insertionSort(arr)
print('The array after sorting in Ascending Order by insertion sort is:')
print(arr)
