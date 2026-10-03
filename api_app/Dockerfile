FROM python:3.12.1-slim
WORKDIR /app
EXPOSE 8080

COPY requirements.txt /app/
RUN pip install --no-cache --no-cache-dir -r requirements.txt

COPY . /app/
ENTRYPOINT ["python3", "-m", "src"]
