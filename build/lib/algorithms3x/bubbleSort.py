from copy import deepcopy
def bubbleSort(arrayParam):
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