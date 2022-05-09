FROM python:3.10


WORKDIR /home/weather

RUN pip3 install gunicorn wget python-dotenv flask

# Finally, copy the entire source.
COPY . .

ENV FLASK_APP weather.py
EXPOSE 5025
ENTRYPOINT ["gunicorn", "-b", ":5025", "--access-logfile", "-", "--error-logfile", "-", "weather:app"]
