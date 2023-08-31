FROM python:3.5.3-slim

COPY [".", "/home/pi/Firmware/"]

WORKDIR /home/pi/Firmware/

ENTRYPOINT ["sh", "/home/pi/Firmware/entrypoints/docker-entrypoint.sh"]
