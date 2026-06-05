import requests


class CountryLeadersAPI:
    def __init__(self):
        #We store all the api urls once in the class so we can reuse them everywhere in the object.
        self.base_url = "https://country-leaders.onrender.com"
        self.cookie_url = self.base_url + "/cookie"
        self.countries_url = self.base_url + "/countries"
        self.leaders_url = self.base_url + "/leaders"
        self.cookies = None #None at start because we don't have a cookie yet.

    def refresh_cookie(self):
        #This ask the api for a fresh cookie because the api is protected and the cookie expire fast.
        self.cookies = requests.get(self.cookie_url).cookies
        # We send a get request to /cookie, the API sends me a cookie and we stock it in self.cookies
    def get_countries(self):
        #If we don't have a cookie yet we get one first before touching the protected endpoint.
        if self.cookies is None:
            self.refresh_cookie()
            # We do that because as we said the cookie expires quickly so it fetches a new one.

        #We ask the api the list of countries using the cookie.
        response = requests.get(self.countries_url, cookies=self.cookies)

        #If the cookie expired or something failed, we retry once with a fresh cookie.
        if response.status_code != 200:
            self.refresh_cookie()
            response = requests.get(self.countries_url, cookies=self.cookies)

        #.json turns the api response into a python object, here normally a list.
        return response.json()

    def get_leaders(self, country):
        # Fetches the list of political leaders for a given country from the API..
        if self.cookies is None:
            self.refresh_cookie()
            #Same logic as above: No cookie, we retry with a fresh one

        #We call leaders: with a cookie and with a url parameter like ?country=fr.
        response = requests.get(self.leaders_url, cookies=self.cookies, params={"country": country})

        .
        if response.status_code != 200:
            #If the request fails, with retry it with a fresh cookie.
            self.refresh_cookie()
            response = requests.get(self.leaders_url, cookies=self.cookies, params={"country": country})

        #You return the list of leaders as a Python object: a list of dictionaries.
        return response.json()
