FROM python:3.9
WORKDIR /app
COPY app.py /app
EXPOSE 8080
CMD ["python", "app.py"]
