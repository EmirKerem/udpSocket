import socket
import datetime
import requests
from random import randint

def returning(msg):
    msg = (str(msg)).lower()

    # for historical events
    today = datetime.date.today()
    month = today.month
    day = today.day
    url = "https://byabbe.se/on-this-day/"+month+"/"+day+"/events.json"
    ans = requests.get(url)
    data = ans.json()
    firstEvent = data["events"][0]
    lastEvent = data["events"][-1]

    # for forecast in Istanbul
    url2 = "https://api.open-meteo.com/v1/forecast?latitude=41.01&longitude=28.97&current_weather=true"
    ansWeather = requests.get(url2)
    dataWeather = ansWeather.json()
    weather = dataWeather.get("current_weather",{})
    temp = weather.get("temperature")
    description = "At the moment weather in Istanbul is "+str(temp)+"°C"

    if "happened" in msg or "history" in msg:
        return data["events"][randint(firstEvent,lastEvent)]
    elif "weather" in msg or "temperature" in msg or "Istanbul" in msg:
        return description

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('127.0.0.1', 2424))

print("Server is ACTIVE")

while True:
    data, addr = server.recvfrom(1024)
    print("Connection to ", addr)

    ans = returning(data.decode())
    server.sendto(ans.encode(), addr)


server.close() # Not necessery

