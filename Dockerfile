FROM python:3.9-alpine
COPY . /test-container
WORKDIR /test-container
RUN pip install -r requirements.txt 
EXPOSE 5003
CMD python ./main.py
