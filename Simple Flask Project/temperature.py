from selectorlib import Extractor
import requests

class Temperature:

    # class variables, not object variables
    # headers = {
    #     'pragma': 'no-cache',
    #     'cache-control': 'no-cache',
    #     'dnt': '1',
    #     'upgrade-insecure-requests': '1',
    #     'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
    #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    #     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # }
    base_url = 'https://www.timeanddate.com/weather/'
    yaml_path = 'temperature.yaml'

    # 'country' & 'city' are instance variables
    def __init__(self, country, city):
        self.country = country.replace(' ', '_')
        self.city = city.replace(' ', '_')

    def _build_url(self):
        url = self.base_url + self.country + '/' + self.city
        return url

    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yaml_path)
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace('°C', '').strip())


# The 'if' statement avoids the current file/script from being executed when imported into another script.
# When this script is run directly, the '__name__' variable equals '__main__'
if __name__ == '__main__':
    temperature = Temperature(country='iran', city='tehran')
    print(temperature.get())
