import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
page_title="Smart Language Translator",
page_icon="🌍",
layout="centered"
)

st.markdown("""

<style>
.main {
    background-color: #f5f7fa;
}

h1 {
    text-align: center;
    color: #1f4e79;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
}

.translation-box {
    padding: 15px;
    border-radius: 10px;
    background-color: #eef6ff;
}
</style>""", unsafe_allow_html=True)

st.title("🌍 Smart Language Translator")
st.write("Translate text instantly into multiple languages.")

text = st.text_area(
"Enter your text",
height=150,
placeholder="Type your text here..."
)

languages = {
"Tamil": "ta",
"Hindi": "hi",
"French": "fr",
"Spanish": "es",
"German": "de",
"Japanese": "ja",
"Korean": "ko"
}

target_language = st.selectbox(
"Choose Target Language",
list(languages.keys())
)

if st.button("🚀 Translate"):
    if text.strip():
        translated = GoogleTranslator(
            source="auto",
target=languages[target_language]
).translate(text)

    st.success("Translation Completed!")

    st.markdown(
        f"""
        <div class="translation-box">
        <h4>Translated Text:</h4>
        <p>{translated}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning("Please enter text to translate.")