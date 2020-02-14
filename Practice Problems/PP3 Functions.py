def reverse(input_string):
    string_list = list(input_string)
    reverse_list = []
    index = len(string_list) - 1
    for i in range(len(string_list)):
        reverse_list += string_list[index]
        string_list.pop(index)
        index -= 1
    return("".join(reverse_list))

def swapchar(stringa, stringb):
    newa = stringb[:1] + stringa[1:]
    newb = stringa[:1] + stringb[1:]
    return (newa, newb)

def swapchar2(stringa):
    string_list = stringa.split(" ")
    
    stringa = string_list[0]
    stringb = string_list[1]
    
    newa = stringb[:1] + stringa[1:]
    newb = stringa[:1] + stringb[1:]

    return(newa + " " + newb)

def swapchar3(s):
    newa, newb = s.split(" ")
    new_string = newb[0] + newa[1:] + " " + newa[0] + newb[1:]
    return new_string
