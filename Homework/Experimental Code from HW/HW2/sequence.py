''' CS5001
    Spring 2020
    HW2 starter code

    (1) Compute the kth term in an arithmetic sequence
    (2) Sum the first n terms in an arithmetic sequence
'''

def kth_term(initial, diff, k):
    ''' Function: kth_term
        Parameters: initial value, common difference, k -- all integers
        Returns: the kth term in the arithmetic sequence, an integer
        Does: Calculates the kth term of arithmetic sequence a1, a2, a3, ...,
              where a1 = a, a2 = a + k, a3 = a + 2k, ...
    '''
    return initial + (k - 1) * diff

def arith_sum(initial, diff, n):
    ''' Function: arith_sum
        Parameters: initial value, common difference, n -- all integers
        Returns: the value of the first n terms of the summation, an integer
        Does: Calculates the arithmetic sum using the handy formula
               (# terms)(first + last) / 2
    '''
    first = initial
    last = kth_term(initial, diff, n)
    return (n * (first + last)) / 2
