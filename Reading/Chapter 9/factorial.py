def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def sum_numbers(a_list):
    if not a_list:
        return 0
    else:
        return a_list[0] + sum_numbers(a_list[1:])

def find_max_loop(a_list):
    max_num = a_list[0]
    for item in a_list:
        if item > max_num:
            max_num = item
    return max_num

def reverse_char(a_string):
    if len(a_string) == 1:
        return a_string
    else:
        return reverse_char(a_string[1:]) + a_string[0]
