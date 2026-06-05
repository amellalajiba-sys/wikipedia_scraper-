import json
from pathlib import Path
from src.api_client import CountryLeadersAPI
from src.html_scraper import WikipediaScraper


def save_to_json(data, filepath="leaders.json"):
    #We save next to main.py so the file always goes in the project folder no matter where the terminal is.
    output_path = Path(__file__).resolve().parent / filepath
    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    #We create one object for the api side and one object for the wikipedia/html side.
    api = CountryLeadersAPI()
    scraper = WikipediaScraper()

    leaders_per_country = {}#Final dictionary where we will store everything country by country.

    #First we ask the api the list of countries.
    countries = api.get_countries()
    for country in countries:
        #For each country we ask the api the list of leaders.
        leaders = api.get_leaders(country)

        #Then for each leader we scrape their wikipedia first paragraph and add it to the leader dict.
        for leader in leaders:
            wikipedia_url = leader.get("wikipedia_url")
            if wikipedia_url:
                leader["first_paragraph"] = scraper.scrape_first_paragraph(wikipedia_url)
            else:
                leader["first_paragraph"] = ""#If there is no wikipedia url we still keep the key but empty.

        #Once one country is done we store its leaders in the big final dictionary.
        leaders_per_country[country] = leaders

    #At the end we save the whole final result into leaders.json.
    save_to_json(leaders_per_country)
    print("The leaders have been saved to leaders.json")


if __name__ == "__main__":
    #This makes the script run only if we launch main.py directly.
    main()
