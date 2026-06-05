import json
#We import the json module to save python data into a .json file.
from pathlib import Path
#We import Path, which is used to handle file paths in a clean way
from src.api_client import CountryLeadersAPI
from src.html_scraper import WikipediaScraper
#We import the 2 principal classes


def save_to_json(data, filepath="leaders.json"):
    #Here, we define a function who will save the data in a .json file.
    output_path = Path(__file__).resolve().parent / filepath
    #We save next to main.py so the file always goes in the project folder no matter where the terminal is.
    with open(output_path, "w", encoding="utf-8") as file:
        #We open the file in write mode (w) with UTF-8 encoding to handle accents 
        # and special characters.
        json.dump(data, file, ensure_ascii=False, indent=4)
        #We write the data into the .json file: 
        # ensure_ascii will keep the special caracters and 
        # indent=4 helps make the file more readable for us, humans.


def main():
    api = CountryLeadersAPI()
    scraper = WikipediaScraper()
    #We create one object for the api side and one object for the wikipedia/html side.

    leaders_per_country = {}
    #Final dictionary where we will store everything country by country 
    # but for now, it's empty.


    countries = api.get_countries()
    #First we ask the api the list of countries.
    for country in countries:
        #We go through each country stored in countries.
        leaders = api.get_leaders(country)
        #For each one of them we ask the api the list of leaders.

        #Then for each leader we scrape their wikipedia first paragraph 
        # and add it to the leader dict.
        for leader in leaders:
            wikipedia_url = leader.get("wikipedia_url")
            if wikipedia_url:
                leader["first_paragraph"] = scraper.scrape_first_paragraph(wikipedia_url)
            else:
                leader["first_paragraph"] = ""
                #If there is no wikipedia url we still keep the key but empty. 
                # It helps keeping a clean and uniform structure.

        leaders_per_country[country] = leaders
        #Once one country is done we store its leaders in the big final dictionary.  

    save_to_json(leaders_per_country)
    #At the end we save the whole final result into leaders.json.
    print("The leaders have been saved to leaders.json")
    #If this message is printed then it is the proof that everything went well 


if __name__ == "__main__":
    #This makes the script run only if we launch main.py directly, not when it is imported as a module.
    main()
