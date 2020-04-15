def double_square(num):
    return (2 * num) ** 2

def count_list(lst, item):
    count = 0
    for element in lst:
        if element == item:
            count += 1
    return count

def count_list_recursive(lst, item):
    if not lst:
        return 0
    else:
        if item == lst[0]:
            return 1 + count_list_recursive(lst[1:], item)
        else:
            return count_list_recursive(lst[1:], item)
