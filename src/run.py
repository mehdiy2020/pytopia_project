import streamlit as st
from io import StringIO
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

login_option = st.sidebar.radio('Login/Signup', ('Login', 'Signup'))

if login_option == 'Login':
  with st.sidebar.form("Login"):
      st.write("Login Here.")
      username = st.text_input("Username")
      password = st.text_input("Passwprd", type="password")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
          pass
else:
  with st.sidebar.form("Signup"):
      st.write("Signup Here.")
      username = st.text_input("Username")
      password = st.text_input("Passwprd", type="password")
      email = st.text_input("Email")

      # Every form must have a submit button.
      submitted = st.form_submit_button("Submit")
      if submitted:
          pass


st.image("data/python.jpg", caption="Git Project Practice")

st.title(':trophy: Python Git GitHub')

col1, col2, col3 = st.columns(3)
col1.metric(label="Pytopia Telegram member", value="4000", delta="+100")
col2.metric(label="Pytopia Website", value="3000", delta="-50")
col3.metric(label="Class Registered", value="4500", delta="+80")

with st.expander("Statistics"):
  uploaded_file = st.file_uploader("Select Your Desired File")
  if uploaded_file is not None:
      # To convert to a string based IO:
      stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
      string_data = stringio.read()
      st.write(string_data)
    
      data = json.loads(string_data)
      st.json(data, expanded=False)


with st.expander("Plot"):
  fig, ax = plt.subplots(1,1,figsize=(10, 5))
  sns.histplot(np.random.randn(100), ax = ax)
  st.pyplot(fig)  

with st.expander("Your Picture"):
  col1, col2 = st.columns(2, border=True)
  col1.text_input("Name: ")
  col2.text_input("Location: ")
  st.camera_input("Take a picture", key='camera_input')