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
# sl.write(df)

# Put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)

# Let's put a pick list here so they can pick the color
option = sl.selectbox('pick a sweatsuit color or style:', list(color_list))

# We'll build the image caption now, since we can
product_caption = 'Our warm, comortable, ' + option + ' sweatsuit!'

# Use the option selected to go bacj and get all the info from the database
my_cur.execute("SELECT direct_url, price, size_list, upsell_product_desc FROM catalog_for_website WHERE color_or_style = '" + option + "';")
df2 = my_cur.fetchone()

sl.image(
  df2[0],
  width = 400,
  caption = product_caption
)

sl.write('Price: ', df2[1])
sl.write('Sizes Available: ', df2[2])
sl.write(df2[3])
