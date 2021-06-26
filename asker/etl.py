#-*- coding: utf-8 -*-

from os import system
import requests


class Etl:
    def __init__(self, categories_list):
        self.categories_list = categories_list
        self.querycat = self.get_json_from_catname()
        self.products = self.transform_for_sql_insertion()
        
        
    def get_json_from_catname(self):
        """Function to get json file with all needed products from OpenFoodFacts."""
        all_query_cat = {}
        catnamestr = ", ".join(self.categories_list)
        system("cls")
        print(f"Récupération des produits des categories {catnamestr}.\nVeuillez patienter!")
        for element in self.categories_list:
            categreq = requests.get("https://world.openfoodfacts.org/cgi/search.pl?tagtype_0=categories&tag_contains_0=\
            contains&tag_0=" + element + "&tagtype_1=languages&tag_contains_1=contains&tag_1=fr\
            &page_size=150&search_simple=1&action=process&json=1").json()
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
                    found_product = (self.name, self.categories_list[countind], self.nutrition_grades, self.store, self.description, self.url)
                    allproducts.append(found_product)
            countind += 1
        return allproducts