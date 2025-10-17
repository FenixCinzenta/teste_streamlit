import streamlit as st

st.title("Hello, Streamlit!")
st.write("Welcome to your first Streamlit app.")
user_input = st.text_input("Enter some text: ")

st.write(f"You entered: {user_input}")

button_info = st.button("Click me!")

print(button_info)
if button_info:
    st.write("Button clicked!")
else:
    st.write("Button not clicked yet.")

chat_principal = st.chat_input("Type a message...")

print(chat_principal)

with st.chat_message("user"):
    st.write(chat_principal)
    st.image("elon_musk.png")
