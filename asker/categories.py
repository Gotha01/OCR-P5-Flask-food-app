# -*- coding: utf-8 -*-

from send_query import Make_Query
from constants import SQL_CONNECTORS, DTB

class Categories:
    def __init__(self, categories):
        self.categories = categories
        self.url = self.find_url()

    def init_table():
        Make_Query(
            SQL_CONNECTORS,
            '''CREATE TABLE IF NOT EXISTS category
            (
                id SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE,
                url VARCHAR(100) NOT NULL
            )
            ENGINE=INNODB;''',
            "CREATE", DTB)

    def find_url(self):
        found_url = "https://fr.openfoodfacts.org/categorie/%s".format(*self.categories)
        return found_url

    def update_category_values(self):
        for name in self.categories:
            Make_Query(SQL_CONNECTORS, f"INSERT IGNORE INTO category(name, url) VALUES('{name}', '{self.url}')", "UPDATE", DTB)
        
    def read_column_sql(column, where=None):
        column_result = []
        if where != None:
            query = Make_Query(SQL_CONNECTORS, f"SELECT `{column}` FROM category {where}", "READ", DTB).result
        else:
            query = Make_Query(SQL_CONNECTORS, f"SELECT `{column}` FROM category", "READ", DTB).result
        for elements in query:
            for element in elements:
                column_result.append(element)
        return column_result