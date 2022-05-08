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

    # display data
    return "<pre># unix time from last json download <br>" \
            "weather_scrape_dt %s <br>" \
            "# current temp <br>" \
            "current_temp %s <br>" \
            "# what it feels like outside <br>" \
            "current_feels_like %s <br>" \
            "# wind speed <br>" \
            "current_wind_speed %s <br>" \
            "# dew point <br>" \
            "current_dew_point %s <br>" \
            "# weather description <br>" \
            "weather_description %s <br>"\
            "# latest precipitation <br>" \
            "latest_precipitation %s <br>" \
            "# 7 day forcast <br>" \
            "day_0_day_temp %s <br>" \
            "day_1_day_temp %s <br>" \
            "day_2_day_temp %s <br>" \
            "day_3_day_temp %s <br>" \
            "day_4_day_temp %s <br>" \
            "day_5_day_temp %s <br>" \
            "day_6_day_temp %s <br>" \
            "day_7_day_temp %s <br>" \
            "# 7 day min temp <br>"  \
            "day_0_min_temp %s <br>" \
            "day_1_min_temp %s <br>" \
            "day_2_min_temp %s <br>" \
            "day_3_min_temp %s <br>" \
            "day_4_min_temp %s <br>" \
            "day_5_min_temp %s <br>" \
            "day_6_min_temp %s <br>" \
            "day_7_min_temp %s <br>" \
            "# 7 day max temp <br>"  \
            "day_0_max_temp %s <br>" \
            "day_1_max_temp %s <br>" \
            "day_2_max_temp %s <br>" \
            "day_3_max_temp %s <br>" \
            "day_4_max_temp %s <br>" \
            "day_5_max_temp %s <br>" \
            "day_6_max_temp %s <br>" \
            "day_7_max_temp %s </pre>" \
           %  (data["current"]["dt"], data["current"]["temp"], data["current"]["feels_like"], data["current"]["wind_speed"],
               data["current"]["dew_point"], data["current"]["weather"][0]["description"], data["minutely"][0]["precipitation"],
               data["daily"][0]["temp"]["day"], data["daily"][1]["temp"]["day"], data["daily"][2]["temp"]["day"], data["daily"][3]["temp"]["day"],
               data["daily"][4]["temp"]["day"], data["daily"][5]["temp"]["day"], data["daily"][6]["temp"]["day"], data["daily"][7]["temp"]["day"],
               data["daily"][0]["temp"]["day"], data["daily"][1]["temp"]["min"], data["daily"][2]["temp"]["min"], data["daily"][3]["temp"]["min"],
               data["daily"][4]["temp"]["min"], data["daily"][5]["temp"]["min"], data["daily"][6]["temp"]["min"], data["daily"][7]["temp"]["min"],
               data["daily"][0]["temp"]["max"], data["daily"][1]["temp"]["max"], data["daily"][2]["temp"]["max"], data["daily"][3]["temp"]["max"],
               data["daily"][4]["temp"]["max"], data["daily"][5]["temp"]["max"], data["daily"][6]["temp"]["max"], data["daily"][7]["temp"]["max"])
