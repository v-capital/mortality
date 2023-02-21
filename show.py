import streamlit as st
from calc import *

with st.form('Mortality calculation'):
    st.header('Mortality calculation')

    # Creating columns to organize the form
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio('Gender?',('Male','Female'))
    with col2:
        age = st.slider('Age',1,100,1)

    submit_button = st.form_submit_button('Calculate')

if submit_button is True:
    qx,le = calc_mort(age,gender)
    st.write('**Age:**', age, '**Gender:**', gender) 
    st.write('**qx:**', qx, '**Life expectancy:**', le)
