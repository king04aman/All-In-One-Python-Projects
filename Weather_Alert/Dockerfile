#BASEIMAGE

FROM python:3.7

#WORKDIR

WORKDIR /app

#COPY CODE

COPY . /app

#INSTALL LIBRARIES

RUN pip install requests python-dotenv
RUN pip install -r requirement.txt

#RUN THE APP

CMD ["python","main.py"]



