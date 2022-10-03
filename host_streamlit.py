import streamlit as st
from transliteration import transliteration_model


st.header("Transliteration")
choice1 = st.selectbox("Select the transliteration direction:", ["English Script -> Tamil Script", "Tamil Script -> English Script"])
choice2 = st.selectbox("Select what you want to transliterate:", ["Word", "Sentence"])
transliteration_text = st.text_area("Enter text to transliterate:")
if st.button("Process"):
    if choice1 == "English Script -> Tamil Script":
        if choice2 == "Word":
            result = transliteration_model.transliterate_word(str(transliteration_text), t2e=False)
        else:
            result = transliteration_model.transliterate_sentence(str(transliteration_text), t2e=False)
    else:
        if choice2 == "Word":
            result = transliteration_model.transliterate_word(str(transliteration_text), t2e=True)
        else:
            result = transliteration_model.transliterate_sentence(str(transliteration_text), t2e=True)
    st.subheader("Transliterated Text:")
    st.write(result)
  
