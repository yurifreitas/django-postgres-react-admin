# pull the official base image
FROM python:3-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY requirements.txt /app/

#install posgres dependencies
RUN apk add --no-cache postgresql-libs 
RUN apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev

#install requeriments
RUN pip install --no-cache-dir -r requirements.txt
RUN apk --purge del .build-deps

# copy project
COPY . /app/
RUN rm -rf /app/static 
COPY ./static /var/www/app/static

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh" ]

EXPOSE 8000