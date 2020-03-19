def count_items(a_list):
    if a_list == []:
        return 0
    else:
        return 1 + count_items(a_list[1:])

lst = [1, 2, 3, 4]

print(count_items(lst))

