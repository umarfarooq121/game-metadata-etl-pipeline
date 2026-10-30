# Game Metadata ETL Pipeline

A Python data engineering project that parses, normalises, validates, enriches, and loads game metadata from multiple sources into PostgreSQL, with interactive reporting in Power BI.

## Data Sources

- Steam — synthetic JSON feed
- Xbox — synthetic XML feed
- PlayStation — synthetic Excel feed
- RAWG API — game image enrichment

The three standard feeds contain 12 listings each, for a total of 36. Deliberately incorrect feeds are also used to test validation and error handling.

## Pipeline Flow

Source feeds → Parsing → Normalisation → Validation and duplicate detection → Image enrichment → JSON outputs and quality reports → PostgreSQL → Power BI

Rejected records are saved separately with their validation errors.

## Current Features

- Multi-format feed parsing
- Canonical game model and platform-specific normalisation
- Data validation and accepted/rejected record classification
- Duplicate detection within incoming records using platform and source ID
- Source-level error reporting
- JSON validation logs and data-quality summaries
- RAWG image lookup and image downloading
- Existing local image detection to skip repeat downloads
- Image metadata manifest stores resolved URLs and local paths
- Restoration of saved image URLs when reusing downloaded images
- PostgreSQL connection using Psycopg 3
- Loading all validated games using parameterised SQL queries
- Skipping existing database listings using platform and source ID
- Per-game transactions with automatic commit and rollback
- Database error reporting with game identifiers
- Continued processing of remaining games after a database error
- Power BI report connected to PostgreSQL using Import mode
- Overview page with total listings, platform counts, average ratings, and genre counts
- Platform slicers for interactive filtering
- Game Details page for inspecting individual listings

## Getting Started

### Prerequisites

- Python 3.14 — the version used during development
- PostgreSQL and pgAdmin
- Git
- A RAWG API key for image enrichment
- Power BI Desktop to view and edit the report

### Download the Project

```powershell
git clone https://github.com/umarfarooq121/game-metadata-etl-pipeline.git
cd game-metadata-etl-pipeline
```

### Install Python Dependencies

Run from the project root:

```powershell
py -m pip install -r requirements.txt
```

This installs the libraries needed for Excel parsing, API requests, image processing, environment settings, and PostgreSQL connectivity.

Database and environment configuration are also required before running the pipeline.

### Create the Database and Table

1. Open pgAdmin and connect to your PostgreSQL server.
2. Right-click **Databases → Create → Database**.
3. Name the database `game_metadata` and save.
4. Open the Query Tool for `game_metadata`.
5. Open `database/schema.sql` in the Query Tool and execute it.

The script creates `public.games`, including its primary key, unique listing constraint, and price and rating checks.

### Configure Environment Variables

From the project root, copy the example settings file:

```powershell
Copy-Item .env.example .env
```

If you already have a configured `.env`, keep that file instead.

Open `.env` and enter your RAWG API key and PostgreSQL credentials. Update the host, port, and username if your PostgreSQL installation uses different settings.

Never commit the real `.env` file.

### Test the Database Connection

Ensure PostgreSQL is running, then execute from the project root:

```powershell
py test_db_connection.py
```

The output should show the `game_metadata` database name and the current game count.

### Run the Pipeline

```powershell
py main.py
```

The pipeline reads the feeds, normalises and validates records, processes images for the first three accepted games, saves validation outputs, and loads accepted records into PostgreSQL.

Existing database listings are skipped. Review the terminal summary for inserted, skipped, and failed records.

Generated validation files are saved under `logs/output/`. Downloaded images and their metadata manifest are saved under `images/downloads/`.

### Open the Power BI Report

Open `reports/game_metadata_dashboard.pbix` in Power BI Desktop.

If necessary, update the PostgreSQL connection through **File → Options and settings → Data source settings** to match your local server and database, and provide your own credentials.

Select **Home → Refresh** to retrieve your database records.

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

## Image Metadata

The image manifest is stored at:

`images/downloads/image_manifest.json`

Each entry uses a platform and source ID key to store the resolved image URL and local file path.

On subsequent runs, the pipeline reuses existing images and restores saved URLs when a manifest entry is available.

## Power BI Report

Report file:

`reports/game_metadata_dashboard.pbix`

### Overview

- Total game listings
- Listings by platform
- Average rating by platform
- Listings by genre
- Platform slicer

### Game Details

- Title
- Platform
- Genre
- Price and currency
- User rating
- Platform slicer

The report uses Import mode. Select Refresh in Power BI Desktop to retrieve database changes.

Counts represent platform listings. A title available on two platforms counts as two listings.

## Validation and Database Checks

- Python-to-PostgreSQL connection verified
- First game insertion confirmed in pgAdmin
- Validated records loaded into PostgreSQL
- Existing listings skipped during loading
- Deliberately invalid price used to test database rejection and error handling
- Power BI platform counts compared with PostgreSQL query results

## Current Limitations

- Image processing is limited to the first three validated games during development.
- Images downloaded before the manifest existed may lack saved resolved URLs.
- Database loading opens a separate connection for each game.
- Database load errors are displayed in the terminal but are not yet saved to a dedicated report.
- Existing database listings are skipped; changed metadata and newly restored image metadata are not updated in those rows.
- Power BI data must be refreshed to reflect database changes.
- Standard feed data is synthetic and does not represent market-wide trends.

## Planned Features

- Save database load errors and summaries to files
- Support updates to existing database listings
- Expand RAWG integration
- Improve recurring ingestion and error recovery

## Technologies

Python, JSON, XML, openpyxl, requests, Pillow, python-dotenv, Psycopg 3, PostgreSQL, Power BI Desktop, and Git.

## Project Status

In development. The pipeline processes synthetic feeds from three platforms, normalises and validates records, enriches selected games with artwork, and loads accepted records into PostgreSQL.

Database loading supports duplicate skipping, per-game transactions, and error reporting. Image metadata is persisted in a manifest for reuse across runs.

The standard feeds contain 36 listings. Database totals depend on accepted records loaded across runs; rejected records are reported separately. Power BI provides overview and game-level reporting.
