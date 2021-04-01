import getpass
import webbrowser
import winsound
import time
from datetime import datetime
username = getpass.getuser()
def alert(url):
    if url != "":
        webbrowser.open(url)
    for i in range(3):
        winsound.Beep(2500, 1000)
        time.sleep(1)
oldmin = 0
while True:
    try:
        file = open("C:/Users/"+username+"/Documents/alarms.txt","r")
        alarms = [[int(j) for j in i.split(" ")[:-1]]+[i.split(" ")[-1]] for i in file.read().split("\n")]
        file.close()
    except:
        try:
            file.close()
        except:
            break
        alarms = []
    now = datetime.now()
    try:
        pos = [i[:-1] for i in alarms].index([now.hour, now.minute])
    except:
        pos = -1
    if pos >= 0:
        alert(alarms[pos][-1])
    else:
        weekday = now.weekday()
        try:
            print([now.hour, now.minute] in [i[-3:-1] for i in alarms if weekday in i[:-3]])
            pos = [i[-3:-1] for i in alarms if weekday in i[:-3]].index([now.hour, now.minute])
            print(pos)
        except:
            pos = -1
        if pos >= 0:
            alert(alarms[pos][-1])
    time.sleep(56)
    oldmin = now.minute
