import requests
import selectorlib

URL = "https://programmer100.pythonanywhere.com/"

def scrape(url):
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    with open ("temperature_data.txt", "a") as file:
        file.write(extracted + "\n")

