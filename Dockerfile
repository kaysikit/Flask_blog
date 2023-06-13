FROM python:3.10

WORKDIR /flask_blog

COPY pyproject.toml poetry.lock ./

RUN pip install poetry && \
    poetry install --no-cache-dir

COPY . .

CMD ["poetry", "run", "python", "app.py"]