def mean(num_list):
    if len(num_list) == 0:
        return 0
    total = 0
    for i in range(len(num_list)):
        total += num_list[i]
    average = total / len(num_list)
    return average

def intersect(lista, listb):
    common_list = []
    for i in range(len(lista)):
        if lista[i] in listb and lista[i] not in common_list:
            common_list.append(lista[i])
    for i in range(len(listb)):
        if listb[i] in lista and listb[i] not in common_list:
            common_list.append(lista[i])
    return common_list

def dedupe(lst):
    scrubbed = []
    for i in range(len(lst)):
        if lst[i] not in scrubbed:
            scrubbed.append(lst[i])
    return scrubbed
            
