# syntax=docker/dockerfile:1
# use 3.8 instead of deprecated 2.7
FROM python:3.8

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 init_db.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]