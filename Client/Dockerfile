FROM python:3.7-alpine 
RUN pip install pika
RUN mkdir -p /src/deploy
WORKDIR /src/deploy
COPY ThesisWork .
CMD ["python","./StartClient.py"]

