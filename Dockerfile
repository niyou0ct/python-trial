FROM python:3

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

# EXPOSE 80

# CMD ["python3", "main.py"]
