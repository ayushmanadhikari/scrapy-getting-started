import sqlite3


conn = sqlite3.connect('myquotes.db')
cursor = conn.cursor()

# cursor.execute(""" CREATE TABLE quotes_tb (
#                     title text,
#                     author text,
#                     tag text
#                 ) """)


cursor.execute("""
insert into quotes_tb 
values ('Python is great', 'ayusman', 'prgramming, problem-solving')
""")

conn.commit()
conn.close()