def pn(n):
    if n == 0:
        print(0)
    else:
        print(n)
        pn(n-1)

##pn(9):
##    print(9)
##    pn(8)
##        print(8)
##        pn(7)
##            print(7)
##            pn(6)
##                print(6)
##                pn(5)
##                    print(5)
##                    pn(4)
##                        print(4)
##                        pn(3)
##                            print(3)
##                            pn(2)
##                                print(2)
##                                pn(1)
##                                    print(1)
##                                    pn(0)
##                                        print(0)

def pnr(n):
    if n == 0:
        print(0)
    else:
        pnr(n-1)
        print(n)

##pnr(4):
##    pnr(3)
##        pnr(2)
##            pnr(1)
##                print(0)
##            print(1)
##        print(2)
##    print(3)
##print(4)

def rev(string):
    if not string:
        return ""
    else:
        return string[-1] + rev(string[:-1])

##rev("nate")
##    "e" + rev("nat")
##        "t" + rev("na")
##            "a" + rev("n")
##                "n" + rev("")
##                "n" + ""
##            "a" + "n"
##        "t" + "an"
##    "e" + "tan"
##"etan"


def factorial(num):
    if num == 0:
        return 0
    else:
        return num + factorial(num - 1)
