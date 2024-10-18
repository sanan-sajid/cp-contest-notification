import requests 
import time
import datetime

url='https://codeforces.com/api/contest.list'

response = requests.get(url)
response.raise_for_status()
data=response.json()
data=data['result']
contest={}
for contests in data:
    if(contests['phase']=="FINISHED"):
        break
    if(contests['type']!="CF"):
        continue
    contest=contests

# print(contest)

unix_timestamp=contest['startTimeSeconds']
utc_time = datetime.datetime.utcfromtimestamp(unix_timestamp)

ist_time = utc_time + datetime.timedelta(hours=5, minutes=30)

formatted_time = ist_time.strftime('%d') + (
    'th' if 4 <= int(ist_time.strftime('%d')) <= 20 else
    {1: 'st', 2: 'nd', 3: 'rd'}.get(int(ist_time.strftime('%d')) % 10, 'th')
) + ist_time.strftime(' %B %Y at %I:%M %p IST')

# Convert durationSeconds into hours and minutes
duration_seconds = contest['durationSeconds']
hours = duration_seconds // 3600
minutes = (duration_seconds % 3600) // 60
formatted_duration = f"{hours} hours" if minutes == 0 else f"{hours} hours {minutes} minutes"

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

message = (f"{contest['name']} will start on {formatted_time}.\n"
           f"Contest duration is {formatted_duration}.\n\n"
           f"Contest link: https://codeforces.com/contests/{contest['id']}\n"
           "Happy Coding! 😀")

facebook_message = (f"Upcoming Contest: {bold_text(str(contest['name']))}\n"
                    f"Date: {bold_text(str(ist_time.strftime('%d')))}𝐭𝐡 {bold_text(str(ist_time.strftime('%B')))}, {bold_text(str(ist_time.strftime('%A')))}, {bold_text(str(ist_time.strftime('%Y')))}\n"
                    f"Contest Timing: {bold_text(str(ist_time.strftime('%I:%M %p')))} 𝐈𝐒𝐓\n"
                    f"Duration: {bold_text(formatted_duration)}\n\n"
                    f"Contest link: https://codeforces.com/contest/{contest['id']}\n"
                    "Happy Coding! 😀")

def result(option):
    if option == "whatsapp":
        print(message)
        return message
    elif option == "facebook":
        print(facebook_message)
        return facebook_message
    
result("facebook")
result("whatsapp")
