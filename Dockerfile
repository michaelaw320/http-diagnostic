FROM python:3.8.1-alpine3.11

COPY main.py /main.py

EXPOSE 80

ENTRYPOINT ["python", "/main.py"]
