FROM python:3.8

WORKDIR .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1


COPY dev_requirements.txt .
RUN pip install -r dev_requirements.txt

COPY . .