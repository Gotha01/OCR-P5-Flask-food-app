#-*- coding: utf-8 -*-

import mysql.connector as mys
from send_query import make_Query
from categories import Categories
from constants import *
from products import Product


class check_dtb():
    def __init__(self):
        self.check_err = mys.errors.ProgrammingError
        self.tables = [('category',), ('product',), ('substituted',)]
        self.values_category = [('boissons',), ('pates',), ('pizzas',), ('snacks',)]
        
        #Check if dtb 'projet5' exists.
        try:
            make_Query(user, use_dtb, "EXECUTE")
        except self.check_err:
            for element in init_Dtb:
                make_Query(user, element, "CREATE")
            print("Database correctly initialized")

        #Checking the database tables.
        read_tables = make_Query(user, "SHOW tables;", "READ", use_dtb).result
        if read_tables != self.tables:
            for element in init_Tables:
                make_Query(user, element, "CREATE", use_dtb)
            print("Tables correctly created")

        #Checking category values.
        read_category = make_Query(user, "SELECT name FROM category;", "READ", use_dtb).result
        if read_category != self.values_category:
            for value in self.values_category:
                for element in value:
                    Categories(element).create_category_values()
            print("Correct implementation of categories")
            
        #Create values in "product" table
        Product()