# Books to Scrape: Web Scraping + SQL Analysis

A small learning project that scrapes 100 books (pages 1 to 5) from 
[Books to Scrape](https://books.toscrape.com), saves them to a CSV file, loads them into SQL Server,
and answers a few questions with SQL.

> Books to Scrape is a demo site made for practising web scraping.
> Its prices and ratings are randomly assigned, so the results have no real-world meaning.

## Project structure

```
Python_Learning/
├── scrape_books.py   # scraper script
├── books.csv         # output: 100 rows
└── README.md
```

## Data collected

| Column     | Type    | Description                                   |
|------------|---------|-----------------------------------------------|
| `title`    | text    | Full book title                               |
| `price`    | float   | Price in GBP, without the £ sign (e.g. 51.77) |
| `rating`   | integer | Star rating from 1 to 5                       |
| `in_stock` | boolean | `True` if the book is in stock                |                 |


## License / usage

For learning purposes only. Please scrape responsibly.
