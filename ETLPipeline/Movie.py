# Left for reference only
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, BIGINT, Date, REAL

Base = declarative_base()

class movie(Base):
    __tablename__ = "movie"
    movie_id = Column(BIGINT, primary_key=True)
    title = Column(String)
    overview = Column(String)
    release_date = Column(Date)
    popularity = Column(REAL)
