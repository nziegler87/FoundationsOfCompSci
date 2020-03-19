def is_pal(string):
    '''
    input: string
    base case: one letter
    make smaller: lob off head and tail
    recursive step:
    '''
    if len(string) == 0:
        return True
    else:
        if string[0] == string [-1]:
            return is_pal(string[1:-1])
        else:
            return False
                          
