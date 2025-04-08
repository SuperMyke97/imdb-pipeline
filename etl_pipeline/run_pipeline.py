from src import web_scraper, data_transform, db_loader, db_setup
import json
import polars


engine, Session = db_setup.init_session(path=".env.example")
session = Session()
db_setup.init_db(engine=engine)


# extract
files = web_scraper.extract(
    path_1="data/top_250.json", path_2="data/top_250_details.json"
)
if files:
    top_250, top_250_details = files
else:
    top_250, top_250_details = web_scraper.extract_offline(
        path_1="data/top_250.json", path_2="data/top_250_details.json"
    )

# transform
df_movies, df_casts, df_directors, df_writers, df_prod_companies = (
    data_transform.transform(top_250=top_250, top_250_details=top_250_details)
)
data_transform.save_files(
    df_movies, df_casts, df_directors, df_writers, df_prod_companies, path="data"
)

# load
db_loader.load(path="data", session=session)
