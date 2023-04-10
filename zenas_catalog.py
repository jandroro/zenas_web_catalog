import streamlit as sl
import snowflake.connector as sf
import pandas as pd

sl.title('Zena\'s Amazing Athleisure Catalog')

# Connect to Snowflake
my_cnx = sf.connect(**sl.secrets['snowflake'])
my_cur = my_cnx.cursor()

# Run a Snowflake query and put it all in a var called my_catalog
my_cur.execute('SELECT color_or_style FROM catalog_for_website')
my_catalog = my_cur.fetchall()

# Put the data into a dataframe
df = pd.DataFrame(my_catalog)

# Temp write the dataframe to the page so I can see what I am working with
sl.write(df)

# Put the first column into a list
color_list = df[0].values.tolist()
print(color_list)
