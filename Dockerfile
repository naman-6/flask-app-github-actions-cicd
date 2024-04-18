FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

RUN python3 -m pytest

CMD ["python3", "main.py"]


