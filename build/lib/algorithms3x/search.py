from .sort import selection_sort
def binary_search(arrayParam, target):
    """
    Searches for an item using binary search algorithm. Run time: O(log n)
    """
    array = selection_sort(arrayParam) 
    middleIndex = int(len(array) / 2)
    while len(array) > 1:
        middleIndex = int(len(array) / 2)
        middlePoint = array[middleIndex]
        if target == middlePoint:
            return True
        if target > middlePoint:
            if array[middleIndex] != array[0]:
                del array[0 : middleIndex]
            else:
                del array[0]
        else:
            if array[middleIndex] != array[-1]:
                del array[middleIndex : -1]
            else:
                del array[-1]
    return False


def linear_search(array, target):
    """
    Search for an item using liner search. Run time: O(n)
    """
    for i in array:
        if i == target:
            return True
    return False