import time

import requests
from bs4 import BeautifulSoup

print("Put some skill that you are not familiar with")
unfamiliar_skill = input("Enter unfamiliar Skill:")
print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation="
    ).text
    # using '.text' to get the html page in the form of text
    # print(html_text) # printing the html_text variable without the '.text' function will get you the response of the webpage that you have passed to '.get' function
    soup = BeautifulSoup(html_text, "lxml")
    jobs = soup.findAll("li", class_="clearfix job-bx wht-shd-bx")
    # print(jobs)
    for index, job in enumerate(jobs):
        job_published_date = job.find("span", class_="sim-posted").span.text
        if "few" in job_published_date:
            company_name = job.find("h3", class_="joblist-comp-name").text.replace(
                " ", ""
            )  # replace function to replace the space with nothing in the company_name variable
            skills = job.find("span", class_="srp-skills").text.replace(" ", "")
            more_info = job.header.h2.a[
                "href"
            ]  # to get the link of the job from 'a' tag which is present in the 'header' tag
            if unfamiliar_skill not in skills:
                with open(rf"./posts/{index}.txt", "w") as f:
                    f.write(
                        f"Company Name: {company_name.strip()}\n"
                    )  # '.strip()' function to remove the whitespaces from the beginning and the end of the string
                    f.write(f"Required Skills:{skills.strip()}\n")
                    f.write(f"More Info: {more_info}\n")
                print(f"File saved: {index}")


if __name__ == "__main__":
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting {time_wait} minutes...")
        time.sleep(time_wait * 60)
