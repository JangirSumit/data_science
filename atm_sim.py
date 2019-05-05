from datetime import datetime
# ATM Simulation

# defaults
DEF_PIN_NUMBER = "1234"
DEF_CASH_BALANCE = 10000

print("********** HDFC BANK ATM **********")
print("********** Welcome **********\n")
print("Enter your 4-digit pin number.")
pin_number = input(">>> ").strip("")
list = ["10000 Debited on " + str(datetime.now())]


while True:
    if DEF_PIN_NUMBER != pin_number:
        print("Wrong pin number. Please re enter.")
        pin_number = input(">>> ").strip("")
        continue
    print("\n")
    print("Please select your option from below")
    print("1. Check your balance")
    print("2. Withdraw cash")
    print("3. Pin Change")
    print("4. Mini Statement")
    print("5. Exit")
    print("\n")
    user_option = input(">>> ")

    if user_option == "1":
        print("****** Cash Balance ******")
        print("Your latest balance is : " + str(DEF_CASH_BALANCE))
    elif user_option == "2":
        print("****** Withdraw Cash ******")
        print("Enter amount")
        withdraw_amount = int(input(">>> "))
        if withdraw_amount > DEF_CASH_BALANCE:
            print("Please select less amount than your cash balance.")
            continue
        else:
            print("****** Please collect cash ******")
            print(str(withdraw_amount))
            DEF_CASH_BALANCE -= withdraw_amount
            print("Available cash balance : " +
                  str(DEF_CASH_BALANCE))
            list.append(str(withdraw_amount) + " Debited on " +
                        str(datetime.now()))
            continue
    elif user_option == "3":
        print("****** Pin Change ******")
        print("Please enter your old pin")
        pin_number = input(">>> ")
        print("Please enter new pin number")
        new_pin = input(">>> ")
        print("Please re enter new pin number")
        re_new_pin = input(">>> ")

        if pin_number == DEF_PIN_NUMBER and new_pin == re_new_pin:
            DEF_PIN_NUMBER = pin_number
            print("Your pin is successfully changed.")
        else:
            print("Either old pin is wrong or new pin is not correct")
            print("Please re try again")

        continue
    elif user_option == "4":
        print("****** Mini Statement ******")
        for item in list:
            print(item)
        print("Clear Cash Balance now : " + str(DEF_CASH_BALANCE))
    elif user_option == "5":
        print("\n\nThanks for Choosing HDFC Bank.\nVisit Again.")
        break
    else:
        print("OOpsss! Seems wrong option. Please reselect option or exit by pressing 5")
