FROM python:3.6-slim

## set
RUN mkdir /root/.ssh/
ARG SSH_PRIVATE_KEY
ARG SSH_PUBLIC_KEY
ARG KNOWN_HOSTS
RUN echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa
RUN echo "${SSH_PUBLIC_KEY}" > /root/.ssh/id_rsa.pub
RUN echo "${KNOWN_HOSTS}" > /root/.ssh/known_hosts
RUN chmod -R 700 /root/.ssh

##todo
RUN apt-get update && apt-get install -y git 
WORKDIR /app
COPY . .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

##end
RUN rm -rf /root/.ssh