import pytest

from src.web_scraper import extract, extract_offline, Expired, ConnectionError


@pytest.fixture
def fix_extract():
    return extract(path_1="../data/top_250", path_2="../data/top_250_details.json")


@pytest.fixture
def fix_extract_offline():
    return extract_offline(
        path_1="../data/top_250.json", path_2="../data/top_250_details.json"
    )


def test_online(fix_extract):
    if fix_extract == True:
        assert isinstance(fix_extract,list)
    else:
        assert fix_extract == False


def test_offline(fix_extract_offline):
    assert type(fix_extract_offline) == tuple
