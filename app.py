import streamlit as st

st.title("🎨 Color Splash Simulator")
st.write("Celebrate Holi by splashing colors! 🌈")

color = st.color_picker("Pick a color:", "#ff5733")
st.write("You selected:", color)

st.button("Splash! 🎉")

st.write("Enjoy and share your Holi colors! 🥳")
