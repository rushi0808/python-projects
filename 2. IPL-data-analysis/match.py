import csv


def toss_Win(team):
    infile = open(r".\matches.csv")
    data = csv.DictReader(infile)
    list_toss = []
    matches = 0
    toss_win = 0
    for each in data:
        if team in (each["TEAM1"] or each["TEAM2"]):
            matches = matches + 1
            if team in each["TOSS_WINNER"]:
                toss_win = toss_win + 1
    else:
        list_toss.append(matches)
        list_toss.append(toss_win)
        return list_toss


def yearwise_Wonplayed(team):
    infile = open(r".\matches.csv")  # this is for forming listYear(var)
    data = csv.DictReader(infile)
    listYear = set()
    for each in data:
        listYear.add(each["SEASON"])

    year_matches = []
    for x in list(listYear):
        infile = open(
            r".\matches.csv"
        )  # this is for fetching data if not open in here data will not be fetched as new block has started
        data = csv.DictReader(infile)
        t_matches = 0
        matches_won = 0
        for y in data:
            if (team in (y["TEAM1"] or y["TEAM2"])) and y["SEASON"] == x:
                t_matches += 1
                if y["WINNER"] == team:
                    matches_won += 1
        year_matches.append([x, t_matches, matches_won])

    return year_matches


def locationwise_Wonplayed(team):
    infile = open(r".\matches.csv")  # same as yearwise_Wonplayed
    data = csv.DictReader(infile)
    listCities = set()
    for each in data:
        listCities.add(each["CITY"])

    city_Matches = []
    for x in list(listCities):
        infile = open(r".\matches.csv")  # same as yearwise_Wonplayed
        data = csv.DictReader(infile)
        t_matches = 0
        matches_won = 0
        for y in data:
            if (team in (y["TEAM1"] or y["TEAM2"])) and y["CITY"] == x:
                t_matches += 1
                if y["WINNER"] == team:
                    matches_won += 1
        city_Matches.append([x, t_matches, matches_won])

    return city_Matches


def showTeam():
    infile = open(r".\matches.csv")
    data = csv.DictReader(infile)
    listTeam = set()
    for each in data:
        listTeam.add(each["TEAM1"])
        listTeam.add(each["TEAM2"])
    dictTeam = dict(zip(range(0, len(listTeam)), listTeam))
    for x, y in dictTeam.items():
        print(x, ".", y)
    team = int(input("Enter a Team:"))
    a = True
    while a:
        if team in dictTeam.keys():
            a = False
        else:
            print("Enter a valid Team")
    else:
        return dictTeam[team]
