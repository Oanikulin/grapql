FROM python:3.8

COPY . .

RUN pip install -r requirements.txt

CMD ["bash", "-c", "python -m flask run --host=0.0.0.0"]