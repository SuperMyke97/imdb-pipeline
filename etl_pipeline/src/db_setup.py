from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os


def init_session(path):
    load_dotenv(dotenv_path=path)
    DB_URL = os.getenv("DB_URL")
    engine = create_engine(DB_URL)
    Session_db = sessionmaker(autoflush=False, autocommit=False, bind=engine)

    return engine, Session_db


Base = declarative_base()


def init_db(engine):
    try:
        Base.metadata.create_all(engine)
    except Exception as e:
        print(f"{e}")
