FROM python:3.5.3-slim

COPY [".", "/home/pi/Firmware/"]

WORKDIR /home/pi/Firmware/

ENV CENTRALIZER_SERVER="http://127.0.0.1:3000"
ENV SERVER_TO_FORWARD="http://127.0.0.1:4000"
ENV CHANEL_UUID="1"
ENV SOCKECTS_TIMEOUT=43200

ENTRYPOINT ["sh", "/home/pi/Firmware/entrypoints/docker-entrypoint.sh"]
