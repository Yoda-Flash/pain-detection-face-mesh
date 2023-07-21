FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "launch.py"]