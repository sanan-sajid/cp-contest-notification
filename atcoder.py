from bs4 import BeautifulSoup
import lxml , requests
from datetime import datetime
import pytz


def convert_japan_to_india_time(japan_time_str):
    input_format = "%Y-%m-%d %H:%M:%S%z"
    japan_time = datetime.strptime(japan_time_str, input_format)
    india_tz = pytz.timezone("Asia/Kolkata")
    india_time = japan_time.astimezone(india_tz)
    return india_time.strftime("%Y-%m-%d %I:%M:%S %p %Z")


# Fetch the content form atcoder
url = "https://atcoder.jp/contests/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "lxml")


contestDIV=soup.find("div", {"id": "contest-table-upcoming"})
contestDIV=contestDIV.find("tbody")

def test():
    for test in contestDIV.find_all("tr"):
        anchor_tags = test.find_all("a")
        if (anchor_tags[1].text.find("Beginner")!=-1):
            return anchor_tags

res = test()

contest_num=res[1]['href'][-3]+res[1]['href'][-2]+res[1]['href'][-1]


time=convert_japan_to_india_time(res[0].text)
dt = datetime.strptime(time, "%Y-%m-%d %I:%M:%S %p IST")
formatted_date = dt.strftime("%dth %B %Y at %I:%M %p").replace("th", "th" if dt.day % 10 == 3 and dt.day != 13 else "st" if dt.day % 10 == 1 and dt.day != 11 else "nd" if dt.day % 10 == 2 and dt.day != 12 else "th")

message = (f"AtCoder Beginner Contest {contest_num} will start on {formatted_date}.\n"
           "Contest duration is 100 minutes.\n\n"
           f"Contest link: https://atcoder.jp{res[1]['href']}\n"
           "Happy Coding! 😀")

def result():
    return message


print(message)