FROM python:3.9-alpine
COPY . /stAItus
WORKDIR /stAItus
RUN pip install -r requirements.txt 
CMD python ./main.py