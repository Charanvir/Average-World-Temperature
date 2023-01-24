import streamlit as st
import plotly.express as px
from functions import scrape, extract, read, store

st.title("Average World Temperature")

source = scrape()
extracted = extract(source)
store(extracted)
values = read()
dates = values["dates"]
temperatures = values["temperatures"]
figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature"})
st.plotly_chart(figure)
