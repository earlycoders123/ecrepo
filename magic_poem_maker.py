import streamlit as st
import random
import io

st.set_page_config(page_title="📝 Magic Poem Maker", page_icon="🌈")

st.title("📝 Magic Poem Maker")
st.subheader("Enter a topic, and let the 'AI' write a magical poem!")

topic = st.text_input("🌟 What should the poem be about? (e.g. stars, cake, school)")

openings = ["In the land of", "Beneath the sky of", "Oh beautiful", "Mysterious", "Magical"]
middles = ["dreams come alive", "dances with light", "hides many stories", "sings softly", "holds secrets"]
endings = ["like a shining star.", "on a windy day.", "with a glowing heart.", "under moonlight.", "forevermore."]

poem = ""

if st.button("🎨 Generate Poem"):
    if topic.strip() == "":
        st.warning("Please enter a topic first!")
    else:
        poem = (
            f"{random.choice(openings)} {topic},\n"
            f"It {random.choice(middles)},\n"
            f"And it {random.choice(endings)}"
        )
        st.success("Here's your poem!")
        st.markdown(f"### ✨ Your Poem:\n\n*{poem}*")

        poem_file = io.StringIO()
        poem_file.write("✨ Magic Poem ✨\n")
        poem_file.write("--------------------\n")
        poem_file.write(poem)
        poem_file.seek(0)

        st.download_button(
            label="📥 Download Poem as TXT",
            data=poem_file,
            file_name="magic_poem.txt",
            mime="text/plain"
        )
