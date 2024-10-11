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

def bold_text(text):
    bold_map = {
        'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅', 'G': '𝐆', 'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 
        'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍', 'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 
        'U': '𝐔', 'V': '𝐕', 'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙', 'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 
        'e': '𝐞', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡', 'i': '𝐢', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧', 
        'o': '𝐨', 'p': '𝐩', 'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭', 'u': '𝐮', 'v': '𝐯', 'w': '𝐰', 'x': '𝐱', 
        'y': '𝐲', 'z': '𝐳', '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑', '4': '𝟒', '5': '𝟓', '6': '𝟔', '7': '𝟕', 
        '8': '𝟖', '9': '𝟗'
    }
    return ''.join(bold_map.get(char, char) for char in text)
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

facebook_message = (f"Upcoming Contest: 𝐀𝐭𝐂𝐨𝐝𝐞𝐫 𝐁𝐞𝐠𝐢𝐧𝐧𝐞𝐫 𝐂𝐨𝐧𝐭𝐞𝐬𝐭 {bold_text(str(contest_num))}\n"
                    f"Date: {bold_text(str(dt.strftime('%d')))}𝐭𝐡 {bold_text(str(dt.strftime('%B')))}, {bold_text(str(dt.strftime('%A')))}, {bold_text(str(dt.strftime('%Y')))}\n"
                    f"Contest Timing: {bold_text(str(dt.strftime('%I:%M %p')))} 𝐈𝐒𝐓\n"
                    "Duration: 𝟏𝟎𝟎 𝐦𝐢𝐧𝐮𝐭𝐞𝐬\n\n"
                    f"Contest link: https://atcoder.jp{res[1]['href']}\n"
                    "Happy Coding! 😀")




def result(option):
    if option == "whatsapp":
        print(message)
        return message
    elif option == "facebook":
        print(facebook_message)
        return facebook_message

result("facebook")