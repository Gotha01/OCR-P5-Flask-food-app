# -*- coding: utf-8 -*-


from sql_requests import *


class Table:
""" This class delete and re-create "Projet5" Database with tables: Category, Product, Substituted """
    def __init__(self):
        make_query("""DROP DATABASE IF EXISTS projet5;
            CREATE DATABASE projet5;
            USE projet5;
            CREATE TABLE Category 
            (
                id SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(100) NOT NULL UNIQUE,
                url VARCHAR(100) NOT NULL
            )
            ENGINE=INNODB;
            CREATE TABLE Product 
            (
                id_product SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                name_product VARCHAR(100) NOT NULL,
                category_ID SMALLINT UNSIGNED NOT NULL,
                nutrition_grades_product VARCHAR(1) NOT NULL,
                store_product VARCHAR(100),
                description_product VARCHAR(1000) NOT NULL,
                url_product VARCHAR(1000) NOT NULL,
                CONSTRAINT fk_product_category_ID FOREIGN KEY (category_ID) REFERENCES category(id) ON DELETE CASCADE
            )
            ENGINE=INNODB;
            CREATE TABLE Substituted 
            (
                id_substituted SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                original_product_ID SMALLINT UNSIGNED NOT NULL,
                substituted_product_ID SMALLINT UNSIGNED NOT NULL,
                CONSTRAINT fk_original_product_ID FOREIGN KEY (original_product_ID) REFERENCES product(id_product) ON DELETE CASCADE,
                CONSTRAINT fk_substituted_product_ID FOREIGN KEY (substituted_product_ID) REFERENCES product(id_product) ON DELETE CASCADE,
                UNIQUE INDEX ind_original_product_ID_substituted_product_ID (original_product_ID, substituted_product_ID)
            )
            ENGINE=INNODB;
            """, method = "creation")