import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of days for forecast")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky Info."))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures =  [dict["main"]["temp"] for dict in filtered_data]
        temperature_celsius=[]
        temperatures_celsius = [i - 273.15 for i in temperatures]

        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates , y=temperatures_celsius, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky Info.":
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        images = {"Clear": "images/clear.png",
                  "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)