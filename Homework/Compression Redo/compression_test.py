pixels = [["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c"],
          ["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c"],
          ["a", "a", "a", "a", "b", "b", "b", "b", "c", "c", "c", "c"],
          ["d", "d", "d", "d", "e", "e", "e", "e", "f", "f", "f", "f"],
          ["d", "d", "d", "d", "e", "e", "e", "e", "f", "f", "f", "f"],
          ["d", "d", "d", "d", "e", "e", "e", "e", "f", "f", "f", "f"]]

example =  [[(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (0, 10), (0, 11)],
            [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11)],
            [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8), (2, 9), (2, 10), (2, 11)],
            [(3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (3, 10), (3, 11)],
            [(4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9), (4, 10), (4, 11)],
            [(5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (5, 9), (5, 10), (5, 11)]]

RPC = 3
CPC = 4

##00 01 02 03
##10 11 12 13
##20 21 22 23
##
##04 05 06 07
##14 15 16 17
##24 25 26 27
##
##08 09 100 110
##18 19 110 120
##29 29 210 220
##
##30 31 32 33
##40 41 42 43
##50 51 52 53

def paginate2(pixels):
    rows = int(len(pixels) / RPC)
    cols = int(len(pixels[0]) / CPC)
    total_pages = rows * cols
    paginated_master = []
    for r in range(rows):
        for c in range(cols):
            for i in range(r * RPC, r + RPC):
                for j in range(c * CPC, c + CPC):
                    print(pixels[i][j])
        

def paginate(pixels):
    rows = int(len(pixels) / RPC)
    cols = int(len(pixels[0]) / CPC)
    total_pages = rows * cols
    paginated_master = []
    for x in range(total_pages):
        paginated = []
        for i in range(RPC):
            row = []
            for j in range(CPC):
                row.append((i, j))          # need to switch back to pixels[i][j]
            paginated.append(row)
        paginated_master.append(paginated)
    print(paginated_master)
