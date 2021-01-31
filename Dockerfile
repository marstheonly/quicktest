FROM python:3.9.1-buster

RUN apt update -y

WORKDIR /app

COPY myserver.py /app

RUN pip --no-cache-dir install requests flask-restful

EXPOSE 4999

ENTRYPOINT ["python3"]
CMD ["myserver.py"]
