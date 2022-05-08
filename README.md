# weather-prometheus
Send weather info to prometheus with python.
Using OpenWeather One Call API https://openweathermap.org/api/one-call-api

You need an OpenWeather API Key https://openweathermap.org/price




# How to run
You need to fill in data in ```config-example.py``` and rename it to ```config.py``` before you run it

## Flask

Things you need to install
```
pip install flask wget python-dotenv
```

To run with Flask first clone the repo
```
git clone https://github.com/lambda-byte/weather-prometheus.git
```

Enter the directory
```
cd weather-prometheus
```

Then run it with flask
```
flask --host 0.0.0.0 --port 5025
```


## Docker using docker-compose

Download docker-compose.yml and config-example.py
```
wget https://raw.githubusercontent.com/lambda-byte/weather-prometheus/main/docker-compose.yml
wget https://raw.githubusercontent.com/lambda-byte/weather-prometheus/main/config-example.py
```

Fill in data in config-example.py then rename it to config.py

Start container
```
docker-compose up
```
