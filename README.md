# movie-updater-discord-bot

# Description

This is a discord bot intended to notify users in a server with the upcoming movies releasing in theathers. It allows users to subscribe to specific movie genres, and receiver a more tailored response based on subscribed genres.

# Used technologies

- Programming languages
  - python
- Frameworks
  - Discord.py
- Databases
  - PostgreSQL
- Infrastrucuture
  - Docker (Docker Compose)
  - Cron (Scheduled ETL pipeline)
  - RabbitMQ

# Database

![Movie Bot Entity Relation](./Documentation/Bot-Db-ER.png)

The above image shows the design entity relation model for the bot database. All the movie information was fetched from the TMDB movie API.

- member: Represents the members that have a specific role in the discord server.
- genres: Represents all the movie genres available for a movie.
- movie: Contains all the important information of a movie.
- Company: Contains all the movie companies. Planned to be used in future updates.
- movie_genres: A relationship, that allows to identify which genres a movie has.
- genre_subscription: Identifies the genres a member of the server is subscribed to.

# Bot Commands

/ping -> A ping command to test if the bot is alive. <br>
/listcommands -> Returns a list of all the available commands. <br>
/subscribe genre -> Allows a user to subscribe to a specific genre. <br>
/listsubscriptions -> Lists all subscriptions for the member. <br>
/upcoming -> Returns only the upcoming movies that have the genres that a user is subscribed to.

# Attribution

This project integrates with the TMDB (The Movie Database) API to provide up-to-date movie and TV metadata.  
Please note that this product uses the TMDB API but is **not** endorsed or certified by TMDB.
