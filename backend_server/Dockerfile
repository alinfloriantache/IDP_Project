FROM alpine:edge

WORKDIR /usr/src/app/backend_server

RUN apk add --update py-pip

COPY requirements.txt /usr/src/app/backend_server
RUN pip install --no-cache-dir -r /usr/src/app/backend_server/requirements.txt

COPY *.py /usr/src/app/backend_server/

EXPOSE 5000

CMD ["python3", "/usr/src/app/backend_server/app.py"]