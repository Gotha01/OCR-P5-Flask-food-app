# -*- coding: utf-8 -*-

from send_query import make_Query
import constants as cst

class Categories:
    def __init__(self, name=""):
        self.name = name
        self.url = self.find_url()

    def find_url(self):
        found_url = "https://fr.openfoodfacts.org/categorie/" + self.name
        return found_url

    def read_column_sql(self, column, where=None):
        self.column_result = []
        if where != None:
            self.query = make_Query(cst.user, f"SELECT `{column}` FROM category {where}", "READ", cst.use_dtb).result
        else:
            self.query = make_Query(cst.user, f"SELECT `{column}` FROM category", "READ", cst.use_dtb).result
        for elements in self.query:
            for element in elements:
                self.column_result.append(element)
        return self.column_result
        
    def create_category_values(self):
        result = make_Query(cst.user, f"INSERT INTO category(name, url) VALUES('{self.name}', '{self.url}')", "UPDATE", cst.use_dtb)
        return result