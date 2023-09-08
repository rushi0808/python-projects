import json

import requests

json_page = requests.get(
    r"https://data.nasdaq.com/api/v3/datasets/XNSE/BAJAJ_AUTO.json?api_key=RdaxscUbcc4x-XpQdsWe"
)
dt = json.loads(json_page.text)


def hi_lo_Yearwise():
    list_Year = year_List()
    dt1 = []
    for year in list_Year:
        dt2 = []
        high = []
        low = []
        for each in dt["dataset"]["data"]:
            if year == each[0].split("-")[0]:
                high.append(float(each[2]))
                low.append(float(each[3]))
        else:
            dt2.append(year)
            dt2.append(max(high))
            dt2.append(min(low))
            dt1.append(dt2)
    else:
        return dt1


def year_List():
    yl = set()
    for each in dt["dataset"]["data"]:
        yl.add(each[0].split("-")[0])
    else:
        year_List = sorted(list(yl))
        return year_List


def show_detl():
    print(
        f"""id of Stock: {dt['dataset']['id']}\n)
    Name of Stock:', {dt['dataset']['name']}\n)
    Type of Stock:', {dt['dataset']['type']}\n)
    Data of stock is available from {dt['dataset']['oldest_available_date']} to {dt['dataset']['newest_available_date']}."""
    )


if __name__ == "__main__":
    # print(hi_lo_Yearwise())
    print(dt)
#    print(year_List())
#    for each in dt['dataset']['data']:
#        print(each)
#    for each in dt['dataset'].keys():
#        print(each)
#    print(dt['dataset'].keys())
#    for each in dt['dataset']['data']:
#        print(each[0].split('-')[0])
