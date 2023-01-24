import requests
import selectorlib
from datetime import datetime


def scrape():
    url = "https://programmer100.pythonanywhere.com/"
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)["temperature"]
    return value


def store(extracted):
    with open ("temperature_data.txt", "a") as file:
        now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
        file.write(f"{now},{extracted}" + "\n")


def read():
    with open("temperature_data.txt", "r") as file:
        content = file.readlines()
        content = [cont.strip("\n") for cont in content]
        dates = []
        temperatures = []
        for cont in content[1:]:
            date = cont.split(",")[0]
            temperature = cont.split(",")[1]
            dates.append(date)
            temperatures.append(temperature)
    return {"dates": dates, "temperatures": temperatures}


if __name__ == "__main__":
    source = scrape(URL)
    extracted = extract(source)
    store(extracted)
    print(read())
