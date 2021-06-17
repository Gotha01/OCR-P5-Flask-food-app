#-*- coding: utf-8 -*-

import requests


class Etl:
    def __init__(self, categories_name):
        self.categories_name = categories_name
        self.querycat = self.get_json_from_catname()
        self.products = self.transform_for_sql_insertion()
        
        
    def get_json_from_catname(self):
        """Get json file from openfoodfacts."""
        all_query_cat = {}
        for element in self.categories_name:
            print(f"Récupération des produits de la categorie {element}")
            categreq = requests.get("https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=\
            contains&tag_0=" + element + "&tagtype_1=languages&tag_contains_1=contains&tag_1=fr\
            &page_size=100&search_simple=1&action=process&json=1").json()
            all_query_cat[element] = categreq
        return all_query_cat


    def transform_for_sql_insertion(self):
        allproducts = []
        countind = 0
        for val in self.querycat.values():
            for value in val["products"]:
                if "nutrition_grades" in value and "product_name_fr" in value and "generic_name" in value\
                        and "url" in value and value["nutrition_grades"] in ["a", "b", "c", "d", "e"]\
                        and value["product_name_fr"] != "" and "\n" not in value["product_name_fr"]\
                        and value["generic_name"] != "":
                    self.name = value['product_name_fr']
                    self.nutrition_grades = value["nutrition_grades"]
                    self.url = value["url"]
                    self.description = value["generic_name"]
                    if "stores" in value:
                        self.store = []
                        self.store.append(value["stores"])
                    else:
                        self.store = "Aucun magasin ne propose ce produit"
                    found_product = (self.name, self.categories_name[countind], self.nutrition_grades, self.store, self.description, self.url)
                    allproducts.append(found_product)
            countind += 1
        return allproducts