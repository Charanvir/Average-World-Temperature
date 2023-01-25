import requests
import selectorlib
from datetime import datetime
import sqlite3

connection = sqlite3.connect("temperature_data.db")

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
    now = datetime.now().strftime("%y-%m-%d-%H-%M-%S")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperature_data VALUES(?,?)", (now, extracted))
    connection.commit()


def read():
    cursor = connection.cursor()
    dates = cursor.execute("SELECT date FROM temperature_data")
    temperatures = cursor.execute("SELECT temperature FROM temperature_data")
    dates = dates.fetchall()
    temperatures = temperatures.fetchmany()
    return [dates, temperatures]


if __name__ == "__main__":
    url = "https://programmer100.pythonanywhere.com/"
    source = scrape()
    extracted = extract(source)
    store(extracted)
    # print(read())
