import requests 
from datetime import datetime

url = 'https://www.codechef.com/api/list/contests/all?sort_by=START&sorting_order=asc&offset=0&mode=all'

response = requests.get(url)

data=response.json()
contest=data['future_contests'][0]
print(contest)

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

print(message)