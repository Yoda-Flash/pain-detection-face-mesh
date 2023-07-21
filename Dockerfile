FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY modules .

CMD ["python3", "-m", "run", "--host=0.0.0.0", "--port=7860"]