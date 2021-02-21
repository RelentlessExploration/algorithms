def merge(L, R):
    res = []
    left_ind = right_ind = 0
    while left_ind < len(L) and right_ind < len(R):
        
        if L[left_ind] < R[right_ind]:
            res.append(L[left_ind])
            left_ind += 1
        elif L[left_ind] > R[right_ind]:
            res.append(R[right_ind])
            right_ind += 1
        else:
            res.append(R[right_ind])
            res.append(L[right_ind])
            left_ind += 1
            right_ind += 1
    res.extend(L[left_ind:])
    res.extend(R[right_ind:])
    return res


def merge_sort(array):
    """
    ### Merge sort
    Implementation of one of the most powerful sorting algorithms algorithms.\n
    Return a sorted array, 
    """
    length = len(array)
    if length <= 1:
        return array
    
    middle_ind = int(length/2)
    right = merge_sort(array[middle_ind:])
    left = merge_sort(array[:middle_ind])
    
    return merge(right, left)


print(merge_sort([1, 9, 6, 4, 2, 5, 3, 8, 7]))