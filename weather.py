# weather.py

# time to import tons of stuff for some reason
from config import *
import os
import wget
from flask import Flask, json
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

# wip route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())