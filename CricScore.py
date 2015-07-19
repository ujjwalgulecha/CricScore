import requests
from bs4 import BeautifulSoup
from time import sleep
import pynotify
def popUpMessage(title, message):
        pynotify.init("Cricket Score")
        pynotify.Notification(title, message, "dialog-information").show()


Url = "http://static.cricinfo.com/rss/livescores.xml"
matchChoice = 0
score = ""
didInterrupt = False


while True:
    try:
        r = requests.get(Url)
        while r.status_code is not 200:
            r = requests.get(liveUrl)
        data = BeautifulSoup(r.text).find_all("description")
        if not matchChoice:
            print("Matches available:")
            for index, game in enumerate(data[1:], 1):
                print(index, str(game.text))
            matchChoice = int(input("Enter your choice: "))
            while True:
                if matchChoice in range(1, index):
                    break
                matchChoice = int(input("Invalid Choice. Enter your choice: "))
            didInterrupt=False
        score = data[matchChoice].text
        popUpMessage("Score", score)
        sleep(15)

    except KeyboardInterrupt:
        if didInterrupt:
            print("Bye bye")
            break
        else:
            print("Press Ctrl+C again to quit")
            matchChoice, didInterrupt = 0, True

