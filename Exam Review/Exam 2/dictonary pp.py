def count_occurrences(lst, item):
    if not lst:
        return 0
    else:
        if lst[0] == item:
            return 1 + count_occurrences(lst[1:], item)
        else:
            return count_occurrences(lst[1:], item)


def rev(lst):
    if not lst:
        return ""
    else:
        return lst[-1] + lst[:-1]

def log(num):
    pass

def doubles_values(dictionary):
    new_dict = {}
    for k, v in dictionary.items():
        new_dict[k] = v * 2
    return new_dict

def merge_dicts(d1, d2):
    merged = {}
    for k, v in d2.items():
        if k in d1.keys():
            merged[k] = [v, d1[k]]
        else:
            merged[k] = v
    for k, v in d1.items():
        if k not in merged.keys():
            merged[k] = v
    return merged
