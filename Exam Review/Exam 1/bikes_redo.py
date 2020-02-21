'''
    Bikes Redo
'''

parts = ["wheels", "frames", "links"]

WHEELS_PER_BIKE = 2
FRAMES_PER_BIKE = 1
LINKS_PER_BIKE = 50

def collect_amount(part_name):
    amount = int(input("How many " + part_name + " do you have?\n"))
    return amount

def bikes_possible(user_amount, amount_per_bike):
    return(user_amount // amount_per_bike)

def leftover_parts(num_bikes, user_amount, amount_per_bike):
    parts_used = num_bikes * amount_per_bike
    return (user_amount - parts_used)

def print_bikes_possible(bikes_possible):
    if bikes_possible == 0:
        print("You don't have enough parts for me to make one bike....")
    elif bikes_possible == 1:
        print("I can make", bikes_possible, "bike.")
    else:
        print("I can make", bikes_possible, "bikes.")

def print_leftover_parts(wheels, frames, links):
    print("I'm keeping the leftover parts:")
    print_individual_leftovers(wheels, "wheel", "wheels")
    print_individual_leftovers(frames, "frame", "frames")
    print_individual_leftovers(links, "link", "links")

def print_individual_leftovers(part, singular_name, plural_name):
    if part == 1:
        print(part, singular_name)
    else:
        print(part, plural_name)

def main():
    while True:
        wheels = collect_amount("wheels")
        frames = collect_amount("frames")
        links = collect_amount("links")
        
        total_possible = min((bikes_possible(wheels, WHEELS_PER_BIKE),
                              bikes_possible(frames, FRAMES_PER_BIKE),
                              bikes_possible(links, LINKS_PER_BIKE)))

        wheels_leftover = leftover_parts(total_possible, wheels, WHEELS_PER_BIKE)
        frames_leftover = leftover_parts(total_possible, frames, FRAMES_PER_BIKE)
        links_leftover = leftover_parts(total_possible, links, LINKS_PER_BIKE)

        print_bikes_possible(total_possible)
        print_leftover_parts(wheels_leftover, frames_leftover, links_leftover)
    

main()
