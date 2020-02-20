def ask_bill():
    amount = float(input("How much was your bill?\n"))
    return amount

def ask_tip():
    tip = int(input("How much do you want to tip?\n"))
    return tip

def main():
    while True:
        bill = ask_bill()
        tip_percent = ask_tip()
        tip_amount = bill * (tip_percent / 100)
        total_bill = bill + tip_amount
        print("A {:n}% tip on a ${:.2f} bill is ${:.2f}.\n"
              "Your total  bill is: ${:.2f}".format(tip_percent, bill,
                                                     tip_amount, total_bill))
main()
