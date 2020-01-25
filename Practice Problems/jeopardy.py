'''
    CS5001
    Spring 2020
    Practice Problem 3 - Jeopardy

    Test Case:


'''

def main():
    current_money = float(input("How much money do you have?\n"))
    amount_wagered = float(input("What did you wager on the daily double?\n"))
    win_or_lose = input("Did you get the daily double correct? Enter Yes or No.\n")
    after_wager_money = 0
    if win_or_lose == "Yes":
        after_wager_money = current_money + amount_wagered
        print("You now have {}.".format(after_wager_money))
    if win_or_lose == "No":
        after_wager_money = current_money - amount_wagered
        print("You now have ${:.2f}.".format(after_wager_money))
        

main()
