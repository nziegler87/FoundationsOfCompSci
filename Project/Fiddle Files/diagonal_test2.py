grid_n = [["00", "01", "02", "03", "04", "05", "06"],
          ["10", "11", "12", "13", "14", "15", "16"],
          ["20", "21", "22", "23", "24", "15", "26"],
          ["30", "31", "32", "33", "34", "35", "36"],
          ["40", "41", "42", "43", "44", "45", "46"],
          ["50", "51", "52", "53", "54", "55", "56"]]

grid_1 = [["b", "01", "02", "03", "04", "05", "06"],
          ["10", "b", "12", "13", "14", "15", "16"],
          ["20", "21", "b", "r", "24", "15", "y"],
          ["30", "31", "r", "33", "34", "y", "36"],
          ["40", "r", "42", "43", "y", "45", "46"],
          ["r", "51", "52", "y", "54", "55", "56"]]

small = [['00', '01', '02'],
         ['10', '11', '12'],
         ['20', '21', '22']]

def make_lst_num(row, col):
    master = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(str(i) + str(j))
        master.append(row)
    return master

def make_lst_alpha(row, col, letter):
    count = ord(letter)
    master = []
    for i in range(row):
        row = []
        for j in range(col):
            if count == ord(letter) + 26:
                count = ord(letter)
            row.append(chr(count))
            count += 1
        master.append(row)
    return master

def diagonals(lst):
    """
    """
    height = len(lst)
    width = len(lst[0])
    for p in range(height + width - 1):
        for q in range(max(p - height + 1, 0), min(p + 1, width)):
            print(lst[height - p + q - 1][q], end = " ")
        print()
        
def antidiagonals(lst):
    """
    """
    height = len(lst)
    width = len(lst[0])
    for p in range(height + width - 1):
        for q in range(max(p - height + 1,0), min(p+1, width)):
            print(lst[p - q][q], end = " ")
        print()

def antidiagonals_lst(lst):
    """
    """
    height = len(lst)
    width = len(lst[0])
    master = []
    for p in range(height + width - 1):
        mini = []
        for q in range(max(p - height + 1,0), min(p+1, width)):
            mini.append(lst[p - q][q])
        master.append(mini)
    return master

def diagonals_lst(lst):
    """
    """
    height = len(lst)
    width = len(lst[0])
    master = []
    for p in range(height + width - 1):
        mini = []
        for q in range(max(p - height + 1, 0), min(p + 1, width)):
            mini.append(lst[height - p + q - 1][q])
        master.append(mini)
    return master

def diagonals_og(lst):
    """
    """
    height = len(lst)
    width = len(lst[0])
    return [[lst[height - p + q - 1][q]
             for q in range(max(p-height+1, 0), min(p+1, width))]
            for p in range(height + width - 1)]

def antidiagonals_og(L):
    """
    """
    h, w = len(L), len(L[0])
    return [[L[p - q][q]
             for q in range(max(p-h+1,0), min(p+1, w))]
            for p in range(h + w - 1)]


