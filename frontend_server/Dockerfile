FROM alpine:edge

WORKDIR /usr/src/app/frontend_server

RUN apk add --update py-pip

COPY requirements.txt /usr/src/app/frontend_server
RUN pip install --no-cache-dir -r /usr/src/app/frontend_server/requirements.txt

COPY *.py /usr/src/app/frontend_server/
COPY templates /usr/src/app/frontend_server/templates
COPY static /usr/src/app/frontend_server/static

EXPOSE 5000

CMD ["python3", "/usr/src/app/frontend_server/app.py"]