FROM python:3.8

ADD apka.py .

RUN pip install flask flask_restful

CMD [ "python", "./apka.py" ]