import pandas as pd
import polars as pl
import pyarrow


from src.model import Movies, Casts, Writers, Directors, Production_companies


def load(path: str, session) -> str:
    df_movies = pd.read_parquet(f"{path}/movies.parquet")
    df_directors = pd.read_parquet(f"{path}/directors.parquet")
    df_casts = pd.read_parquet(f"{path}/casts.parquet")
    df_writers = pd.read_parquet(f"{path}/writers.parquet")
    df_prod_companies = pd.read_parquet(f"{path}/production_companies.parquet")

    def load_movies(sess=session):
        for _, row in df_movies.iterrows():
            movie = session.query(Movies).filter(Movies.movie_id == row["id"]).first()
            if not movie:
                movie = Movies(
                    movie_id=row["id"],
                    primary_title=row["primaryTitle"],
                    content_rating=row["contentRating"],
                    start_year=row["startYear"],
                    release_date=row["releaseDate"],
                    interests=row["interests"],
                    countries_of_origin=row["countriesOfOrigin"],
                    spoken_languages=row["spokenLanguages"],
                    filming_locations=row["filmingLocations"],
                    budget=row["budget"],
                    gross_worldwide=row["grossWorldwide"],
                    genres=row["genres"],
                    runtime_minutes=row["runtimeMinutes"],
                    average_rating=row["averageRating"],
                    numVotes=row["numVotes"],
                    metascore=row["metascore"],
                )
                sess.merge(movie)
        sess.commit()

    def load_casts(sess=session):
        for _, row in df_casts.iterrows():
            cast = Casts(
                cast_id=row["id"],
                full_name=row["fullName"],
                job=row["job"],
                characters=row["characters"],
                movie_id=row["movie_id"],
            )
            sess.merge(cast)
        sess.commit()

    def load_writers(sess=session):
        for _, row in df_writers.iterrows():
            writer = Writers(
                writer_id=row["id"], full_name=row["fullName"], movie_id=row["movie_id"]
            )
            sess.merge(writer)
        sess.commit()

    def load_directors(sess=session):
        for _, row in df_directors.iterrows():
            director = Directors(
                director_id=row["id"],
                full_name=row["fullName"],
                movie_id=row["movie_id"],
            )
            sess.merge(director)
        sess.commit()

    def load_prod_comp(sess=session):
        for _, row in df_prod_companies.iterrows():
            prod_company = Production_companies(
                prod_comp_id=row["id"], name=row["name"], movie_id=row["movie_id"]
            )
            sess.merge(prod_company)
        sess.commit()

    load_movies(session)
    print("Movie data loaded successfully")
    load_directors(session)
    print("Director data loaded successfully")
    load_writers(session)
    print("Writer data loaded successfully")
    load_casts(session)
    print("Cast data loaded successfully")
    load_prod_comp(session)
    print("Production company data loaded successfully")

    return "Data loaded into database successful"
