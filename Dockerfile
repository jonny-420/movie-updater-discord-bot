FROM python:3.11.9

WORKDIR /bot

RUN pip install discord.py python-dotenv requests 

COPY . .

CMD ["python", "movieUpdaterBot.py"]