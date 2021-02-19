from algorithms3x.sort import selection_sort
def binary_search(arrayParam, target):
    """
    Searches for an item using binary search algorithm. Run time: O(log n)
    """
    array = selection_sort(arrayParam)     
    while len(array) > 1:
        middleIndex = int(len(array) / 2)
        middlePoint = array[middleIndex]
        if target == middlePoint:
            return True
        if target > middlePoint:
            if array[middleIndex] != array[0]:
                del array[0 : middleIndex + 1]
                if array[-1] == target:
                    return True
            else:
                del array[0]
                if array[-1] == target:
                    return True
        else:
            if array[middleIndex] != array[-1]:
                del array[middleIndex : -1]
            else:
                del array[-1]
                if array[0] == target:
                    return True
    return False

print(binary_search([1, 2, 3, 4], 4))