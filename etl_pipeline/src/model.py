from sqlalchemy import (
    Column,
    Integer,
    Date,
    String,
    ForeignKey,
    Table,
    DECIMAL,
    Time,
    BIGINT,
)
from sqlalchemy.orm import relationship
from src.db_setup import Base, init_db


class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)


class Movies(BaseModel):
    __tablename__ = "movies"

    movie_id = Column(String(200), unique=True, nullable=False)
    primary_title = Column(String(100))
    content_rating = Column(String(100))
    start_year = Column(Date)
    release_date = Column(Date)
    interests = Column(String(1000))
    countries_of_origin = Column(String(1000))
    spoken_languages = Column(String(1000))
    filming_locations = Column(String(1000))
    budget = Column(BIGINT)
    gross_worldwide = Column(BIGINT)
    genres = Column(String(200))
    runtime_minutes = Column(Integer)
    average_rating = Column(DECIMAL(5, 2))
    numVotes = Column(Integer)
    metascore = Column(Integer)

    casts = relationship("Casts", back_populates="movie")
    directors = relationship("Directors", back_populates="movie")
    writers = relationship("Writers", back_populates="movie")
    prod_companies = relationship("Production_companies", back_populates="movie")


class Casts(BaseModel):
    __tablename__ = "casts"

    cast_id = Column(String(100), nullable=False)
    full_name = Column(String(100))
    job = Column(String(1000))
    characters = Column(String(1000))
    movie_id = Column(String(20), ForeignKey("movies.movie_id"))

    movie = relationship("Movies", back_populates="casts")


class Writers(BaseModel):
    __tablename__ = "writers"

    writer_id = Column(String(20), nullable=False)
    full_name = Column(String(1000))
    movie_id = Column(String(20), ForeignKey("movies.movie_id"))

    movie = relationship("Movies", back_populates="writers")


class Directors(BaseModel):
    __tablename__ = "directors"

    director_id = Column(String(20), nullable=False)
    full_name = Column(String(1000))
    movie_id = Column(String(20), ForeignKey("movies.movie_id"))

    movie = relationship("Movies", back_populates="directors")


class Production_companies(BaseModel):
    __tablename__ = "production_companies"

    prod_comp_id = Column(String(20), nullable=False)
    name = Column(String(1000))
    movie_id = Column(String(20), ForeignKey("movies.movie_id"))

    movie = relationship("Movies", back_populates="prod_companies")


# init_db()
