# Wikipedia Scraper

Small Python project where we use an API to get political leaders by country, then scrape the first paragraph of their Wikipedia page and save everything into a JSON file.

## What the project does

The API gives us:
- the list of countries
- the leaders for each country
- the Wikipedia URL of each leader

Then the scraper:
- opens each Wikipedia page
- looks for the first real paragraph
- cleans the text a little
- adds it back to the leader data

At the end, everything is saved into `leaders.json`.

## How It Works

1. Create an API client instance to communicate with the Country Leaders API.
2. Retrieve the list of available countries.
3. Retrieve all leaders for each country.
4. For every leader, access their Wikipedia page.
5. Extract the first meaningful paragraph from the page.
6. Add the extracted paragraph to the leader's data.
7. Store all results in a dictionary organized by country.
8. Export the final dataset to a JSON file.

## Architecture

The project follows a simple separation of concerns:

* `CountryLeadersAPI` handles all communication with the API.
* `WikipediaScraper` handles HTML parsing and data extraction.
* `main.py` orchestrates the workflow.
* `leaders.json` stores the final output.

This structure keeps the code modular and easier to maintain.



## Visuals (Data flow)


```text
Country Leaders API
        │
        ▼
 Get Countries
        │
        ▼
  Get Leaders
        │
        ▼
 Wikipedia URLs
        │
        ▼
 Wikipedia Scraper
        │
        ▼
 First Paragraph
        │
        ▼
   leaders.json
```



## Project structure

```text
wikipedia_scraper/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── dev/
│   ├── Imad_notebook.ipynb
│   └── Hiba_notebook.ipynb
└── src/
    ├── __init__.py
    ├── api_client.py
    └── html_scraper.py
```

## Files

- `main.py`
  Main file that connects everything together.

- `src/api_client.py`
  Handles the API side:
  - cookie
  - countries
  - leaders

- `src/html_scraper.py`
  Handles the Wikipedia side:
  - fetch HTML
  - find first paragraph
  - clean the text

- `leaders.json`
  Final output file created after running the script.

## Installation

Clone the repository and go inside it:

```bash
git clone <your-repo-url>
cd wikipedia_scraper
```

Create and activate a virtual environment:

### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Requirements

This project uses:
- `requests`
- `beautifulsoup4`

## Usage

Run the project with:

```bash
python main.py
```

If it works, it creates:

```text
leaders.json
```

inside the project folder.

## Example output

Each leader keeps the API data and gets a new key called `first_paragraph`.

Example:

```json
{
    "id": "Q157",
    "first_name": "François",
    "last_name": "Hollande",
    "birth_date": "1954-08-12",
    "death_date": null,
    "place_of_birth": "Rouen",
    "wikipedia_url": "https://fr.wikipedia.org/wiki/Fran%C3%A7ois_Hollande",
    "start_mandate": "2012-05-15",
    "end_mandate": "2017-05-14",
    "first_paragraph": "François Hollande, né le 12 août 1954 à Rouen..."
}
```
## Challenges

- Understanding how the API cookie system works.
- Finding the first meaningful paragraph on Wikipedia pages.
- Cleaning the scraped text while preserving readability.


## Authors

Made as part of a Becode project, in this both Imad and Hiba
