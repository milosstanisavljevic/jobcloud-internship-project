FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install-deps
RUN playwright install chromium

COPY . .

CMD [ "python", "crawler.py", "1180" ]