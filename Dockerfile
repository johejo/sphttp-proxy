FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install git+https://github.com/johejo/sphttp.git && \
    pip install -U git+https://github.com/Lukasa/hyper.git

COPY ./app /app
