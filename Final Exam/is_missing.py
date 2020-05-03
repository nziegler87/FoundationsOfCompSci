def is_missing(lst):
    sequence = 1
    for i in range(len(lst) + 1):
        try:
            lst.index(sequence)
            lst.remove(sequence)
            sequence += 1
        except ValueError:
            return sequence
