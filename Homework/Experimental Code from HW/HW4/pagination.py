big = [["P", "P", "P", "P", "G", "G", "G", "G"],
       ["P", "G", "G", "G", "Y", "Y", "L", "L"],
       ["L", "L", "L", "L", "P", "P", "L", "L"],
       ["L", "L", "P", "P", "L", "L", "L", "L"],
       ["W", "W", "W", "W", "L", "L", "L", "L"],
       ["W", "G", "G", "G", "L", "L", "P", "P"]]

small = [["P", "P", "P", "P"],
         ["P", "G", "G", "G"],
         ["L", "L", "L", "L"],
         ["L", "L", "P", "P"],
         ["W", "W", "W", "W"],
         ["W", "G", "G", "G"]]

ROW_PER_PAGE = 3
COL_PER_PAGE = 4

def paginate2(master):
    temp = []
    for i in range(3):
        for j in range(4):
            temp.append(master[i][j])
    return temp

# This one works!
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

## Original attempt at pagination but was looking at quadrants

def paginate_image(raw_image):
    ''' Name: paginate_image
        Inputs:
        Returns:
    '''
    # set blank strings for each page plus final combined image string
    top_left = []
    top_right = []
    bottom_left = []
    bottom_right = []
    paginated_image = []
    
    # sequence for joining individual pages together in string
    compression_sequence = [top_left, top_right, bottom_left, bottom_right]

    # process image string, separating into four quadrants
    for i in range(len(raw_image)):
        for j in range(len(raw_image[i])):
            if i < ROW_PER_PAGE and j < COL_PER_PAGE:
                top_left.append(raw_image[i][j])
            if i < ROW_PER_PAGE and j >= COL_PER_PAGE:
                top_right.append(raw_image[i][j])
            if i >= ROW_PER_PAGE and j < COL_PER_PAGE:
                bottom_left.append(raw_image[i][j])
            if i >= ROW_PER_PAGE and j >= COL_PER_PAGE:
                bottom_right.append(raw_image[i][j])

    # combine individual page strings together into one master string
    for i in compression_sequence:
        paginated_image.append(i)

    return paginated_image

