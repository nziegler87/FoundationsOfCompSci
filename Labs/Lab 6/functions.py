def interleave(lista, listb):
    new_list = []
    for i in range(len(lista)):
        item = lista[i] + listb[i]
        new_list.append(item)
    print(" ".join(new_list))
    return new_list

def get_max(num_list):
    if len(num_list) == 0:
        max_num = 0
    else:
        max_num = -99999
        for num in num_list:
            if num > max_num:
                max_num = num
    return max_num

def flip(boolean_list):
    for i in range(len(boolean_list)):
        if boolean_list[i] == False:
            boolean_list[i] = True
        else:
            boolean_list[i] = False
