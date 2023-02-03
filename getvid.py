import requests
import re
from win11toast import toast
from time import sleep
import getpass
import os
USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" "%s"' % file_path)


def lookup(channel):
    prefix = "https://www.youtube.com/@"
    html = requests.get(prefix + channel + "/videos").text
    info = re.search('(?<={"label":").*?(?="})', html).group()
    url = "https://www.youtube.com/watch?v=" + \
        re.search('(?<="videoId":").*?(?=")', html).group()
    days = re.search('by .* (\d) days', info).group(1)
    creator = re.search('by (\D*) \d', info).group(1)
    title = re.search('(^.*) by', info).group(1)

    def check_days(title, creator, url, days):
        if int(days, 10) <= 7:
            toast(f"New Video by {creator}: {title}", url, on_click=f"{url}")

    check_days(title, creator, url, days)



lookup("Phreak")
sleep(5)
lookup("BrokenByConcept")
