import langchain_helper as lch
import streamlit as st

st.title("Pet name generator")

user_animal_type = st.sidebar.selectbox("What is your pet ?",("Cat","Dog","Cow","Hen","Hamster"))

if user_animal_type == "Cat" : 
    Pet_color = st.sidebar.text_area(label = "What is the color of your cat ?" , max_chars=7)
    
if user_animal_type == "Dog" : 
    Pet_color = st.sidebar.text_area(label = "What is the color of your Dog ?" , max_chars=7)
    
if user_animal_type == "Cow" : 
    Pet_color = st.sidebar.text_area(label = "What is the color of your Cow ?" , max_chars=7)
    
if user_animal_type == "Hen" : 
    Pet_color = st.sidebar.text_area(label = "What is the color of your Hen ?" , max_chars=7)
    
if user_animal_type == "Hamster" : 
    Pet_color = st.sidebar.text_area(label = "What is the color of your Hamster ?" , max_chars=7)
    
if Pet_color:
    response = lch.generate_pet_name(user_animal_type , Pet_color)
    st.text(response)