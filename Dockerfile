FROM python:3.11.9

WORKDIR /bot

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "movieUpdaterBot.py"]