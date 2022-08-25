FROM python:3.9

RUN mkdir code
WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip
RUN pip install  -r /code/requirements.txt

COPY ./app /code

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
