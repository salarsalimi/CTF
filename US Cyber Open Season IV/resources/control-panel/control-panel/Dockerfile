FROM python:3-alpine

# Create app directory
WORKDIR /www

# Install app dependencies
RUN pip install flask
RUN apk add curl supervisor

COPY config/destroy_humans.sh .
COPY config/supervisord.conf /etc/supervisord.conf
COPY config/destroyer.py /root/destroyer.py

COPY challenge ./challenge
COPY run.py .

RUN chmod +x destroy_humans.sh
# RUN chmod +x docker_entrypoint.sh

EXPOSE 9999
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]