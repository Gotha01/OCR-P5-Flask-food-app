#-*- coding: utf-8 -*-

from favourites import Favourites
import mysql.connector as mys
from send_query import make_Query
from constants import *
from categories import Categories
from products import Product
from substituted import Substituted


class init_dtb():
    def __init__(self, database_name, categories_list):
        self.dtb = database_name
        self.categories_list = categories_list
        self.check_err_prog = mys.errors.ProgrammingError
        self.check_err_integ = mys.errors.IntegrityError
        self.check_if_exists()
        self.init_tables()
        self.insert_categories()
        self.insert_products()

    def check_if_exists(self):
            try:
                make_Query(user, f"USE {self.dtb}", "EXECUTE")
            except self.check_err_prog:
                make_Query(user,f"DROP DATABASE IF EXISTS {self.dtb};", "DELETE")
                make_Query(user,f"CREATE DATABASE {self.dtb};", "CREATE")

    def init_tables(self):
        Categories.init_table()
        Product.init_table()
        Substituted.init_table()
        Favourites.init_table()

    def insert_categories(self):
        Categories(self.categories_list).update_category_values()

    def insert_products(self):
        Product(self.categories_list).insert_product_values(True)