import streamlit

import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('Business is business')

streamlit.header('Organs left to smuggle')
streamlit.text('Kidney dialysis')
streamlit.text('Blockaged heart')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_repsonse = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_repsonse.json())
    return fruityvice_normalized
streamlit.header("Fruityvice Fruit Advice!")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information")
    else:
#         streamlit.write('The user entered ', fruit_choice)
        result = get_fruityvice_data(fruit_choice)
        streamlit.dataframe(result)
except URLError as e:
    streamlit.stop()

# import pandas
# my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
# my_cur = my_cnx.cursor()
# my_cur.execute("SELECT * from fruit_load_list")
# my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
def get_fruit_load():
    with my_cnx.cursor() as cur:
        cur.execute("select * from fruit_load_list")
        return cur.fetchall()
if streamlit.button('Get fruit load list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load()
    streamlit.dataframe(my_data_rows)

# streamlit.test("What fruit would you like to add:")
def insert_row_snowflake(new_fruit):
    witg my_cnx.cursor() as cur:
        cur.execute("insert into fruit_load_list values('from streamlit')")
        return "Thanks for adding :" + new_fruit
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    result = insert_row_snowflake(add_my_fruit)
    streamlit.text(result)

