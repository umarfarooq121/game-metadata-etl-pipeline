
# Game Metadata ETL Pipeline

A Python data engineering project that parses, normalises, validates, enriches, and loads game metadata from multiple sources into PostgreSQL.

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
- Loading all validated games using parameterised SQL queries
- Skipping existing database listings using platform and source ID
- Per-game transactions with automatic commit and rollback
- Database error reporting with game identifiers
- Continued processing of remaining games after a database error

## PostgreSQL Integration

The `game_metadata` database contains a `public.games` table for normalised game metadata and image references.

Database components:

- `database/db_connection.py` — reusable connection function
- `database/game_loader.py` — inserts one game per call and skips existing listings
- `test_db_connection.py` — checks database access and game count
- `main.py` — loads validated games and reports inserted, skipped, and failed counts

Each game is processed in a separate transaction. Successful insertions are committed. Failed transactions are rolled back without undoing previously committed games.

A unique constraint on `(platform, source_id)` prevents duplicate listings. Check constraints reject negative prices and ratings outside 0–5.

Connection settings are loaded from `.env`. Credentials are excluded from version control.

## Validation and Database Checks

- Python-to-PostgreSQL connection verified
- First game insertion confirmed in pgAdmin
- Full validated dataset loaded, with 28 records confirmed
- Existing listing skipped during loading
- Deliberately invalid price used to test database rejection and error handling

## Current Limitations

- Image processing is limited to the first three validated games during development.
- Existing image files are reused, but their resolved image URLs are not automatically recovered.
- Database loading opens a separate connection for each game.
- Database load errors are displayed in the terminal but are not yet saved to a dedicated report.
- Existing database listings are skipped; changed metadata is not updated.

## Planned Features

- Persist image metadata across runs
- Save database load errors and summaries to files
- Connect PostgreSQL to Power BI
- Expand RAWG integration
- Improve recurring ingestion and error recovery

## Technologies

Python, JSON, XML, openpyxl, requests, Pillow, python-dotenv, Psycopg 3, PostgreSQL, and Git.

Power BI integration is planned.

## Project Status

In development. The pipeline processes synthetic feeds from three platforms, normalises and validates records, enriches selected games with artwork, and loads accepted records into PostgreSQL.

Database loading supports duplicate skipping, per-game transactions, and error reporting. The current database contains 28 game listings.
