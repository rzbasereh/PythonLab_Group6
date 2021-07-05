FROM ubuntu

RUN apt-get update && apt-get install -y python3

ADD server.py /app/server.py

CMD ["python3", "/app/server.py"]

EXPOSE 3000