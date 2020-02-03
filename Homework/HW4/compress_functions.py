##master = [["P", "P", "P", "P", "G", "G", "G", "G"],
##          ["P", "G", "G", "G", "Y", "Y", "L", "L"],
##          ["L", "L", "L", "L", "P", "P", "L", "L"],
##          ["L", "L", "P", "P", "L", "L", "L", "L"],
##          ["W", "W", "W", "W", "L", "L", "L", "L"],
##          ["W", "G", "G", "G", "L", "L", "P", "P"]]

ROW_PER_PAGE = 3
COL_PER_PAGE = 4

def compress(raw):
    paginated_string = paginate(raw)
    combined_pixels_string = compile_pixels(paginated_string)
    return combined_pixels_string

def paginate(master):
    temp = []
    num_row = int(len(master) / ROW_PER_PAGE)
    num_col = int(len(master[0]) / COL_PER_PAGE)
    for row in range(num_row):
        for col in range(num_col):
            row_mult = row * ROW_PER_PAGE
            col_mult = col * COL_PER_PAGE
            line = []
            for i in range(3):
                for j in range(4):

                    line.append(master[(row_mult + i)][(col_mult + j)])
            temp.append(line)
    return temp

def compile_pixels(original):
    ''' Name: compile_pixels
        Input: strings of pixel colors, each item a string
        Returns: updated lists with repeat pixel colors combined
    '''
    combined_pixels_list = []
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

        combined_pixels_list.append(combined_pixels)
    return combined_pixels_list
