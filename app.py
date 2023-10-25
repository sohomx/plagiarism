import streamlit as st

st.title("GPT Shield")

text_area = st.text_area("Enter your text")

if text_area is not None:
    if st.button("Analyze"):


        col1, col2, col3 = st.columns([1, 1, 1])

        with col1:
            st.info("Your input text")
            st.success(text_area)

        with col2:
            st.info("calculated score")

        with col3:
            st.info("Basic Insights")