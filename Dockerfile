FROM python:3.10
COPY setup.py /home/
COPY src/ /home/
COPY requirements.txt /home/
WORKDIR /home
RUN pip3 install -e .
RUN  pip3 install -r requirements.txt
ENTRYPOINT FLASK_APP=egg/app/app.py flask run --host=0.0.0.0