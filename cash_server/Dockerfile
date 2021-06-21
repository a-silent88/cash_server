#FROM fastapi:1.1
FROM python:3.6
COPY / /
COPY requirements.txt requirements.txt

RUN apt-get -y update

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5037:5037

CMD ["python", "main.py"]