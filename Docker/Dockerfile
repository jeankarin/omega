FROM alpine:latest
LABEL maintainer="Juan A. Horrillo jean.karin@mail.ru"
RUN apk add --update --no-cache vim python3 py3-mysqlclient && \
    mkdir -p /opt/app && mkdir -p /opt/files
COPY euromillon/* /opt/app/
RUN chmod +x -R /opt/app/
CMD ["python3", "./opt/app/main.py"]
