FROM python:3.12-rc-slim-buster
WORKDIR /app
COPY . /app
RUN apt update -y && apt install awscli -y

RUN apt-get update && pip install -r requirrements.txt
CMD [ "python3", "app.py" ]