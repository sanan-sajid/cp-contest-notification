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

# print(formatted_time)

message = (f"{contest['name']} will start on {formatted_time}.\n"
           f"Contest duration is {contest['durationSeconds']/(3600)} hours.\n\n"
           f"Contest link: https://codeforces.com/contests/{contest['id']}\n"
           "Happy Coding! 😀")

facebook_message = (f"Upcoming Contest: 𝐂𝐨𝐝𝐞𝐅𝐨𝐫𝐜𝐞𝐬 {contest['name']}\n"
                    f"Date: {ist_time.strftime('%d')}𝐭𝐡 {ist_time.strftime('%B')}, {ist_time.strftime('%A')}, {ist_time.strftime('%Y')}\n"
                    f"Contest Timing: {ist_time.strftime('%I:%M %p')} 𝐈𝐒𝐓\n"
                    f"Duration: {contest['durationSeconds'] / 3600:.1f} 𝐡𝐨𝐮𝐫𝐬\n\n"
                    f"Contest link: https://codeforces.com/contest/{contest['id']}\n"
                    "Happy Coding! 😀")

def result(option):
    if option == "whatsapp":
        print(message)
        return message
    elif option == "facebook":
        print(facebook_message)
        return facebook_message