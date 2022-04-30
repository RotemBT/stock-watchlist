FROM python:3.8

RUN mkdir /stream-service

COPY requirements.txt /stream-service

WORKDIR /stream-service

RUN apt-get update
RUN pip3 install -r requirements.txt

COPY . /stream-service/

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0","--port", "8086" ]