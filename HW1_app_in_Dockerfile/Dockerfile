FROM python:latest

LABEL Maintainer = "Egor Kuts"
LABEL version = 0.0.1

COPY server.py index.html /

ENV port 7001

ENTRYPOINT [ "python", "server.py" ]
CMD [ "${port}" ]