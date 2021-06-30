# -*- coding: utf-8 -*-

from send_query import make_Query
from constants import *

class Categories:
    def __init__(self, categories):
        self.categories = categories
        self.url = self.find_url()

    def init_table():
        make_Query(
            user,
            '''CREATE TABLE IF NOT EXISTS category
            (
                id SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE,
                url VARCHAR(100) NOT NULL
            )
            ENGINE=INNODB;''',
            "CREATE", dtb)

    def find_url(self):
        found_url = "https://fr.openfoodfacts.org/categorie/%s".format(*self.categories)
        return found_url

    def update_category_values(self):
        for name in self.categories:
            make_Query(user, f"INSERT IGNORE INTO category(name, url) VALUES('{name}', '{self.url}')", "UPDATE", dtb)
        
    def read_column_sql(column, where=None):
        column_result = []
        if where != None:
            query = make_Query(user, f"SELECT `{column}` FROM category {where}", "READ", dtb).result
        else:
            query = make_Query(user, f"SELECT `{column}` FROM category", "READ", dtb).result
        for elements in query:
            for element in elements:
                column_result.append(element)
        return column_result