FROM python:3.8
LABEL maintainer="Visual Velocity"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install net-tools -y
EXPOSE 5000

# command to run on container start
CMD [ "/bin/bash" ]
CMD [ "flask","run","--host","0.0.0.0" ]


