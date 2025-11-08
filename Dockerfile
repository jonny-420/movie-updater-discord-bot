FROM python:3.11.9

WORKDIR /bot

RUN pip install discord.py python-dotenv requests psycopg2 

COPY . .

CMD ["python", "movieUpdaterBot.py"]