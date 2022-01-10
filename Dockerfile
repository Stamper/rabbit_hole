FROM python:3.8-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN mkdir -p /output
WORKDIR /app
COPY requirements-server.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY /server/ /app