import pytest
from src import data_transform, web_scraper
from polars import DataFrame


top_250, top_250_details = web_scraper.extract_datafiles(
    path_1="../data/top_250.json", path_2="../data/top_250_details.json"
)


def test_tranform():
    assert (
        type(data_transform.transform(top_250=top_250, top_250_details=top_250_details))
        == tuple
    )
    for df in data_transform.transform(
        top_250=top_250, top_250_details=top_250_details
    ):
        assert type(df) == DataFrame
