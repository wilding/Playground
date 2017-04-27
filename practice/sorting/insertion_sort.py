def insertion_sort(inputArray):
    """input: array
    output: sorted array
    features: in-place, stable, adaptive, online
    efficiency: O(n^2) (worst/avg cases), O(n) (best case)
    space complexity: O(1)
    method:
    Iterate through the array.
    If the previous value is greater than the current value,
    move previous value to current index.
    Continue backwards until current value is larger than the previous value,
    and assign the value to the corresponding index."""
    for index in range(len(inputArray)):
        value = inputArray[index]
        position = index
        while position > 0 and inputArray[position-1] > value:
            inputArray[position] = inputArray[position-1]
            position = position - 1
        inputArray[position] = value
    return inputArray


# Testing
array1 = [1, 2, 3, 4, 5]  # best case - linear
array2 = [5, 4, 3, 2, 1]  # worst case - quadratic
array3 = [2, 4, 1, 5, 3]
array4 = [2, 2, 2, 2, 2]
array5 = ['e', 'd', 'c', 'b', 'a']
print insertion_sort(array1)
print insertion_sort(array2)
print insertion_sort(array3)
print insertion_sort(array4)
print insertion_sort(array5)
