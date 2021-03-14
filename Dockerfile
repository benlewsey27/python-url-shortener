FROM python:3.9-slim
WORKDIR /opt

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .

EXPOSE 3000
CMD ["python", "./server.py"]
