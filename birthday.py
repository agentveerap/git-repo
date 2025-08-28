import streamlit as st
import random

# Page config
st.set_page_config(
    page_title="Happy Birthday 🎉",
    layout="wide"
)

# Custom CSS for background animation
page_bg = """
<style>
body {
    background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1, #fbc2eb);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    font-family: "Comic Sans MS", cursive, sans-serif;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

h1 {
    color: white;
    text-align: center;
    font-size: 70px !important;
    text-shadow: 3px 3px 6px #00000090;
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.1); }
    100% { transform: scale(1); }
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Heading
st.markdown("<h1>🎂 Happy Birthday Piyush Sir 🎉</h1>", unsafe_allow_html=True)

# Balloons + Snow
st.balloons()
st.snow()

# Background Music (Birthday tune)
music_html = """
<audio autoplay loop>
  <source src="https://www2.cs.uic.edu/~i101/SoundFiles/StarWars60.wav" type="audio/wav">
  Your browser does not support the audio element.
</audio>
"""
st.markdown(music_html, unsafe_allow_html=True)

# Surprise 1: Quotes
if st.button("💝 Click for a Birthday Quote!"):
    quotes = [
        "🎉 May your day be filled with laughter, joy, and cake!",
        "🌟 A year older, a year wiser, and even more awesome!",
        "🎂 Birthdays are nature’s way of telling us to eat more cake.",
        "🥳 May all your dreams and wishes come true this year!"
    ]
    st.success(random.choice(quotes))
    st.balloons()

# Surprise 2: Random Gift Reveal
if st.button("🎁 Open Your Gift!"):
    gifts = [
        "🚗 A shiny new car! (well… virtually 😉)",
        "🏝 A vacation to Maldives (in imagination!)",
        "📚 A library full of wisdom!",
        "💻 A supercomputer for coding fun!"
    ]
    st.info("You got: " + random.choice(gifts))

# Surprise 3: Cake ASCII Art
if st.button("🍰 Show me the Cake!"):
    cake = """
        🎂🎂🎂🎂🎂
       🎂🎂🎂🎂🎂🎂
      🎂🎂🎂🎂🎂🎂🎂
     🎂🎂 HAPPY 🎂🎂
    🎂🎂 BIRTHDAY 🎂🎂
   🎂🎂 PIYUSH SIR 🎂🎂
      🎂🎂🎂🎂🎂🎂🎂
       🎂🎂🎂🎂🎂🎂
        🎂🎂🎂🎂🎂
    """
    st.code(cake, language="")

# Surprise 4: Confetti Effect
if st.button("🎊 Confetti Blast!"):
    st.success("Boom 💥🎊✨🎉💫 Enjoy the confetti vibes!")
    st.snow()
    st.balloons()
