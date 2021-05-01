# -*- coding: utf-8 -*-

import requests

class Product:
    __init__(self, category_name):
        self.category_name = category_name
        self.name = ""
        self.sql_category_ID = 0
        self.nutrition_grades = ""
        self.url = ""
        self.description = ""
        self.store = ""
        # get json file from openfoodfacts containing all products of category_name
        self.json = requests.get(f"https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=\
        contains&tag_0={self.category_name}&tagtype_1=languages&tag_contains_1=contains&tag_1=fr\
        &page_size=50&search_simple=1&action=process&json=1").json()