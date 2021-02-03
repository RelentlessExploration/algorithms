from copy import deepcopy
def bubble_sort(arrayParam):
    """
    Sort a list using bubble sort algorithm. Run time: O(n**2)
    """
    done = True
    array = deepcopy(arrayParam)
    for l in range(1, len(array)):
        if array[l] < array[l - 1]:
            done = False
    if done == True:
        return array
    
    while done == False:
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                tmp = array[i]
                array[i] = array[i - 1]
                array[i - 1] = tmp
        done = True
        for k in range(1, len(array)):
            if array[k] < array[k - 1]:
                done = False
        if done == True:
            return array
def selection_sort(arrayParam):
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