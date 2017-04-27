def bubble_sort(inputArray):
    """input: array
    output: sorted array
    features: in-place
    efficiency: O(n^2) (worst/avg cases), O(n) (best case)
    space complexity: O(1)
    method:
    Iterate through the list;
    compare adjacent elements and swap when necessary.
    Each full iteration, the largest element 'sinks' to end of list.
    If no swaps are made in a full iteration,
    the sorted list is immediately returned.
    Each subsequent iteration only iterates through the subset of the list
    before the index of the final swap from the last iteration.
    """
    swap = True
    sorted_point = len(inputArray)
    new_point = None
    while swap and sorted_point > 1:
        swap = False
        for index in range(sorted_point):
            value = inputArray[index]
            if index == sorted_point - 1:
                next_value = None
            else:
                next_value = inputArray[index + 1]
            if next_value and value > next_value:
                inputArray[index] = next_value
                inputArray[index + 1] = value
                swap = True
                new_point = index + 1
        sorted_point = new_point
    return inputArray


# Testing
array1 = [1, 2, 3, 4, 5]  # best case - linear
array2 = [5, 4, 3, 2, 1]  # worst case - quadratic
array3 = [2, 1, 3, 4, 5]
array4 = [2, 2, 2, 2, 2]
array5 = ['e', 'd', 'c', 'b', 'a']
print bubble_sort(array1)
print bubble_sort(array2)
print bubble_sort(array3)
print bubble_sort(array4)
print bubble_sort(array5)
