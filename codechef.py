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

hour = dt.strftime("%I").lstrip("0")  

formatted_date = f"{get_day_with_suffix(dt.day)} {dt.strftime('%B')} {dt.year} at {hour}:{dt.strftime('%M %p')} IST"

bold_contest_name = bold_text(contest['contest_name'])
bold_Date = bold_text(f"{get_day_with_suffix(dt.day)} {dt.strftime('%B')}, {dt.strftime('%A')}, {dt.year}\n")

message = (f"Codechef {contest['contest_name']} will start on {formatted_date}.\n"
           f"Contest duration is {contest['contest_duration']} minutes.\n\n"
           f"Contest link: https://www.codechef.com/{contest['contest_code']}\n"
           "Happy Coding! 😀")

facebook_message = (f"Upcoming Contest: {bold_text('CodeChef ') +bold_contest_name}\n"
                    f"Date: {bold_Date}\n"
                    f"Contest Timing: {bold_text(str(hour))}:{bold_text(str(dt.strftime('%M %p')))} 𝐈𝐒𝐓\n"
                    f"Duration: {bold_text(str(int(contest['contest_duration'])//60))} 𝐡𝐨𝐮𝐫𝐬\n\n"
                    f"Contest link: https://www.codechef.com/{contest['contest_code']}\n"
                    "Happy Coding! 😀")

def result(option):
    if option == "whatsapp":
        print(message)
        return message
    elif option == "facebook":
        print(facebook_message)
        return facebook_message
    

result("facebook")