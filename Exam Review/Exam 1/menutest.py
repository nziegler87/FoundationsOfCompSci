MENU_ITEMS = ["New", "Open", "Save", "Close"]
MENU_OPTIONS = ["N", "O", "S", "C"]
MENU = [("N", "New"), ("O", "Open"), ("S", "Save"), ("C", "Close")]

def call_menu():
    print("Do you want to create new document, open an existing document, "
          "save your current file, or close completely?")
    for i in range(len(MENU_ITEMS)):
        print("   ", MENU_OPTIONS[i], "--", MENU_ITEMS[i])

def collect_choice(validate_list):
    choice = input("Enter your selection: ").upper()
    while choice not in validate_list:
        choice = input(("Invalid entry. Please try again: ")).upper()
    else:
        return choice

def call_menu2(menu):
    print("Do you want to create new document, open an existing document, "
          "save your current file, or close completely?")
    for options in menu:
        option, item = options
        print("    ", option, "--", item)

def main():

    call_menu2(MENU)
    choice = collect_choice(MENU_OPTIONS)
    print(choice)

main()
