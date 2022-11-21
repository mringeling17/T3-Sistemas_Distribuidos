FROM python:3.9.6-slim-buster

WORKDIR /cliente

COPY requirements.txt /cliente

RUN python3 -m pip install -r requirements.txt

EXPOSE 8000

COPY . .

CMD ["flask","run"]