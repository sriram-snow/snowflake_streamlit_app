import streamlit
import pandas as pd
streamlit.title('Business is business')

streamlit.header('Organs left to smuggle')
streamlit.text('Kidney dialysis')
streamlit.text('Blockaged heart')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
