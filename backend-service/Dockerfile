FROM python:3.8

RUN mkdir /backend-service

COPY requirements.txt /backend-service

WORKDIR /backend-service

RUN apt-get update
RUN pip3 install -r requirements.txt

COPY . /backend-service/
RUN pytest test_main.py
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0","--port", "8085"]