def linearSearch(array, target):
    """
    Search for an item using liner search. Run time: O(n)
    """
    for i in array:
        if i == target:
            return True
    return False