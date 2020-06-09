import requests
import json
import webbrowser


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
        print(username_json)
    except json.decoder.JSONDecodeError:            
        print(f"{name} is available")
        name_out.write(f"{name}\n")
        webbrowser.open(f"https://namemc.com/search?q={name}")

name_out.close()