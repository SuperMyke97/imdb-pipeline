from src import db_loader, web_scraper, db_setup

top_250, top_250_details = web_scraper.extract_datafiles(
    path_1="../data/top_250.json", path_2="../data/top_250_details.json"
)


def test_load():
    Session = db_setup.init_session(path="..\.env.example")
    session = Session()
    assert (
        db_loader.load(path="..\data", session=session)
        == "Data loaded into database successful"
    )
