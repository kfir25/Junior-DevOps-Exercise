FROM python:3.8-alpine3.10

WORKDIR /app
COPY requirements.txt requirements.txt
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev
# RUN apk add mariadb-dev python3-dev build-deps
# RUN pip3 install mysql-connector
# RUN pip3 install mysql-connector-python
# RUN pip3 install pymysql
# RUN pip3 install flask-mysqldb
RUN pip3 install -r requirements.txt
COPY . .
#have a dockerignore file
ENV FLASK_APP=app
WORKDIR /app/app

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0" ]
