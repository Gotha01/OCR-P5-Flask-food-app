# -*- coding: utf-8 -*-

from os import system
from send_query import Make_Query
from constants import SQL_CONNECTORS, DTB
from display import display

class Favourites():
    def init_table():
        Make_Query(SQL_CONNECTORS,
            """CREATE TABLE IF NOT EXISTS favourites
            (
                id_favourite SMALLINT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                favourite_product_ID SMALLINT UNSIGNED NOT NULL,
                substituted_product_ID SMALLINT UNSIGNED NOT NULL,
                CONSTRAINT fk_favourite_product_ID FOREIGN KEY (favourite_product_ID) REFERENCES product(id_product) ON DELETE CASCADE,
                CONSTRAINT fk_substituted_product_ID FOREIGN KEY (substituted_product_ID) REFERENCES product(id_product) ON DELETE CASCADE
            )
            ENGINE=INNODB;""", "CREATE", DTB)

    def record_product(favorite_prod_ids, substituted_prod_ids):
        Make_Query(SQL_CONNECTORS, f"""INSERT IGNORE INTO\
            favourites(favourite_product_ID,substituted_product_ID)\
            VALUES({favorite_prod_ids},{substituted_prod_ids})""",
            "UPDATE", DTB)

    def display_favourite_product(ident, ident2):
        favourite_prod = Make_Query(
            SQL_CONNECTORS, f"SELECT * FROM product WHERE id_product={ident}",
            "READ", DTB).result[0]
        substituted_prod = Make_Query(
            SQL_CONNECTORS, f"SELECT * FROM product WHERE id_product={ident2}",
            "READ", DTB).result[0]
        replace_fp = favourite_prod[4].replace("[", "").replace("]", "")
        replace_sp = substituted_prod[4].replace("[", "").replace("]", "")
        fav_and_sub_details = [f"Produit favoris : {favourite_prod[1]}",
            "Description : ", f"{favourite_prod[5]}",
            "Valeur nutritionnelle : ", f"{favourite_prod[3]}",
            "URL : ", f"{favourite_prod[6]}",
            "Magasins : ", f"""{replace_fp.replace(",", ", ")}""",
            "",
            "Produit substitué :", f"{substituted_prod[1]}",
            "Description :", f"{substituted_prod[5]}",
            "Valeur nutritionnelle :", f"{substituted_prod[3]}",
            "URL :", f"{substituted_prod[6]}",
            "Magasins :", f"""{replace_sp.replace(",", ", ")}"""]
        system("cls")
        input(display(150, "=", fav_and_sub_details, False, "|"))
    
    def display_all_favourite_product():
        all_fav = Make_Query(SQL_CONNECTORS,
            "SELECT favourite_product_ID,substituted_product_ID FROM favourites;",
            "READ", DTB).result
        return all_fav

    def suppress_all():
        Make_Query(SQL_CONNECTORS, "TRUNCATE TABLE favourites;", "DELETE", DTB)