# BMI Calculator

import streamlit as st

st.title("BMI Calculator")
st.write("Enter your height and weight to calculate your BMI.")


height = st.number_input(
    "Height (in meters)", min_value=0.5, max_value=3.0, value=1.75)

weight = st.number_input(
    "Weight (in kg)", min_value=10, max_value=500, value=70)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is {bmi:.2f}")

        if bmi < 18.5:
            st.warning("You are underweight.")
        elif bmi >= 18.5 and bmi <= 24.9:
            st.success("You are normal weight.")
        elif bmi >= 25 and bmi <= 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid height and weight.")
