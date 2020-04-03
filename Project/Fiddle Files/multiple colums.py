x = 250
size = 10
spacing = 50

arrows = [[1,0,10], [2,20,30], [3,40,50]]

def return_col(x, lst):
    for i in range(len(lst)):
        if x > arrows[i][1] and x < arrows[i][2]:
            print(arrows[i][0])


    
