# Left for reference only
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, BIGINT, Integer, ForeignKey 

Base = declarative_base()

class movieGenre(Base):
    __tablename__ = "movie_genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    movie_id = Column(BIGINT, ForeignKey('movie.id'))
    genre_id = Column(BIGINT, ForeignKey("genres.genre_id"))
