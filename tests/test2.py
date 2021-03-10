def quick_sort(array):
    # Choose pivot
    if len(array) <= 1:
        return array
    pivot_ind = int(sum(array)/len(array))
    pivot = array[pivot_ind]
    left = array[:pivot_ind]
    res = []
    right = array[pivot_ind + 1:-1]


array = [6, 24, 17, 51, 32, 49, 76, 64, 81]
print(array[-2])