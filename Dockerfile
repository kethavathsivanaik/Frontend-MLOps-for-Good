FROM python:3.8
LABEL maintainer="Visual Velocity"

COPY . /app
WORKDIR /app
RUN mkdir model
RUN mkdir images
RUN mkdir predicted
RUN mkdir script
RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install net-tools -y
EXPOSE 5000

# command to run on container start
CMD [ "/bin/bash" ]
CMD [ "./entrypoint.sh" ]


