# weather.py

# time to import tons of stuff for some reason
from config import *
import os
import wget
from flask import Flask
import json
import atexit
from apscheduler.schedulers.background import BackgroundScheduler

# make flask work
app = Flask(__name__)

# make BackgroundScheduler easy
scheduler = BackgroundScheduler()

# time to do things

# json url
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&units=%s&appid=%s"% (latitude_value, longitude_value, unit_value, apikey)

# global json name
json_name = "weather.json"

# download function
# this checks if the file exists, and if it does it will delete it to prevent duplicates (why do you do this macOS).
def json_download():
      if os.path.exists(json_name):
            os.remove(json_name)
      wget.download(url, json_name)

json_download()

scheduler.add_job(func=json_download, trigger="interval", seconds=int(scrape_time_value))
scheduler.start()

with open(json_name) as json_data:
    data = json.load(json_data)



# wip route
@app.route("/metrics")
def hello_world():
    return str(data ["current"])



# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())