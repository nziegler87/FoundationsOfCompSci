def binary_search(lst, key, left, right):
    ''' Function: binary_search
        Parameters: lst of elements, key to search for,
                    leftmost index, rightmost index
        Returns: True if key is found in lst, else false
    '''
    if left > right:
        return False

    midpoint = (left + right) // 2
    if lst[midpoint] == key:
        return True
    elif lst[midpoint] < key:
        return binary_search(lst, key, midpoint + 1, right)
    else:
        return binary_search(lst, key,  left, midpoint - 1)
