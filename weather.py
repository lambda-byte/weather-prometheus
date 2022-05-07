# main.py

# time to import
import os
from flask import Flask, json
import requests
from time import time, sleep
# make flask work
app = Flask(__name__)

# time to do things
import config

# json url

url = "https://api.openweathermap.org/data/2.5/onecall?lat=" + latitude_value + "&lon={lon}&units={units}&appid="