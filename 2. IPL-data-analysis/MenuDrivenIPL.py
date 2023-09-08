import match
from prettytable import PrettyTable

while True:
    print("===Statistics===")
    print("1. Toss Winning Stats")
    print("2. Yearwise matches played/won")
    print("3. Citywise Matches played/won")
    print("4. Exit")
    choice = int(input("Enter a choice: "))

    if choice == 1:
        team = match.showTeam()
        listToss = match.toss_Win(team)
        print("*" * 60)
        print(
            "%s won toss %s times in %s matches.\nHence toss winning percentage is %.2f"
            % (team, listToss[1], listToss[0], float(listToss[1]) / listToss[0] * 100)
            + "%"
        )  # (listToss)
        print("*" * 60)
        continue
    elif choice == 2:
        team = match.showTeam()
        yearMatch = match.yearwise_Wonplayed(team)
        print("*" * 60)
        print(team)
        table = PrettyTable(["YEAR", "MATCHES PLAYED", "MATCHES WON"])
        yearMatch.sort()
        for value in yearMatch:
            table.add_row([value[0], value[1], value[2]])
        print(table)
        print("*" * 60)
        continue
    elif choice == 3:
        team = match.showTeam()
        cityMatch = match.locationwise_Wonplayed(team)
        print("*" * 60)
        print(team)
        table2 = PrettyTable(["CITY", "MATCHES PLAYED", "MATCHES WON"])
        cityMatch.sort()
        for value in cityMatch:
            table2.add_row([value[0], value[1], value[2]])
        print(table2)
        print("*" * 60)
        continue
    elif choice == 4:
        print("Thanks for exploring our site. Do visit again...!!!!")
        break
    else:
        print("Invalid Choice")
