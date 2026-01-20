import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translation Tool")

st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages easily.")

text = st.text_area("Enter text to translate:")

languages = {
    "English": "en",
    "Bangla": "bn",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Hindi": "hi",
    "Arabic": "ar"
}

source_lang = st.selectbox("Select Source Language", list(languages.keys()))
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text.")
    else:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)
        
        st.success("Translated Text:")
        st.write(translated)


