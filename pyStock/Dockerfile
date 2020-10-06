FROM python:3.7

ENV PYHONUNBEFFERED 1

RUN mkdir /pystock
WORKDIR /pystock

ADD requirements.txt /pystock/

EXPOSE 8000

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ADD . /pystock/

#RUN python manage.py runserver
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pyStock.wsgi:application"]
CMD python manage.py runserver 192.168.5.121:8000
