FROM python:3.8.1-slim-buster

WORKDIR /app 

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y ffmpeg
RUN pip install pytube


COPY . /app 

CMD ["python3","main.py"]