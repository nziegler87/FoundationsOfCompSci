menu_options = ["open", "save", "close"]

def ask_selection():
    user_option = input("Do you want to open a document, save your current "
                        "document, or close your current document?\n"
                        "Enter: open, save, or close\n").lower()
    return user_option

user_option = ask_selection()

while user_option not in menu_options:
    print("In valid option.\n")
    user_option = ask_selection()
