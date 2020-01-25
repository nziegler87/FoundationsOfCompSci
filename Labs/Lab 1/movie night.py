'''
    CS5003
    Lab 1
    Spring 2020
    Becker & Ziegler
'''

def main():
    num_tickets = int(input("How many tickets do you want?\n"))
    num_popcorn = int(input("How many buckets of popcorn do you want?\n"))
    num_drinks = int(input("How many drinks do you want?\n"))
    total = (num_tickets * 7.95) + (num_popcorn * 8.95) + (num_drinks * 4.25)
    discount_cost = total * .9
    print("Total cost is\n${:.2f}".format(total))
    print("Your price after the discount is:\n${:.2f}".format(discount_cost))

main()
