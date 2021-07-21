FROM python:3.8

WORKDIR .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1


COPY developerrequirements.txt .
RUN pip install -r developerrequirements.txt

COPY . .