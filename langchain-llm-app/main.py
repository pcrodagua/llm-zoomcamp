from langchain_helper import generate_pet_name
import streamlit as st

st.title("Pets name generator")

animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Crocodile"))

if animal_type:
    pet_color = st.sidebar.text_area(label=f"What is your {animal_type}?", max_chars=15)

if pet_color:
    response = generate_pet_name(animal_type, pet_color)
    st.text(response)
    