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
RUN chmod +x entrypoint.sh
#RUN entrypoint.sh
# command to run on container start

#CMD [ "flask", "run", "--host", "0.0.0.0" ]

ENTRYPOINT /app/entrypoint.sh ; cd UI && flask run --host 0.0.0.0 

