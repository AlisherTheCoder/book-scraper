# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class PostgresPipeline(object):
    try:
        def open_spider(self, spider):
            hostname = 'localhost'
            username = 'postgres'
            password = 'Ali123123'
            database = 'books'
            self.conn = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
            self.cur = self.conn.cursor()
            self.cur.execute("CREATE TABLE Abooks(title text, link text )")

            # self.connection = sqlite3.connect('book.db')
            # self.cur = self.connection.cursor()
            # self.cur.execute("CREATE TABLE Bbooks(title text, link text )")
            # self.connection.commit()

        def close_spider(self, spider):
            self.conn.close()

        def process_item(self, item, spider):
            self.cur.execute("""
                INSERT INTO Abooks (title, link) values (?, ?), (item.get('book_title')),
                                                                (item.get('link_to_download'))
                          
                    """)

            return item
    except OperationalError:
        print("Could not connect to database")

