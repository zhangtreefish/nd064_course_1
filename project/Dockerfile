# syntax=docker/dockerfile:1
# use 3.8 instead of deprecated 2.7
FROM python:3.8
# set ENV to enable logging
ENV FLASK_ENV=development
# set the default directory for the container
WORKDIR /app

COPY techtrends/ .

RUN pip3 install -r requirements.txt
RUN python3 init_db.py

CMD [ "python3", "app.py"]