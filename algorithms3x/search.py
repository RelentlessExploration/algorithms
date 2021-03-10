from sort import merge_sort

def binary_search(array, target):
    """
    ATTENTION: THE PROVIDED ARRAY MUST BE SORTED!
    Searches for an item using binary search algorithm. Run time: O(log n)
    """ 
    # middle = 0
    # if len(array) != 1:
    #     middle =  int(len(array) / 2)
    # print("="*80)
    # print(f"Target: {target}")
    # print(f"Array: {array}")
    # print(f"Middle: {middle}")
    # print(f"Middle item: {array[middle]}")
    # print("="*80)
    # if len(array) == 0:
    #     print("Should have returned!")
    #     return
    # else:
    #     if target < array[middle]:
    #         return binary_search(array[0: middle], target)
    #     elif target > array[middle]:
    #         return binary_search(array[middle + 1:], target)
    #     else:
    #         return True
    array = merge_sort(array)
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

def linear_search(array, target):
    """
    Search for an item using liner search. Run time: O(n)
    """
    for i in array:
        if i == target:
            return True
    return False

arr = [4, 6, 1, 3, 9, 7, 2, 5]
print(binary_search(merge_sort(arr), 14))