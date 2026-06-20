
import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌍")

st.title("🌍 Language Translator")
st.write("Translate text into different languages instantly.")

text = st.text_area("Enter text to translate")

target_language = st.selectbox(
    "Select Language",
    ["Tamil", "Hindi", "French", "Spanish", "German"]
)

lang_codes = {
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

if st.button("Translate"):
    if text:
        translated = GoogleTranslator(
            source="auto",
            target=lang_codes[target_language]
        ).translate(text)

        st.success("Translation Complete!")
        st.write(translated)
    else:
        st.warning("Please enter some text.")