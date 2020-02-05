'''
    CS 50001
    Nathanial Ziegler
    February 5, 2020
    HW 4
    Description:
        Function to first paginate a nested list of lists of pixels into pages
        of four colums and three rows. Then a function to combine streaks
        of pixels. These are combined into one function to compress a nest
        list of list of pixels.
'''

# Pixel constants
P = "P"
G = "G"
Y = "Y"
L = "L"
W = "W"

# Constants for the number of rows and columns for each page
ROW_PER_PAGE = 3
COL_PER_PAGE = 4

def compress(uncompressed_list):
    ''' Name: compress
        Input: nested string of strings of pixels
        Returns: nested string of strings with pixels compressed and paginated
    '''
    # Call the paginate function to group pixels by pages
    paginated_list = paginate(uncompressed_list)

    # Call the compile_pixels to combine strings of pixels
    combined_pixels_list = compile_pixels(paginated_list)

    return combined_pixels_list

def paginate(input_string):
    ''' Name: paginate
        Input: list of nested strings
        Returns: nested list of strings with pixels grouped by pages
    '''
    final_list = []

    # Calculate number of page rows and cols in given list
    num_row = calculate_row_pages(input_string, ROW_PER_PAGE)
    num_col = calculate_col_pages(input_string, COL_PER_PAGE)

    #Ccreate multipliers to iterate number of row and column pages in list
    for row in range(num_row):
        for col in range(num_col):
            row_mult = row * ROW_PER_PAGE
            col_mult = col * COL_PER_PAGE

            # Create a pages of pixels based on 3 row x 4 col page
            page = []
            for i in range(ROW_PER_PAGE):
                for j in range(COL_PER_PAGE):
                    page.append(input_string[(row_mult + i)][(col_mult + j)])

            # Add each each page of pixels to overal list
            final_list.append(page)

    return final_list

def calculate_row_pages(original_list, row_per_page):
    ''' Name: calculate_row
        Input: list of nested strings
        Returns: number of row pages based on number of rows (int)
    '''
    num_row = int(len(original_list) / row_per_page)
    return num_row

def calculate_col_pages(original_list, col_per_page):
    ''' Name: calculate_col
        Input: list of nested strings that are uniform in 
        Returns: number of col pages based on number of cols (int)
    '''
    pixels = int(len(original_list[0]))
    num_col = int(pixels / col_per_page)
    return num_col

def compile_pixels(uncompiled):
    ''' Name: compile_pixels
        Input: strings of pixel colors, each item a string
        Returns: updated lists with repeat pixel colors combined
    '''
    compiled_pixels_list = []

    # Iterate through each list within the list, combining like strings
    for i in range(len(uncompiled)):
        list_length = len(uncompiled[i])
        count = 1
        combined_pixels = []
        for j in range(len(uncompiled[i])):

            # Set potential pixel or pixel streak to be added to temp string
            pixel = str(count) + " " + uncompiled[i][j]

            # Compare each item to next, adding streak or pixel to temp string
            if j < (list_length - 1):
                if list_length == 1:
                    compiled_pixels.append(pixel)
                elif uncompiled[i][j] == uncompiled[i][(j + 1)]:
                    count += 1
                else:
                    combined_pixels.append(pixel)
                    count = 1
            else:
                combined_pixels.append(pixel)

        # Add string of compressed pixels to overal list
        compiled_pixels_list.append(combined_pixels)

    return compiled_pixels_list
