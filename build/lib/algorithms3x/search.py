from .sort import selection_sort
def binary_search(arrayParam, target):
    """
    Searches for an item using linear search algorithm. Run time: O(n/2)
    """

    array = selection_sort(arrayParam) 
    middleIndex = int(len(array) / 2)
    while len(array) != 1:
        middleIndex = int(len(array) / 2)
        middlePoint = array[middleIndex]
        if target == middlePoint:
            return True
        if target > middlePoint:
            del array[0 : middleIndex]
        else:
            del array[middleIndex : -1]
    return False
    
def linear_search(array, target):
    """
    Search for an item using liner search. Run time: O(n)
    """
    for i in array:
        if i == target:
            return True
    return False