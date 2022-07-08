import streamlit
# import pandas as pd
streamlit.title('Business is business')

streamlit.header('Organs left to smuggle')
streamlit.text('Kidney dialysis')
streamlit.text('Blockaged heart')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

# import requests
fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
fruityvice_normalized = pd.json_normalize(fruityvice_repsonse.json())
streamlit.dataframe(fruityvice_normalized)
# dont run anything above
streamlit.stop()

import pandas
import requests
import snowflake.connector
from urllib.error import URLError
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
# streamlit.test("What fruit would you like to add:")
add_my_fruit = streamlit.text_input('What fruit would you like to add?','jackfruit')
streamlit.write("Thanks for adding :" + add_my_fruit)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
