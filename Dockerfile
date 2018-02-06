FROM python:3

RUN pip install pillow

VOLUME /p.in
VOLUME /p.out

WORKDIR /workspace
