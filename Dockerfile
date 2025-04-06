FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install sentence-transformers

# EXPOSE is optional on Railway, but fine to leave
EXPOSE 10000  

# Use the PORT env var Railway provides
CMD gunicorn -b 0.0.0.0:$PORT app:app
