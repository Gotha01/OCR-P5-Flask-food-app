# -*- coding: utf-8 -*-

from send_query import make_Query
from constants import user, dtb

class Favourites():
    def __init__(self):
        pass
    
    def init_table():
        make_Query(user,
            """CREATE TABLE IF NOT EXISTS favourites
            (
                id_favourite SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                favourite_product_ID SMALLINT UNSIGNED NOT NULL,
                favourite_category_ID SMALLINT UNSIGNED NOT NULL,
                CONSTRAINT fk_favourite_product_ID FOREIGN KEY (favourite_product_ID) REFERENCES product(id_product) ON DELETE CASCADE,
                CONSTRAINT fk_favourite_category_ID FOREIGN KEY (favourite_category_ID) REFERENCES category(id) ON DELETE CASCADE
            )
            ENGINE=INNODB;""", "CREATE", dtb)

    def record_aliment(prod_id, categ_id):
        make_Query(user, f"""INSERT IGNORE INTO favourites(favourite_product_ID,favourite_category_ID) VALUES({prod_id},{categ_id})""", "UPDATE", dtb)

    def display_favourite_product(ident):
        favourite_prod = make_Query(user, f"""SELECT * FROM product WHERE id_product={ident}""", "READ", dtb).result
        input(f"""Votre favoris :\n   {favourite_prod[1]}\
            \nDescription :\n    {favourite_prod[5]}\
            \nURL :\n    {favourite_prod[6]}\
            \nMagasins :\n    {favourite_prod[4].replace("[", "").replace("]", "").replace(",", ", ")}""")
    
    def display_all_favourite_product():
        all_fav = make_Query(user, "SELECT DISTINCT favourite_product_ID FROM favourites;", "READ", dtb).result
        return all_fav