import streamlit as st
import string
import random

st.set_page_config(page_title="Password Generator", page_icon="🔒"  )
st.title("🔒Password Generator")

# *************length of password*************


length = st.slider("Length of password", min_value=8, max_value=24, value=12)



# *************check the password strength*************


def input_password(password):

    if not password: # Handle empty input case
        return "Weak: Please enter a password."    

    characters_of_length =  len(password)
    use_digits = any(c.isdigit() for c in password)
    use_special_characters = any(c in string.punctuation for c in password) 


    if characters_of_length < 8 and not use_digits and not use_special_characters:
        return f"Weak: Your password is weak please enter a password with more than {length} characters and atleast one digit and one special character and one uppercase letter"


    if characters_of_length >= length and use_digits and not use_special_characters:
        return "Moderate: Your password is moderate please enter a password with atleast one special character"


    if characters_of_length >= length and use_digits and use_special_characters:
        return "Strong: Your password is strong" 
        

username = st.text_input("Enter your username")
password = st.text_input("Enter your password", type="password")

if st.button("Submit password"):
    strength = input_password(password)

    
    if strength: 
        if "Weak:" in strength:
            st.error(strength)
        
        elif "Moderate:" in strength:
            st.warning(strength)

        elif "Strong:" in strength:
            st.success(strength)



# *************Generate password*************


# ascii_letters: ascii_letters can provide lowercase and uppercase letters


def generate_password(length, use_digits, use_special_characters):

    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    
    if use_special_characters:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


use_digits = any(string.digits)
use_special_characters = any(string.punctuation)

if st.button("Generate password"):
    password = generate_password(length, use_digits, use_special_characters)
    
    st.write(f"Generated password: {password}")

