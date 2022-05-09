FROM python:3.10

RUN addgroup --gid 1000 server && adduser --uid 1000 --gid 1000 --system server
WORKDIR /home/weather

RUN pip3 install gunicorn wget python-dotenv flask

USER server

# Finally, copy the entire source.
COPY . .

ENV FLASK_APP weather.py
EXPOSE 5025
ENTRYPOINT ["gunicorn", "-b", ":5025", "--access-logfile", "-", "--error-logfile", "-", "weather:app"]
