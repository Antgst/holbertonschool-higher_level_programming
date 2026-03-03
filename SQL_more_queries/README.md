# SQL More Queries

## Description
This project extends SQL fundamentals with user permissions, constraints, table relationships, and multi-table queries using joins and subqueries.

## Learning Objectives
- Manage MySQL users and privileges.
- Define constraints (`NOT NULL`, `UNIQUE`, foreign keys).
- Model relationships between tables.
- Query multiple tables with `JOIN`.
- Use subqueries to filter and structure results.

## Requirements
- OS: Ubuntu 20.04 LTS
- SQL engine: MySQL 8.0 (or compatible)
- SQL files should run from the MySQL CLI.
- Files should include clear SQL comments when needed.

## Project Files
- `0-privileges.sql`
- `1-create_user.sql`
- `2-create_read_user.sql`
- `3-force_name.sql`
- `4-never_empty.sql`
- `5-unique_id.sql`
- `6-states.sql`
- `7-cities.sql`
- `8-cities_of_california_subquery.sql`
- `9-cities_by_state_join.sql`
- `10-genre_id_by_show.sql`
- `11-genre_id_all_shows.sql`
- `12-no_genre.sql`
- `13-count_shows_by_genre.sql`
- `14-my_genres.sql`
- `15-comedy_only.sql`
- `16-shows_by_genre.sql`

## Usage
```bash
mysql -u root -p < 0-privileges.sql
```
