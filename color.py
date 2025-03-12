import streamlit as st
import random
from PIL import Image, ImageDraw
import io

def generate_holi_splash(keyword):
    # Create a blank canvas
    img_size = (500, 500)
    image = Image.new("RGB", img_size, "white")
    draw = ImageDraw.Draw(image)

    # Generate random color splashes
    for _ in range(100):
        x, y = random.randint(0, img_size[0]), random.randint(0, img_size[1])
        size = random.randint(20, 100)
        color = random.choice(["red", "blue", "green", "yellow", "purple", "orange", "pink"])
        draw.ellipse((x, y, x + size, y + size), fill=color, outline=None)

    # Add text to image
    draw.text((200, 450), keyword, fill="black")

    return image

# Streamlit UI
st.title("🎨 Holi Color Splash AI 🌈")
st.write("Enter a word and get a beautiful Holi-themed splash image!")

# User input
user_input = st.text_input("Enter a word (e.g., Joy, Magic, Happy):", "Happy")

if st.button("✨ Generate Holi Splash! ✨"):
    splash_image = generate_holi_splash(user_input)
    img_bytes = io.BytesIO()
    splash_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    st.image(splash_image, caption="Your Holi Splash!", use_column_width=True)
    st.download_button(label="Download Image", data=img_bytes, file_name="holi_splash.png", mime="image/png")
