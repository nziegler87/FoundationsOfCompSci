def collect_number():
    number = int(input("Enter a non-zero integer, or 0 to stop: "))
    return number

def append_list(value, total_list):
    total_list.append(value)

def calculate_mean(total_list):
    if len(total_list) == 0:
        return 0
    else:
        average = sum(total_list) / len(total_list)
        return average
    
