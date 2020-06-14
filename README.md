# minecraft username checker

This simple Python script will check, from a list of names, if any of them are available. If any are, it will open them in [namemc.com](https://namemc.com/) (if you want them to) on a new tab in your web browser for you to confirm if they are truly available or just "available soon."

### Requirements:
- [python](https://www.python.org/)
- [Python requests module](https://requests.readthedocs.io/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (for `experimental_username_checker.py`)


### usage:
- put a list of names you want to check in the "names.txt" file (there is no limit but if you have it open the names on namemc you might run out of ram.)
- add `{"open_name_in_namemc": true or false}` to a file named `config.json` file in the root directory of this project (This will decided whether or not the names will be opened on namemc.)
-  run `username_checker.py` or `experimental_username_checker.py` and it will output to `namelog.txt`.

### Other info:
`experimental_username_checker.py` will require [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to run because it will scrape data (*True* availability and searches / month) from [namemc](https://namemc.com/), print it out, and write it in `namelog.txt`.
If you have any issues with the script please open an issue and I will try to get back as soon as possible. 

#### Resources:
For finding words to check I recommend [this](https://github.com/dwyl/english-words) GitHub repository because there are a *TON* of words and they are already correctly formatted.

> Note: I have little experience with programming and this may be a very inefficient way of doing this, I don't know.
