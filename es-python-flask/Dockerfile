FROM tiangolo/uwsgi-nginx
RUN apt-get update && apt-get install -y bash nano vim

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY uwsgi.ini /app/uwsgi.ini
COPY main.py /app/main.py
COPY pytest.ini /app/pytest.ini
COPY .flake8 /app/.flake8