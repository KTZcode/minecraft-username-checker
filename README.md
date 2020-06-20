# minecraft username checker

This simple Python script will check, from a list of names, if any of them are available. If any are, it will open them in [namemc.com](https://namemc.com/) (if you want them to) on a new tab in your web browser for you to confirm if they are truly available or just "available soon."

### Requirements:
- [Python 3](https://www.python.org/)
- [Python requests module](https://requests.readthedocs.io/en/master/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) (for `experimental_username_checker.py`)


### usage:
- put a list of names you want to check in the "names.txt" file (there is no limit but if you have it open the names on namemc you might run out of ram.)
- add
```json
    {
        "open_name_in_namemc": true or false,
        "min_likes_to_save": integer,
        "save_available_later_names": true or false
    }
```
 to a file named `config.json` file in the root directory of this project (This will decided whether or not the names will be opened on namemc.) Note: "min_likes_to_save" and "save_available_later_names" only matter for `experimental_username_checker.py` because I have not implemented it into `username_ckecker.py`.
-  run `username_checker.py` or `experimental_username_checker.py` and it will output to `namelog.txt`.

### Other info:
I've only really left `username_ckecker.py` because it is so much faster but I strongly encourage using `experimental_username_checker.py` because it can be used with more effectively with a large number of names.  `experimental_username_checker.py` will require [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to run because it will scrape data (*True* availability and searches / month) from [namemc](https://namemc.com/), print it out, and write it in `namelog.txt`. It *is* slower but I recommend it when checking a large number of names.
If you have any issues with the script please open an issue and I will try to get back as soon as possible.
### config examples
If I were to run this script using [the set of words below](https://github.com/dwyl/english-words) then I would recommend running `experimental_username_checker.py` with a config like this:
```json
    {
        "open_name_in_namemc": false,
        "min_likes_to_save": 1,
        "save_available_later_names": true
    }
```
because you don't want that many names opening in namemc, most of the names will be bad so you want to ensure that they get at least 1 search per month, and that the available soon names are saved because there will be very few of those which probably will become available and not get sniped quickly. Or, if you are using a set of common or short names then you might want a config where it doesn't save "available later" names because there would be a lot of those and you are just looking for the currently available.

#### Resources:
For finding words to check I recommend [this](https://github.com/dwyl/english-words) GitHub repository because there are a *TON* of words and they are already correctly formatted.

> Note: I have little experience with programming and this may be a very inefficient way of doing this, I don't know.
