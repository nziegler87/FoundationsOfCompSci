def factorial(num):
    if num < 0:
        return 0
    elif num == 0:
        return 0
    else:
        return num + factorial(num - 1)

def summative(lst):
    if not lst:
        return 0
    else:
        return lst[0] + summative(lst[1:])

def countin(lst, item):
    if not lst:
        return 0
    else:
        if item == lst[0]:
            return 1 + countin(lst[1:], item)
        else:
            return countin(lst[1:], item)

def rev(lst):
    if not lst:
        return []
    else:
        return [lst[-1]] + rev(lst[:-1])

def is_pal(string):
    if len(string) < 1:
        return True
    else:
        if string[0] == string[-1]:
            return is_pal(string[1:-1])
        else:
            return False

def log_bs2(n):
    if n == 1:
        return 0
    else:
        return 1 + log_bs2(n // 2)

def binary(n):
    if n > 1:
        binary(n // 2)
    print(n % 2, end = "")

def rev_list(lst):
    if not lst:
        return []
    else:
        return [lst[-1]] + rev_list(lst[:-1])

def rev_string(string):
    if not string:
        return ""
    else:
        return string[-1] + rev_string(string[:-1])

def sum_list(lst):
    if not lst:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])

def factorial
