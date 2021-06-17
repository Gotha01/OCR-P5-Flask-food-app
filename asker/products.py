# -*- coding: utf-8 -*-

from os import system

import send_query as sq
import constants as cst
from categories import Categories
from etl import Etl


class Product:
    def __init__(self):
        self.list_categories = []
        self.find_categories()
        self.products = Etl(self.list_categories)
        self.create_product_values()

    def find_categories(self):
        for element in Categories().read_column_sql("name"):
            self.list_categories.append(element)
        
    def create_product_values(self):
        product_insert = 0
        product_already_check = 0
        for element in self.products.products:
            if product_insert%10 == 0:
                system("cls")
                print(f"Produits dans la base de données : {product_already_check + product_insert}/208")
            self.brow_value = sq.make_Query(cst.user, f'SELECT name_product FROM product WHERE name_product = "{element[0]}"', "READ", cst.use_dtb).result
            if self.brow_value == []:
                self.category_id = int(sq.make_Query(cst.user, f"SELECT id FROM category WHERE name='{element[1]}'", "READ", cst.use_dtb).result[0][0])
                sq.make_Query(cst.user, f'INSERT INTO product(name_product, category_ID, nutrition_grades_product, store_product, description_product, url_product)\
                VALUES("{element[0]}","{self.category_id}","{element[2]}","{element[3]}","{element[4]}","{element[5]}")', "UPDATE", cst.use_dtb)  
                product_insert += 1
            else:
                product_already_check +=1

    def check_for_five_products(category):
        which_category_id = Categories().read_column_sql("id", f"WHERE name='{category}'")[0]
        result = sq.make_Query(cst.user, f"SELECT name_product FROM product WHERE category_ID LIKE '{which_category_id}'\
            ORDER BY nutrition_grades_product ASC LIMIT 5",\
             "READ", cst.use_dtb).result
        return result

    def check_one_product(product_to_check):
        sq.make_Query(cst.user, f"SELECT * FROM product WHERE name={product_to_check}", "READ", cst.use_dtb)