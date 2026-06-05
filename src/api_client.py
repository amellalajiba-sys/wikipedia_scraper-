import requests


class CountryLeadersAPI:
    def __init__(self):
        #We store all the api urls once in the class so we can reuse them everywhere in the object.
        self.base_url = "https://country-leaders.onrender.com"
        self.cookie_url = self.base_url + "/cookie"
        self.countries_url = self.base_url + "/countries"
        self.leaders_url = self.base_url + "/leaders"
        self.cookies = None#None at start because we don't have a cookie yet.

    def refresh_cookie(self):
        #This ask the api for a fresh cookie because the api is protected and the cookie expire fast.
        self.cookies = requests.get(self.cookie_url).cookies

    def get_countries(self):
        #If we don't have a cookie yet we get one first before touching the protected endpoint.
        if self.cookies is None:
            self.refresh_cookie()

        #We ask the api the list of countries like fr be us etc.
        response = requests.get(self.countries_url, cookies=self.cookies)

        #If the cookie expired or something failed, we retry once with a fresh cookie.
        if response.status_code != 200:
            self.refresh_cookie()
            response = requests.get(self.countries_url, cookies=self.cookies)

        #.json turns the api response into a python object, here normally a list.
        return response.json()

    def get_leaders(self, country):
        #Same logic as get_countries but this time for one country at a time.
        if self.cookies is None:
            self.refresh_cookie()

        #params add ?country=fr or ?country=be etc at the end of the url.
        response = requests.get(self.leaders_url, cookies=self.cookies, params={"country": country})

        #If the cookie expired while looping we refresh and retry once.
        if response.status_code != 200:
            self.refresh_cookie()
            response = requests.get(self.leaders_url, cookies=self.cookies, params={"country": country})

        #This should give back the list of leaders for that country.
        return response.json()
