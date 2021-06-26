# -*- coding: utf-8 -*-

from os import system

from send_query import make_Query
from constants import *
from etl import Etl


class Product:
    def __init__(self, categories):
        self.list_categories = categories
        self.json_products = Etl(self.list_categories)
    
    def init_table():
        make_Query(
            user,
            '''CREATE TABLE IF NOT EXISTS product 
            (
                id_product SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                name_product VARCHAR(150) NOT NULL,
                category_ID SMALLINT UNSIGNED NOT NULL,
                nutrition_grades_product VARCHAR(1) NOT NULL,
                store_product VARCHAR(100),
                description_product VARCHAR(1000) NOT NULL,
                url_product VARCHAR(1000) NOT NULL,
                CONSTRAINT fk_product_category_ID FOREIGN KEY (category_ID) REFERENCES category(id)
            )
            ENGINE=INNODB;''',
            "CREATE", dtb)
        
    def display_product(column=[], ref_to_check="", value_to_check="", order_by="", numlimit=0, numtypelimit=""):
        selected_column = ",".join(column)
        condition = f"WHERE {ref_to_check} LIKE '{value_to_check}'"
        number_to_check = f" ORDER BY {order_by} {numtypelimit} LIMIT {numlimit}"
        if ref_to_check == "" and order_by == "":
            display = make_Query(user, f"SELECT {selected_column} FROM product", "READ", dtb).result
        elif ref_to_check != "" and order_by == "":
            display = make_Query(user, f"SELECT {selected_column} FROM product {condition}", "READ", dtb).result
        elif ref_to_check == "" and order_by != "":
            display = make_Query(user, f"SELECT {selected_column} FROM product {number_to_check}", "READ", dtb).result
        elif ref_to_check != "" and order_by != "":
            display = make_Query(user, f"SELECT {selected_column} FROM product {condition}{number_to_check}", "READ", dtb).result
        return display
        
    def insert_product_values(self, print_count_values=False):
        product_insert = 0
        product_already_check = 0
        for element in self.json_products.products:
            all_products = product_insert + product_already_check
            if all_products %10 == 0:
                system("cls")
                if print_count_values:
                    print(f"Vérification des produits enregistrés.\nProduits dans la base de données : {all_products}/{len(self.json_products.products)}")
            self.brow_value = make_Query(user, f'SELECT name_product FROM product WHERE name_product = "{element[0]}"', "READ", dtb).result
            if self.brow_value == []:
                self.category_id = int(make_Query(user, f"SELECT id FROM category WHERE name='{element[1]}'", "READ", dtb).result[0][0])
                make_Query(user, 
                        f'INSERT INTO product(name_product, category_ID, nutrition_grades_product, store_product, description_product, url_product)\
                        VALUES("{element[0]}","{self.category_id}","{element[2]}","{element[3]}","{element[4]}","{element[5]}")', 
                        "UPDATE", dtb)  
                product_insert += 1
            else:
                product_already_check +=1
