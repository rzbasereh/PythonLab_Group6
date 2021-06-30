FROM ubuntu

RUN apt-get update && apt-get install -y python3

ADD server.py /app/server.py

CMD ["python3", "/app/server.py"]

EXPOSE 3000

# build container:
#   $ sudo docker build -t my-server .
# run container:
#   $ sudo docker run -itp3000:3000 -v ~/Pictures:/app/images  my-server