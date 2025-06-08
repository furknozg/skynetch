# Skynetch

A command-line interface for fetching, caching, and exporting flight data using the Kiwi.com API. Skynetch helps you efficiently search for flights, cache results to avoid redundant API calls, and export data for analysis or machine learning purposes.

## Business Purpose

Skynetch is designed for:
- **Flight Data Collection**: Systematically gather flight pricing and availability data
- **Market Research**: Analyze flight prices across different routes and dates
- **ML Training Data**: Export structured flight data for machine learning models
- **Cost Optimization**: Track and compare flight prices over time
- **Travel Planning**: Bulk search flights with intelligent caching

## Features

- **Smart Caching**: Automatically caches API responses to reduce costs and improve performance
- **Flexible Search**: Search flights by country, city, date ranges, and passenger counts
- **Data Export**: Export cached flight data to CSV for analysis
- **Cache Management**: Inspect and manage cached flight data
- **Rate Limiting**: Built-in caching prevents excessive API calls

## Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/yourusername/skynetch.git
```

## Setup

1. **Configure API Key**: You'll need a RapidAPI key for the Kiwi.com Cheap Flights API.

```bash
skynetch setenv RAPIDAPI_KEY your_rapidapi_key_here
```

2. **Verify Installation**: Test the CLI is working:

```bash
skynetch --help
```

## Commands

### `skynetch setenv`
Set environment variables in the `.env` file.

```bash
skynetch setenv KEY VALUE
```

**Example:**
```bash
skynetch setenv RAPIDAPI_KEY abc123xyz789
```

**Required for**: Initial setup to configure API credentials.

### `skynetch search`
Search for one-way flights using configurable parameters.

```bash
skynetch search [OPTIONS]
```

**Key Options:**
- `--source`: Source location (e.g., `Country:GB`, `City:london_gb`)
- `--destination`: Destination (e.g., `City:dubrovnik_hr`)
- `--outbound-start`: Departure date start (ISO format)
- `--outbound-end`: Departure date end (ISO format)
- `--price-start/--price-end`: Price range filters
- `--days`: Specific days of week (e.g., `SUNDAY,MONDAY,TUESDAY`)
- `--adults/--children/--infants`: Passenger counts
- `--force-refresh`: Bypass cache and make fresh API call

**Example:**
```bash
skynetch search --source "Country:GB" --destination "City:dubrovnik_hr" \
  --outbound-start "2024-07-22T00:00:00" --outbound-end "2024-07-23T00:00:01" \
  --price-end 500 --days "FRIDAY,SATURDAY,SUNDAY"
```

**Required for**: Primary flight data collection. Results are automatically cached.

### `skynetch export`
Export cached flight data to CSV format.

```bash
skynetch export [OPTIONS]
```

**Options:**
- `--query-date`: Only export results from specific date (YYYY-MM-DD)
- `--output`: Output CSV filename (default: `export.csv`)

**Example:**
```bash
skynetch export --query-date "2024-07-22" --output "july_flights.csv"
```

**Required for**: Converting cached flight data into structured format for analysis, reporting, or ML training.

### `skynetch inspect`
Inspect cached flight data and database contents.

```bash
skynetch inspect [OPTIONS]
```

**Options:**
- `--db-path`: Path to SQLite cache file (default: `flight_cache.db`)

**Example:**
```bash
skynetch inspect --db-path "flight_cache.db"
```

**Required for**: Debugging cache issues, understanding data structure, and managing cache size.

## Workflow Example

1. **Setup**: Configure your API key
```bash
skynetch setenv RAPIDAPI_KEY your_key_here
```

2. **Search**: Collect flight data for multiple routes/dates
```bash
skynetch search --source "Country:US" --destination "City:paris_fr" \
  --outbound-start "2024-08-01T00:00:00" --outbound-end "2024-08-07T23:59:59"
```

3. **Inspect**: Check what data was cached
```bash
skynetch inspect
```

4. **Export**: Generate CSV for analysis
```bash
skynetch export --output "us_paris_flights.csv"
```

## Data Structure

Exported CSV includes:
- Flight identification (itinerary_id, share_id, flight_code)
- Pricing (price_usd, price_eur, price_before_discount)
- Route details (departure/arrival airports and times)
- Booking information (carrier, provider, booking_url)
- Special flags (hidden_city, virtual_interlining, throwaway_ticket)
- Baggage allowances (checked_bags, hand_bags)

## Cache Behavior

- Responses are cached for 24 hours by default
- Cache key includes all search parameters
- Use `--force-refresh` to bypass cache
- Cache is stored in local SQLite database (`flight_cache.db`)

## API Requirements

- RapidAPI subscription to Kiwi.com Cheap Flights API
- API key must be set via `skynetch setenv RAPIDAPI_KEY`

## Use Cases

- **Travel Agencies**: Bulk price comparison and route analysis
- **Data Scientists**: Flight price prediction model training
- **Researchers**: Aviation market analysis and trends
- **Developers**: Building travel applications with cached flight data
- **Personal Use**: Systematic flight deal hunting and tracking
