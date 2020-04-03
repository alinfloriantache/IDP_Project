FROM alpine:edge

WORKDIR /usr/src/app/backend_server

RUN apk add --update py-pip

COPY requirements.txt /usr/src/app/backend_server
RUN pip install --no-cache-dir -r /usr/src/app/backend_server/requirements.txt

COPY app.py /usr/src/app/backend_server
COPY templates/index.html /usr/src/app/backend_server/templates/index.html
COPY static/Work-In-Progress.png /usr/src/app/backend_server/static/Work-In-Progress.png

EXPOSE 5000

CMD ["python3", "/usr/src/app/backend_server/app.py"]