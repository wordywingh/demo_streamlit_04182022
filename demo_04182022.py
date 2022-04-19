import pandas as pd
import numpy as np
import streamlit as st

# write a function to count how many vowels in a string

def vowel_counter(user_string):
  vowel_list = ["a","e","i","o","u"]
  count = 0
  for x in user_string:
    if x in vowel_list:
      count += 1
  return count

#

st.title("Deployment Demo")

form = st.form(key="my_form")

with form:
  user_input = st.text_area("Please enter a string for analysis")
  submitted = st.form_submit_button(label = "Submit")

if submitted:
  st.success(vowel_counter(str(user_input)))