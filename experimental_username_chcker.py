import requests
import json
import webbrowser
from time import sleep
import json
from bs4 import BeautifulSoup


configs = json.load(open("config.json"))
if configs["open_name_in_namemc"] == True:
    print(f"names will be opening in namemc this session")
if configs["open_name_in_namemc"] == False:
    print(f"names will not be opening in namemc this session")
sleep(1)
failed_names = 0
available_names = 0
name_in = open("names.txt", "r")
name_out = open("namelog.txt", "a")
names = name_in.readlines()
converted_names = []
for element in names:
    converted_names.append(element.strip())
def name_is_available(name):
    global failed_names, available_names
    url = f"https://namemc.com/search?q={name}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    status_bar = soup.find(id="status-bar")
    if str(type(status_bar)) == "<class 'NoneType'>":
        print("there was an error, stopping temporarily. This is normal.")
        sleep(30)
        name_is_available(name)
        return
    info = status_bar.find_all("div", class_="col-sm-6 my-1")
    searches_per_month = info[1].text.split("\n")[2]
    status = info[0].text.split("\n")[2]
    print(f"{name} is: {status} and has {searches_per_month} searches per month")
    name_out.write(f"{name} is: {status} and has {searches_per_month} searches per month\n")
    if configs["open_name_in_namemc"] == True:
        webbrowser.open(f"https://namemc.com/search?q={name}")
    available_names += 1

def full_loop(name):
    global failed_names, available_names
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
            print(username_json)
            failed_names += 1
    except json.decoder.JSONDecodeError:
        name_is_available(name)

for name in converted_names:
    full_loop(name)

success_rate = f"{available_names / (available_names + failed_names) * 100}%"
print(f"------ you were {success_rate} succesful this time ------")
name_out.write(f"------ you were {success_rate} succesful this time ------")

name_out.close()
