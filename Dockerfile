FROM python:3.8.18-slim-bullseye

COPY [".", "/home/pi/Firmware/"]

WORKDIR /home/pi/Firmware/

ENV CENTRALIZER_SERVER="http://localhost:80"
ENV WSS_CENTRALIZER_SERVER="ws://localhost:80/cable"
ENV SERVER_TO_FORWARD="http://localhost:4000"
ENV CHANEL_UUID="1"
ENV SOCKECTS_TIMEOUT=43200

ENTRYPOINT ["sh", "/home/pi/Firmware/entrypoints/docker-entrypoint.sh"]
