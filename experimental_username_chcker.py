import requests
import json
import webbrowser
from time import sleep
import json
from bs4 import BeautifulSoup
import datetime

configs = json.load(open("config.json"))
if configs["open_name_in_namemc"] == True:
    print(f"names will be opening in namemc this session")
if configs["open_name_in_namemc"] == False:
    print(f"names will not be opening in namemc this session")

available_later = 0
failed_names = 0
available_names = 0
name_in = open("names.txt", "r")
name_out = open("namelog.txt", "a")
names = name_in.readlines()
converted_names = []
sleep(1)


for element in names:
    converted_names.append(element.strip())

number_of_names = len(converted_names)
print(f"checking {number_of_names} names starting now")

def name_is_available(name):
    global failed_names, available_names, available_later
    url = f"https://namemc.com/search?q={name}"
    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
    except:
        print("--- could not get webpage from namemc, pausing for 1 minute. ---")
        sleep(60)
        name_is_available(name)
    status_bar = soup.find(id="status-bar")
    if str(type(status_bar)) == "<class 'NoneType'>":
        print("---- Too many requests have been sent to namemc, pausing for 40 seconds. ----")
        sleep(40)
        name_is_available(name)
        return
    info = status_bar.find_all("div", class_="col-sm-6 my-1")
    searches_per_month = info[1].text.split("\n")[2].split(" ")[0]
    status = info[0].text.split("\n")[2]
    if int(searches_per_month) >= configs["min_likes_to_save"]:
        do_not_include = ["unavailable", "too short", "too long", "invalid characters"]
        if configs["save_available_later_names"] == False:
            do_not_include.append("available later*")
        if status.lower() not in do_not_include:
            available_names += 1
            name_out.write(f"{name} is: {status} and has {searches_per_month} searches per month\n")
        elif status.lower() == "available later*":
            available_later += 1
    print(f"{name} is: {status} and has {searches_per_month} searches per month")
    if configs["open_name_in_namemc"] == True:
        webbrowser.open(f"https://namemc.com/search?q={name}")


def full_loop(name):
    global failed_names, available_names, available_later
    try:
        r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    except:
        print("--- could not get data from mojang, pausing for 1 minute and trying again ---")
        sleep(60)
        r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    try:
        username_json = json.loads(r.text)
        if username_json == {'error': 'TooManyRequestsException', 'errorMessage': 'The client has sent too many requests within a certain amount of time'}:
            print("too many requests have been sent... stopping for 10 minutes.")
            sleep(599)
            full_loop(name)
            print("waited for 10 minutes")
            sleep(1)
        elif username_json != {'error': 'TooManyRequestsException', 'errorMessage': 'The client has sent too many requests within a certain amount of time'}:
            print(f"{name} is unavailable")
            failed_names += 1
    except json.decoder.JSONDecodeError:
        name_is_available(name)


for name in converted_names:
    full_loop(name)


success_rate = f"{available_names / (available_names + failed_names) * 100}%"
available_later_rate =  f"{available_later / number_of_names}%"
print(f"\n\n------ you were {success_rate} succesful this time. ------")
print(f"{available_later_rate} of the names were available later")
print(f"checked {number_of_names} name(s).")
print(f"finished at {datetime.datetime.now().replace(microsecond=0)}.")
name_out.write(f"\n\n------ finished at {datetime.datetime.now().replace(microsecond=0)}. ------\n")
name_out.write(f"you were {success_rate} succesful this time.\n")
name_out.write(f"checked {number_of_names} names.")


name_out.close()
