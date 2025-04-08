import pprint
from typing import Tuple

import polars as pl
import json
from polars import DataFrame


def transform(
    top_250=None, top_250_details=None
) -> tuple[DataFrame, DataFrame, DataFrame, DataFrame, DataFrame]:
    for i in range(len(top_250)):
        top_250[i]["interests"] = ",".join(top_250[i]["interests"])
        top_250[i]["countriesOfOrigin"] = ",".join(top_250[i]["countriesOfOrigin"])
        top_250[i]["genres"] = "".join(top_250[i]["genres"])
        if top_250[i]["spokenLanguages"] is not None:
            top_250[i]["spokenLanguages"] = ",".join(top_250[i]["spokenLanguages"])
        else:
            top_250[i]["spokenLanguages"] = None

        if top_250[i]["filmingLocations"] is not None:
            top_250[i]["filmingLocations"] = "".join(top_250[i]["filmingLocations"])
        else:
            top_250[i]["filmingLocations"] = None
        for x in top_250_details[i]["cast"]:
            x["characters"] = " ".join(x["characters"])
        if top_250[i]["primaryTitle"] == "L\u00e9on: The Professional":
            top_250[i]["primaryTitle"] = "Leon: The Professional"

    def create_df(table):
        data = []
        for movie in top_250_details:
            each_id = movie["id"]
            if movie[f"{table}"] is not None:
                for dict in movie[f"{table}"]:
                    dict["movie_id"] = each_id
                    data.append(dict)
            else:
                pass
        return pl.DataFrame(data)

    df_cast = create_df(table="cast")
    df_writer = create_df(table="writers")
    df_director = create_df(table="directors")
    df_prod_companies = create_df(table="productionCompanies")

    df_movie = pl.DataFrame(top_250)
    df_movie = df_movie.drop(
        [
            "isAdult",
            "url",
            "originalTitle",
            "type",
            "primaryImage",
            "trailer",
            "externalLinks",
            "productionCompanies",
            "endYear",
        ]
    )

    # Dealing with columns with null values and data types
    df_movie = df_movie.with_columns(
        pl.col("filmingLocations").fill_null("not available"),
        pl.col("spokenLanguages").fill_null("not available"),
        pl.col("contentRating").fill_null("not available"),
        pl.col("budget").fill_null(0),
        pl.col("grossWorldwide").fill_null(0),
        pl.col("metascore").fill_null(0),
        pl.col("startYear").cast(pl.Date),
        pl.col("releaseDate").cast(pl.Date),
    )

    return df_movie, df_cast, df_director, df_writer, df_prod_companies


def save_files(
    df_movies: DataFrame,
    df_casts: DataFrame,
    df_directors: DataFrame,
    df_writers: DataFrame,
    df_prod_companies: DataFrame,
    path: str,
):
    df_movies.write_parquet(f"{path}/movies.parquet")
    df_directors.drop("url").write_parquet(f"{path}/directors.parquet")
    df_casts.drop("url").write_parquet(f"{path}/casts.parquet")
    df_writers.drop("url").write_parquet(f"{path}/writers.parquet")
    df_prod_companies.write_parquet(f"{path}/production_companies.parquet")

    return "Data saved successfully"
