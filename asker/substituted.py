# -*- coding: utf-8 -*-

from send_query import make_Query
from constants import *


class Substituted():
    def __init__(self):
        pass

    def init_table():
        make_Query(user,'''
            CREATE TABLE IF NOT EXISTS substituted
            (
                id_substituted SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                original_product_ID SMALLINT UNSIGNED NOT NULL,
                substituted_product_ID SMALLINT UNSIGNED NOT NULL,
                CONSTRAINT fk_original_product_ID FOREIGN KEY (original_product_ID) REFERENCES product(id_product) ON DELETE CASCADE,
                CONSTRAINT fk_substituted_product_ID FOREIGN KEY (substituted_product_ID) REFERENCES product(id_product) ON DELETE CASCADE,
                UNIQUE INDEX ind_original_product_ID_substituted_product_ID (original_product_ID, substituted_product_ID)
            )
            ENGINE=INNODB;''',
            "CREATE", dtb)

    def add_substituted_product(original_id, substituted_id):
        query = "INSERT INTO substituted(substituted_product_ID, original_product_ID) VALUES (%s, %s)" % (original_id, substituted_id)
        make_Query(user, query, "UPDATE", dtb)

    def return_substituted_original_product_id():
        sub_ID = make_Query(user, "SELECT substituted_product_ID FROM substituted")
        return sub_ID