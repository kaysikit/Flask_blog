FROM python:3.10

WORKDIR /

COPY pyproject.toml poetry.lock /

RUN pip install poetry

COPY . .

CMD ["poetry", "run", "python", "app.py"]