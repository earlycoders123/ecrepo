
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time

# Function to generate animated color splashes
def color_splash():
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_frame_on(False)

    for _ in range(80):  # Number of splashes
        x, y = np.random.uniform(0, 10, 2)
        color = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink"])
        size = random.uniform(300, 900)

        ax.scatter(x, y, s=size, color=color, alpha=0.7)

    return fig

# Streamlit UI
st.title("🌈 Holi Color Splash Simulator 🎉")
st.write("Click the button to throw colors and celebrate Holi!")

if st.button("✨ Splash Colors!"):
    with st.spinner("Throwing Colors... 🎆"):
        time.sleep(2)
        st.pyplot(color_splash())
        st.success("Happy Holi! 🎊 Enjoy the colors!")
