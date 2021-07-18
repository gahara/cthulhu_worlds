FROM python:3.7

WORKDIR /home/game

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY app app
#COPY migrations migrations
COPY server.py config.py docker-entrypoint.sh ./

RUN chmod +x docker-entrypoint.sh

EXPOSE 5000
ENTRYPOINT ["./docker-entrypoint.sh"]