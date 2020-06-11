import requests
import json
import webbrowser
from time import sleep

failed_names = 0
available_names = 0
name_in = open("names.txt", "r")
name_out = open("namelog.txt", "a")
names = name_in.readlines()
converted_names = []
for element in names:
    converted_names.append(element.strip())

for name in converted_names:
    r = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{name}")
    try:
        username_json = json.loads(r.text)
        if username_json == {'error': 'TooManyRequestsException', 'errorMessage': 'The client has sent too many requests within a certain amount of time'}:
            print("too many requests have been sent... stopping for 10 minutes.")
            sleep(600)
            print("waited for 10 minutes")
        elif username_json != {'error': 'TooManyRequestsException', 'errorMessage': 'The client has sent too many requests within a certain amount of time'}:
            print(username_json)
            failed_names += 1
    except json.decoder.JSONDecodeError:            
        print(f"{name} is available")
        name_out.write(f"{name}\n")
        webbrowser.open(f"https://namemc.com/search?q={name}")
        available_names += 1


success_rate = f"{available_names / (available_names + failed_names) * 100}%"
print(f"{success_rate} is the success rate")
name_out.write(f"------ you were {success_rate} succesful this time ------") 

name_out.close()