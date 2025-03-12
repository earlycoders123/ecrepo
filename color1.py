import streamlit as st
import random
from PIL import Image, ImageDraw, ImageFont
import io

def generate_holi_splash():
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
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 30)
    except IOError:
        font = ImageFont.load_default()

    text = "Early Coders wishes you a colorful Holi!"
    text_width, text_height = draw.textsize(text, font)
    text_position = ((img_size[0] - text_width) // 2, img_size[1] - 50)
    draw.text(text_position, text, fill="black", font=font)

    return image

# Streamlit UI
st.title("🎨 Play Holi with Early Coders! 🌈")

# Button for playing Holi
if st.button("✨ Play Holi! ✨"):
    splash_image = generate_holi_splash()
    img_bytes = io.BytesIO()
    splash_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    st.image(splash_image, caption="Your Holi Splash!", use_column_width=True)
    st.download_button(label="Download Image", data=img_bytes, file_name="holi_splash.png", mime="image/png")

    # Add instrumental music (Holi festival)
    st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")
