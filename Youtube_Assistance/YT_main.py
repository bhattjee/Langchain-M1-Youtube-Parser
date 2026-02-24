import streamlit as st
import YT_langchain_helper as lch
import textwrap

st.title("YouTube Assistant")

with st.sidebar:
    with st.form(key="my-form"):
        youtube_url = st.text_area(
            label="Enter the YouTube video URL:",
            max_chars=100
        )
        query = st.text_area(
            label="Ask me something about the video:",
            max_chars=100,
            key="query"
        )
        submit_button = st.form_submit_button(label='Submit')

if submit_button and youtube_url and query:
    try:
        db = lch.create_vector_db_from_youtube_url(youtube_url)
        response, docs = lch.get_response_from_query(db, query)
        st.subheader("Answer:")
        st.text(textwrap.fill(response, width=80))
    except ValueError as e:
        st.error(f"⚠️ {str(e)}")
    except Exception as e:
        st.error("An unexpected error occurred.")
        st.exception(e)