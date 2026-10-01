import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of days for forecast")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky Info."))

try:
    if place:
        filtered_data = get_data(place, days)

        if option == "Temperature":
            temperatures =  [dict["main"]["temp"] / 10 for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates , y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
            st.subheader(f"{option} for the next {days} days in {place}")
            st.plotly_chart(figure)

        if option == "Sky Info.":
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            images = {"Clear": "images/clear.png",
                      "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png",
                      "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in sky_conditions]
            st.image(image_paths, width=115)

except KeyError:
    st.write(f"No data available for {place}! Please check your spelling.")