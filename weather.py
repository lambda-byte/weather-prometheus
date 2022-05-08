# weather.py

# import things
from config import *
import os
import wget
from flask import Flask
import json

# make flask easy
app = Flask(__name__)

# api url
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&units=%s&appid=%s"% (latitude_value, longitude_value, unit_value, apikey)

# global json name
json_name = "weather.json"

# download function
# this checks if the file exists, and if it does it will delete it to prevent duplicates (why do you do this macOS).
def json_download():
      if os.path.exists(json_name):
            os.remove(json_name)
      wget.download(url, json_name)




# metrics route
@app.route("/metrics")
def hello_world():
    # download json
    json_download()
    # parse json
    with open(json_name) as json_data:
        data = json.load(json_data)
    # return data
    return "<p> dt = %s </p>"% (data["current"]["dt"])
