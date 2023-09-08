import requests
from bs4 import BeautifulSoup

page = requests.get(
    "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
)
soup = BeautifulSoup(page.content, "html.parser")
seven_day = soup.find(id="seven-day-forecast-list")  # seven-day-forecast
forecast_items = seven_day.find_all(class_="tombstone-container")
# print(forecast_items)
tonight = forecast_items[0]
# print(tonight)
# print(tonight.prettify())
period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
# print(period)
# print(short_desc)
print(temp)
img = tonight.find("img")
print(img)
desc = img["title"]
print(desc)
