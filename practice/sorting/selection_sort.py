def selection_sort(inputArray):
    """input: array
    output: sorted array
    features: in-place, adaptive, stable
    efficiency: O(n^2) (worst/avg/best cases)
    space complexity: O(1)
    method:
    starting with 0, record index where every previous element is sorted
    iterate through the unsorted portion of the list
    each iteration, find the min value in the unsorted portion
    swap the min value with the first value in the unsorted portion
    increase index of sorted portion by 1 to include the value
    iterate until the full list is sorted"""
    sort_point = 0
    while sort_point < len(inputArray) - 1:
        minval = inputArray[sort_point]
        for i in range(len(inputArray[sort_point:])):
            index = i + sort_point
            value = inputArray[index]
            if value < minval:
                minval = value
                minindex = index
        if minval != inputArray[sort_point]:
            inputArray[minindex] = inputArray[sort_point]
            inputArray[sort_point] = minval
        sort_point += 1
    return inputArray


# Testing
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]
array3 = [2, 4, 1, 5, 3]
array4 = [2, 2, 2, 2, 2]
array5 = ['e', 'd', 'c', 'b', 'a']
print selection_sort(array1)
print selection_sort(array2)
print selection_sort(array3)
print selection_sort(array4)
print selection_sort(array5)
