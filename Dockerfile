FROM python:3.9-alpine
COPY . /testContainer
WORKDIR /testContainer
RUN pip install -r requirements.txt 
EXPOSE 5003
CMD python ./main.py
