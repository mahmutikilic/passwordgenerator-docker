FROM python:3.8.16-slim-bullseye
LABEL version="0.1"
WORKDIR /app
COPY passgn.py /app
COPY Savedpass.txt /app
CMD python3 passgn.py