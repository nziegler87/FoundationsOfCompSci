'''
    CS 50001
    Nathanial Ziegler
    February 5, 2020
    HW 4
    Description:
        UPDATE
'''

P = "P"
G = "G"
Y = "Y"
L = "L"
W = "W"

##big = [[P, P, P, P, G, G, G, G],
##          [P, G, G, G, Y, Y, L, L],
##          [L, L, L, L, P, P, L, L],
##          [L, L, P, P, L, L, L, L],
##          [W, W, W, W, L, L, L, L],
##          [W, G, G, G, L, L, P, P]]
##
##
##small = [[P, P, P, P],
##         [P, G, G, G],
##         [L, L, L, L],
##         [L, L, P, P],
##         [W, W, W, W],
##         [W, G, G, G]]


ROW_PER_PAGE = 3
COL_PER_PAGE = 4

def compress(raw):
    ''' Name: compress
        Input: string of pixels as strings
        Returns: paginated and compressed list of pixels
    '''
    paginated_string = paginate(raw)
    combined_pixels_string = compile_pixels(paginated_string)
    return combined_pixels_string

def paginate(master):
    ''' Name: paginate
        Input: list of nested strings
        Returns: list of of page-specific lists
    '''
    final_list = []

    # Calculate number of rows and cols in given list
    num_row = calculate_row(master, ROW_PER_PAGE)
    num_col = calculate_col(master, COL_PER_PAGE)

    # Iterate through list by sections of 3 rows and 4 colums, appending each section
    # as new list, which are then appended to master list
    for row in range(num_row):
        for col in range(num_col):
            row_mult = row * ROW_PER_PAGE
            col_mult = col * COL_PER_PAGE
            line = []
            for i in range(ROW_PER_PAGE):
                for j in range(COL_PER_PAGE):
                    line.append(master[(row_mult + i)][(col_mult + j)])

            # Add each each page of pixels to overal list
            final_list.append(line)

    return final_list

def calculate_row(original_list, row_per_page):
    ''' Name: calculate_row
        Input: list of nested strings
        Returns: number of rows in list
    '''
    num_row = int(len(master) / row_per_page)
    return num_row

def calculate_col(original_list, col_per_page)
    ''' Name: calculate_col
        Input: list of nested strings
        Returns: number of columns in list
    '''
    num_col = int(len(master[0]) / col_per_page)
    return num_col

def compile_pixels(original):
    ''' Name: compile_pixels
        Input: strings of pixel colors, each item a string
        Returns: updated lists with repeat pixel colors combined
    '''
    combined_pixels_list = []

    # Iterate through each list within the list, combining like strings
    for i in range(len(original)):
        list_length = len(original[i])
        count = 1
        combined_pixels = []
        for j in range(len(original[i])):
            pixel = str(count) + " " + original[i][j]
            if j < (list_length - 1):
                if list_length == 1:
                    combined_pixels.append(pixel)
                elif original[i][j] == original[i][(j + 1)]:
                    count += 1
                else:
                    combined_pixels.append(pixel)
                    count = 1
            else:
                combined_pixels.append(pixel)

        # Add string of compressed pixels to overal list
        combined_pixels_list.append(combined_pixels)

    return combined_pixels_list
