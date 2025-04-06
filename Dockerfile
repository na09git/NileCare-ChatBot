FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install sentence-transformers  # Ensure this is installed

EXPOSE 10000

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
