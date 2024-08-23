FROM python:3.9-slim

WORKDIR /cybersecurity_news_collector
COPY requirements.txt /cybersecurity_news_collector
RUN pip install --no-cache-dir -r requirements.txt

COPY . /cybersecurity_news_collector
CMD [ "python", "main.py" ]