from copy import deepcopy
def selectionSort(arrayParam):
    """
    Sort a list using selection sort algorithm. Run time: O(n**2)
    """
    position = 0
    array = deepcopy(arrayParam)
    for k in array:
        smallest = None
        subPosition = position
        smallestIndex = None
        # Getting smallest value and index
        for i in range(position, len(array)):
            if subPosition == position:
                smallest = array[i]
                smallestIndex = i
            else:
                if array[i] < smallest:
                    smallest = array[i]
                    smallestIndex = i
            subPosition += 1
        missingIndex = position
        tmp = smallest
        array[smallestIndex] = array[missingIndex]
        array[missingIndex] = tmp
        position += 1
    return array