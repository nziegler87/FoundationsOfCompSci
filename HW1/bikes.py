'''
    Nathanial Ziegler
    CS5001
    Homework 1
    January 15, 2020

    Description:
        Calculates the number of bikes that can be built based on the number
        of available wheels, frames, and links. Program then returns the
        number of leftover parts after building the max number
        of bikes possible.

    Test case #1:
        Parts:
            Wheels: 3
            Frames: 2
            Links: 80
        Bikes: 1
        Leftover:
            1 wheels
            1 frames
            30 links

    Test case #2:
        Parts:
            Wheels: 8
            Frames: 3
            Links: 300
        Bikes: 3
        Leftover:
            2 wheels
            0 frames
            150 links

    Test case #3:
        Parts:
            Wheels: 749
            Frames: 81
            Links: 6089
        Bikes: 81
        Leftover:
            587 wheels
            0 frames
            2039 links
'''

# Minimum number of parts required to build single bike

WHEELS_PER_BIKE = 2
FRAMES_PER_BIKE = 1
LINKS_PER_BIKE = 50

def main():

    # Collects number of wheels, frames, and links owned by user
    
    wheels = int(input("How many wheels do you have?\n"))
    frames = int(input("How many frames do you have?\n"))
    links = int(input("How many links do you have?\n"))

    # Calculates max bikes possible
    
    bikes_possible = min(wheels // WHEELS_PER_BIKE, frames // FRAMES_PER_BIKE,
                         links // LINKS_PER_BIKE)

    # Calculates left over parts
    
    leftover_wheels = wheels - (bikes_possible * WHEELS_PER_BIKE)
    leftover_frames = frames - (bikes_possible * FRAMES_PER_BIKE)
    leftover_links = links - (bikes_possible * LINKS_PER_BIKE)

    # Prints max number of bikes and leftover parts
    
    print("\nAll totalled, you've got", bikes_possible,
          "bike(s) coming up.\n\n"
          "I'm keeping the leftovers for myself:\n"
          "{} wheels\n{} frames\n{} links\n\n"
          "Thanks!".format(leftover_wheels, leftover_frames, leftover_links))

main()
