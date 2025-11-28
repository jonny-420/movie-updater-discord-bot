from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, BIGINT, Integer, ForeignKey, String, Date, REAL, UniqueConstraint

Base = declarative_base()

class movie(Base):
    __tablename__ = "movie"
    movie_id = Column(BIGINT, primary_key=True)
    title = Column(String)
    overview = Column(String)
    release_date = Column(Date)
    popularity = Column(REAL)

class genres(Base):
    __tablename__ = "genres"
    genre_id = Column(BIGINT, primary_key=True)
    genre = Column(String)

class movieGenre(Base):
    __tablename__ = "movie_genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(BIGINT, ForeignKey('movie.movie_id'))
    genre_id = Column(BIGINT, ForeignKey("genres.genre_id"))

    __table_args__ = (
        UniqueConstraint('movie_id', 'genre_id', name='uq_movie_genre'),
    )