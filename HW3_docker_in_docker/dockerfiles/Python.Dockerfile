FROM python:latest
COPY index.html /
EXPOSE 7000
CMD python -m http.server 7000 --bind 127.0.0.1
#CMD [ 'python', '-m', 'http.server', '--bind', '127.0.0.1', '7000' ]