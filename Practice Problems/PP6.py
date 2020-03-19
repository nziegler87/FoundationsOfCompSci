def count_occurrences(lst, number):
    if not lst:
        return 0
    else:
        if lst[0] == number:
            return 1 + count_occurrences(lst[1:], number)
        else:
            return 0 + count_occurrences(lst[1:], number)

def rev(lst):
    if len(lst) == 1:
        return lst
    else:
        return rev(lst[1:]) + lst[0]

def sum_int(integer):
    if integer == 0:
        print("About to enter base case")
        return 0
    else:
        print("Integer:", integer)
        return integer + sum_int((integer - 1))

def sort_list(lsta):
    list_copy = lsta[:]
    combined_list = []
    while len(list_copy) > 0:
        min_index = 0
        for i in range(len(list_copy)):
            if list_copy[i] <= list_copy[min_index]:
                min_index = i
        combined_list.append(list_copy[min_index])
        list_copy.pop(min_index)
    return combined_list

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def merge_dictionary(dict1, dict2):
    if len(dict1) > len(dict2):
        merged_dict = dict1
        insert_dict = dict2
    else:
        merged_dict = dict2
        insert_dict = dict1
    for key in insert_dict.keys():
        if key in merged_dict.keys():
            merged_dict[key] = [merged_dict[key], insert_dict[key]]
        else:
            merged_dict[key] = insert_dict[key]
    return merged_dict

def merge_dictionary2(dict1, dict2):
    merged = {}
    for key, value in dict1.items():
        if key in dict2.keys():
            merged[key] = [value, dict2[key]]
        else:
            merged[key] = value
    for key, value in dict2.items():
        if key not in merged.keys():
            merged[key] = value
    return merged
        
    
def double_values(dictionary):
    doubled_dict = {}
    for key, value in dictionary.items():
        doubled_dict[key] = (value * 2)
    return doubled_dict
        

def double_recursive(org_dict):
    if len(org_dict) == 1:
        double_dict = {}
        k = org_dict.values()
        v = org_dict.values() * 2
        return (double_dict[k] == v)

def how_many_digits(number):
    if number < 10:
        return 1
    else:
        return 1 + how_many_digits(number // 10)

def hailstone(number):
    if number == 1:
        print(1)
    else:
        print(int(number))
        if number % 2 == 0:
            return hailstone(number / 2)
        else:
            return hailstone(3 * number + 1)

def count_freq_loop(lst):
    frequency = {}
    for word in lst:
        if word in frequency.keys():
            count = frequency[word]
            frequency[word] = 1 + count
        else:
            frequency[word] = 1
    return frequency

    
            
        
    
    
    

