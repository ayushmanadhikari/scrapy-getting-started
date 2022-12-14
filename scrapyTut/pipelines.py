# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class ScrapytutPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()


    def create_connection(self):
        self.conn = sqlite3.connect('myquotes.db')
        self.cursor = self.conn.cursor()


    def create_table(self):
        self.cursor.execute("""
            drop table if exists quotes_tbl
        """)

        self.cursor.execute("""
            create table quotes_tbl (
                title text,
                author text,
                tags text
            )
        """)
    
    def store_db(self, item):
        self.cursor.execute("""
            insert into quotes_tbl values (?,?,?)""", (
            item['title'][0],
            item['author'][0], 
            item['tags'][0] 
        ))
        self.conn.commit()



    def process_item(self, item, spider):
        self.store_db(item)
        return item
