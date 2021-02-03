from selectionSort import selectionSort
def binarySearch(arrayParam, target):
    """
    Searches for an item using linear search algorithm. Run time: O(n/2)
    """

    array = selectionSort(arrayParam) 
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
