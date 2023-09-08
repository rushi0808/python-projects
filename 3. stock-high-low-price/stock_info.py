import stock
from prettytable import PrettyTable

while True:
    st1 = "Hello Welcome to Stock Market"
    st2 = "Choose the option "
    print("-" * 35)
    print(st1.center(35, " "))
    print(st2.center(35, " "))
    print("-" * 35)
    print("1. Stock Details")
    print("2. Stock High Low Price Year Wise")
    print("3. Exit")
    print("-" * 35)
    x = int(input("Enter Your option:"))
    if x == 1:
        print("-" * 35)
        stock.show_detl()

    elif x == 2:
        print("-" * 35)
        data = stock.hi_lo_Yearwise()
        table = PrettyTable(["Years", "High Price", "Low Price"])
        for each in data:
            table.add_row([each[0], each[1], each[2]])
        print(table)

    elif x == 3:
        print("-" * 35)
        print("Thanks for using my stock details system!")
        break

    else:
        print("-" * 35)
        error = "Enter a valid option"
        print(error.center(35, " "))
