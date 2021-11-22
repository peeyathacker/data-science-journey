import streamlit as st
import requests

st.title("INVOICE EXPENSE EXTRACTOR (image format)")
st.subheader("Data Science: Week(1) Project")

name = st.text_input("Enter name of image invoice file:")
base = 'http://127.0.0.1:8000/extractor/'
url = base + name
print(url)
if url!=base:
    response = requests.get(url)
    total_amount = response.json()
    if response.status_code == 200:
        if st.button("Extract Expense"):
            st.success('The total expense: ' +str(total_amount))
    elif response.status_code == 404:
        message = total_amount['detail']
        st.error(message)
