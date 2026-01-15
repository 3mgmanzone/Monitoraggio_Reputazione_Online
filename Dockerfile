FROM python:3.10-slim
WORKDIR /app
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV GRADIO_SERVER_NAME="0.0.0.0"
EXPOSE 8080
CMD ["python", "app.py"]
