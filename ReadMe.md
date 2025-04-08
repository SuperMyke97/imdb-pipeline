# <YourFirstName>-etl-pipeline

## Overview

This project implements an API-based ETL (Extract, Transform, Load) pipeline to fetch movie data from the IMDB API (accessed via RapidAPI), 
process and transform this data using Polars (with optional Pandas support), and finally load the cleaned data into a database such as PostgreSQL or SQLite.  The project adheres to software engineering best practices, including automated testing with pytest, code formatting with black, type hints for improved code clarity, 
and Poetry for managing project dependencies.

## Project Requirements

This project fulfills the following requirements:

1.  **Repository & Git Workflow:**

    * A GitHub repository named `<Supermyke97>-imdb-pipeline` has been created.
    * The `main` branch is the default branch.
    * Development was conducted in a feature branch (e.g., `feat/etl-pipeline`).
    * A Pull Request (PR) has been opened from the feature branch to `main`.

2.  **Project Structure:**

    ```
    <YourFirstName>-etl-pipeline/
    ├── .gitignore
    ├── README.md
    ├── pyproject.toml
    ├── poetry.lock
    ├── src/
    │   ├── __init__.py
    │   ├── web_scraper.py
    │   ├── data_transform.py
    │   ├── db_loader.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_scraper.py
    │   ├── test_transform.py
    │   ├── test_db_loader.py
    ├── data/
    │   ├── raw_data.json (or .csv)
    │   └── processed_data.parquet
    └── scripts/
        └── run_pipeline.py
    ```

    The following key files have been implemented:

    * **`src/web_scraper.py`:** Contains the logic to fetch data from the IMDB API using RapidAPI. This includes handling API requests, authentication , and initial parsing of the JSON response.
    * **`src/data_transform.py`:** Implements data cleaning and transformation logic using the Polars library. Pandas was also used for certain transformations if deemed beneficial. This file handles tasks such as data type conversion, filtering, renaming columns, and creating new features.
    * **`src/db_loader.py`:** Manages the connection to the chosen database (PostgreSQL) and implements the functionality to load the cleaned and transformed data into the database tables. This includes table creation and data insertion.
    * **`scripts/run_pipeline.py`:** Orchestrates the entire ETL process. This script calls the functions from `web_scraper.py`, `data_transform.py`, and `db_loader.py` in the correct sequence to execute the pipeline.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/](https://github.com/)<Supermyke97>/<Supermyke97>-etl-pipeline.git
    cd <Supermyke97>-etl-pipeline
    ```

2.  **Install dependencies using Poetry:**

    Ensure you have Poetry installed. If not, you can install it by following the instructions on the [official Poetry website](https://python-poetry.org/docs/).

    ```bash
    poetry install
    ```

3.  **Set up RapidAPI Key:**

    You will need a RapidAPI key to access the IMDB API. Sign up for a RapidAPI account and subscribe to an appropriate IMDB API. Store your API key securely (e.g., as an environment variable or within a configuration file that is *not* committed to the repository).

4.  **Configure Database Connection:**

    Update the database connection details (e.g., host, port, username, password, database name for PostgreSQL, or the file path for SQLite) within the `src/db_loader.py` file or using environment variables.

## Running the Pipeline

To execute the ETL pipeline, run the `run_pipeline.py` script:

```bash
poetry run python scripts/run_pipeline.py
This script will:Fetch data from the IMDB API.Transform the fetched data using Polars (and optionally Pandas).Load the transformed data into the configured database.Automated TestingThe project includes automated tests written using the pytest framework. To run the tests:poetry run pytest tests/
This command will discover and execute all test files within the tests/ directory, ensuring the reliability of the individual components of the pipeline.Code FormattingThe project adheres to the black code style. To automatically format the code:poetry run black src/ tests/ scripts/
Type HintingType hints have been used throughout the Python code to improve code readability and help with static analysis.Data Exploration (Optional)The notebooks/exploration.ipynb file (if present) can be used for initial data exploration and experimentation with the IMDB API response and potential transformations using Jupyter Notebook.Data Storagedata/raw_data.json (or .csv): May temporarily store the raw data fetched from the API (this file is not intended for committed to the repository for large datasets).data/processed_data.parquet: Stores the processed
