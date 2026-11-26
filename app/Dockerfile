FROM python:3.12-slim

WORKDIR /app

COPY requirements-dev.txt /app/requirements-dev.txt
RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . /app

CMD ["python", "-m", "flask", "--app", "app", "run", "--port", "8000"]
