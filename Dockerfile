FROM python:3.9-slim-buster

WORKDIR /mnt/c/myappjfk

COPY . /mnt/c/myappjfk

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9000

CMD ["python3", "myappjfk.py"]
