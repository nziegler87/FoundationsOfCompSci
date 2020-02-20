import random

def count_words(sentence):
    sentence_list = sentence.split()
    count = 0
    for word in sentence_list:
        count += 1

    return count

def return_true(item, check_list):
    for i in range(len(check_list)):
        if item == check_list[i]:
            return True
        
def shuffle(input_list):
    temp_list = input_list.copy()
    shuffled_list = []
    while len(temp_list) > 0:
        random_index = random.randint(0, len(temp_list) - 1)
        shuffled_list.append(temp_list[random_index])
        temp_list.pop(random_index)
    return shuffled_list

def getMin(input_list):
    min_so_far = input_list[0]
    for value in list:
        if value < min_so_far:
            min_so_far = value
    return min_so_far
    
