import time
import streamlit as st
import plotly.express as px
import requests
import selectorlib
from send_email import send_email
from datetime import datetime




URL = "http://programmer100.pythonanywhere.com/"


def scrape(url):
    """Scrape the page source from URL"""
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    """extract temperature from the website"""
    extractor = selectorlib.Extractor.from_yaml_file("tempextract.yaml")
    value = extractor.extract(source)["home"]
    return value


def store(content):
    """rentre les temperatures dans un fichier txt"""
    with open("data2.txt", "a") as file:
        file.write(content + "\n")


def read(content):
    """lit les temperatures dans le nouveau fichier texte"""
    with open("data2.txt", "r") as file:
        return file.read()





if __name__ == "__main__":

    while True:
        scraped = scrape(URL)
        print(scraped)
        source = scraped
        now = datetime.now()
        new_now = now.strftime("%d-%m-%Y %H-%M")
        temperature = extract(scraped)
        content = f"{new_now}, {temperature} "

        store(content)
        print("hello")
        time.sleep(60)
        figure = px.line(x=new_now, y=temperature)
        bonjour = st.plotly_chart(figure)

