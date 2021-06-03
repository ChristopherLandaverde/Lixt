#Docker-file, Image,Container.
FROM python:3.9

EXPOSE 5000

COPY . /flappy

WORKDIR flappy

COPY requirements.txt /flappy
RUN pip install -r requirements.txt

COPY . /src


CMD ["python","rest.py"]


