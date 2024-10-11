import requests 
from datetime import datetime

url = 'https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=all'

response = requests.get(url)

data=response.json()
contest=data['future_contests'][0]

dt = datetime.fromisoformat(contest['contest_start_date_iso'])

def get_day_with_suffix(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        return f"{day}th"
    else:
        return f"{day}{['st', 'nd', 'rd'][day % 10 - 1]}"


hour = dt.strftime("%I").lstrip("0")  

formatted_date = f"{get_day_with_suffix(dt.day)} {dt.strftime('%B')} {dt.year} at {hour}:{dt.strftime('%M %p')} IST"




message = (f"Codechef {contest['contest_name']} will start on {formatted_date}.\n"
           f"Contest duration is {contest['contest_duration']} minutes.\n\n"
           f"Contest link: https://www.codechef.com/{contest['contest_code']}\n"
           "Happy Coding! 😀")

facebook_message = (f"Upcoming Contest: 𝐂𝐨𝐝𝐞𝐂𝐡𝐞𝐟 {contest['contest_name']}\n"
                    f"Date: {dt.strftime('%d')}𝐭𝐡 {dt.strftime('%B')}, {dt.strftime('%A')}, {dt.strftime('%Y')}\n"
                    f"Contest Timing: {hour}:{dt.strftime('%M %p')} 𝐈𝐒𝐓\n"
                    f"Duration: {contest['contest_duration']} 𝐦𝐢𝐧𝐮𝐭𝐞𝐬\n\n"
                    f"Contest link: https://www.codechef.com/{contest['contest_code']}\n"
                    "Happy Coding! 😀")

def result(option):
    if option == "whatsapp":
        print(message)
        return message
    elif option == "facebook":
        print(facebook_message)
        return facebook_message