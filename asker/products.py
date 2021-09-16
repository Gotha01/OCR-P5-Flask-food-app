# -*- coding: utf-8 -*-

from os import system

from send_query import Make_Query
from constants import SQL_CONNECTORS, DTB
from etl import Etl
from display import display

class Product:
    def __init__(self, categories):
        self.list_categories = categories
        self.json_products = Etl(self.list_categories)
        self.all_prod = []
    
    def init_table():
        Make_Query(
            SQL_CONNECTORS,
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
            "CREATE", DTB)
        
    def display_product(column=[], ref_to_check="", value_to_check="",
                        comparator="AND", second_ref="", second_value="",
                        order_by="", numlimit=0, numtypelimit=""):
        selected_column = ",".join(column)
        condition = f"WHERE {ref_to_check} LIKE '{value_to_check}'"
        condition_2 = f" {comparator} {second_ref} LIKE '{second_value}'"
        number_to_check = f" ORDER BY {order_by} {numtypelimit} LIMIT {numlimit}"
        if ref_to_check == "" and order_by == "":
            display = Make_Query(SQL_CONNECTORS, 
                f"SELECT {selected_column} FROM product",
                 "READ", DTB).result
        elif ref_to_check != "" and order_by == "":
            if second_ref == "":
                display = Make_Query(SQL_CONNECTORS, 
                    f"SELECT {selected_column} FROM product {condition}",
                     "READ", DTB).result
            else:
                display = Make_Query(SQL_CONNECTORS, 
                    f"SELECT {selected_column} FROM product {condition}{condition_2}",
                     "READ", DTB).result
        elif ref_to_check == "" and order_by != "":
            display = Make_Query(SQL_CONNECTORS,
                f"SELECT {selected_column} FROM product {number_to_check}",
                 "READ", DTB).result
        elif ref_to_check != "" and order_by != "":
            if second_ref == "":
                display = Make_Query(SQL_CONNECTORS, 
                    f"SELECT {selected_column} FROM product {condition}{number_to_check}",
                     "READ", DTB).result
            else:
                display = Make_Query(SQL_CONNECTORS,
                     f"SELECT {selected_column} FROM product {condition}{condition_2}{number_to_check}",
                      "READ", DTB).result
        return display
        
    def insert_product_values(self, print_count_values=False):
        product_insert = 0
        product_already_check = 0
        for element in self.json_products.products:
            all_products = product_insert + product_already_check
            VERIF = ["Vérification des produits enregistrés.",
                     "Produits dans la base de données :",
                    f"{all_products} / {len(self.json_products.products)}"]
            if all_products %10 == 0:
                system("cls")
                if print_count_values:
                    print(display(150, "=", VERIF, 2, "|"))
            self.brow_value = Make_Query(SQL_CONNECTORS,
                f'SELECT name_product FROM product WHERE name_product = "{element[0]}"',
                "READ", DTB).result
            if self.brow_value == []:
                self.category_id = int(Make_Query(SQL_CONNECTORS,
                    f"SELECT id FROM category WHERE name='{element[1]}'",
                    "READ", DTB).result[0][0])
                Make_Query(SQL_CONNECTORS, 
                        f'INSERT INTO product(name_product, category_ID,\
                             nutrition_grades_product, store_product, \
                                 description_product, url_product)\
                        VALUES("{element[0]}","{self.category_id}","{element[2]}","{element[3]}","{element[4]}","{element[5]}")', 
                        "UPDATE", DTB)  
                product_insert += 1
                self.all_prod.append(element[0])
            else:
                product_already_check +=1
        return self.all_prod