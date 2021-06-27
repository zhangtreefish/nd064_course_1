FROM python:3.9
LABEL maintainer="shuyu"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# command to run on container start
CMD [ "python3", "app.py" ]