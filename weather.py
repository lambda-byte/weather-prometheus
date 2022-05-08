# main.py

# time to import
from config import *
import os
import wget
from flask import Flask, json
from time import time, sleep
# make flask work
app = Flask(__name__)

# time to do things

# json url
url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&units=%s&appid=%s"% (latitude_value, longitude_value, unit_value, apikey)

# download function

def json_download():
      wget.download(url, "weather.json")
