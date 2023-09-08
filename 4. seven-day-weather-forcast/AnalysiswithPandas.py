import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
)
soup = BeautifulSoup(page.content, "html.parser")
seven_day = soup.find(id="seven-day-forecast-list")
forecast_items = seven_day.find_all(class_="tombstone-container")
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
short_descs = [
    sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")
]
temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
descs = [d["title"] for d in seven_day.select(".tombstone-container img")]

print(len(period_tags))
print(len(periods))
print(len(short_descs))
print(len(temps))
print(len(descs))

weather = pd.DataFrame(
    {"period": periods, "short_desc": short_descs, "temp": temps, "desc": descs}
)

print(weather)
weather.to_csv("Analysis.csv", index=False)
