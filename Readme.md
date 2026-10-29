
# Game Metadata ETL Pipeline

A Python data engineering project that parses, normalises, validates, and enriches game metadata from multiple sources, with PostgreSQL loading under development.

## Data Sources

- Steam — synthetic JSON feed
- Xbox — synthetic XML feed
- PlayStation — synthetic Excel feed
- RAWG API — game image enrichment

## Current Features

- Multi-format feed parsing
- Canonical game model and platform-specific normalisation
- Data validation and accepted/rejected record classification
- Duplicate detection within incoming records using platform and source ID
- Source-level error reporting
- JSON validation logs and data-quality summaries
- RAWG image lookup and image downloading
- Existing local image detection to skip repeat downloads
- PostgreSQL connection using Psycopg 3
- Single validated game insertion using a parameterised SQL query
- Database connection and first inserted record verified locally

## PostgreSQL Integration

The `game_metadata` database contains a `public.games` table for normalised game metadata and image references.

Database components:

- `database/db_connection.py` — reusable connection function
- `database/game_loader.py` — inserts one validated game
- `test_db_connection.py` — checks database access and game count

Connection settings are loaded from `.env`. Credentials are excluded from version control.

## Current Limitations

- Database loading currently inserts only the first validated game.
- Repeating that insertion will trigger the database's unique constraint.
- Image processing is currently limited to the first three validated games during development.
- Existing image files are reused, but their resolved image URLs are not automatically recovered.

## Planned Features

- Load all validated games into PostgreSQL
- Skip existing database listings during repeat runs
- Improve database failure reporting and transaction handling
- Persist image metadata across runs
- Connect PostgreSQL to Power BI
- Expand RAWG integration and recurring ingestion

## Technologies

Python, JSON, XML, openpyxl, requests, Pillow, python-dotenv, Psycopg 3, PostgreSQL, and Git.

Power BI integration is planned.

## Project Status

In development. Multi-source parsing, normalisation, validation, image enrichment, and initial PostgreSQL integration have been implemented. The first validated game has been inserted and confirmed in pgAdmin.
