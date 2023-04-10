import streamlit as sl
import snowflake.connector as sf

sl.title('My web catalog')

# Snowflake
my_cnx = sf.connect(**sl.secrets['snowflake'])

my_cur = my_cnx.cursor()
my_cur.execute('SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()')

my_data_row = my_cur.fetchone()

sl.text('Hello from Snowflake:')
sl.text(my_data_row)
