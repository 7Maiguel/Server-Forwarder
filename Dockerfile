FROM python:3.8.18-slim-bullseye

COPY [".", "/home/pi/Firmware/"]

WORKDIR /home/pi/Firmware/

ENV CENTRALIZER_SERVER="https://prod-migration.fusepong.com"
ENV WSS_CENTRALIZER_SERVER="wss://prod-migration.fusepong.com/cable"
ENV SERVER_TO_FORWARD="http://192.168.0.27:4000"
ENV CHANEL_UUID="6"
ENV SOCKECTS_TIMEOUT=43200

ENTRYPOINT ["sh", "/home/pi/Firmware/entrypoints/docker-entrypoint.sh"]
