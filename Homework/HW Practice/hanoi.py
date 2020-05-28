from hanoi_viz import initialize_towers

def recurse():
    


def main():
    num_disks = input("Enter the number of disks (1 - 8): ")
    while not num_disks.isdigit() or int(num_disks) < 1 or int(num_disks) > 8:
        num_disks = input("Enter the number of disks (1 - 8): ")
    num_disks = int(num_disks)

    
    towers = initialize_towers(num_disks, "source", "target", "middle")
    print(towers)

main()
