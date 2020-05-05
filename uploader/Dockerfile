FROM alpine:edge

WORKDIR /usr/src/app/uploader

RUN apk add --update py-pip

COPY requirements.txt /usr/src/app/uploader
RUN pip install --no-cache-dir -r /usr/src/app/uploader/requirements.txt

COPY app.py /usr/src/app/uploader
COPY login.py /usr/src/app/uploader
COPY main.py /usr/src/app/uploader
COPY uploader.py /usr/src/app/uploader
COPY utils.py /usr/src/app/uploader
COPY templates /usr/src/app/uploader/templates
COPY static /usr/src/app/uploader/static

RUN mkdir /usr/src/app/uploader/static/music

EXPOSE 5000

CMD ["python3", "/usr/src/app/uploader/app.py"]