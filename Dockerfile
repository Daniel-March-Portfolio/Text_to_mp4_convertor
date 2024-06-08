FROM python:3.11-alpine

WORKDIR /app

RUN apk update
RUN apk add imagemagick
RUN apk add ffmpeg
RUN apk add imagemagick
RUN apk add ttf-dejavu
RUN apk add py3-pillow

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY Main Main
COPY TextToMP4 TextToMP4
COPY manage.py manage.py
RUN python manage.py migrate

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]