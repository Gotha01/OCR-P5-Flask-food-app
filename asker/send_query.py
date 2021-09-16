# -*- coding: utf-8 -*-

import mysql.connector as mys
from constants import *


class Make_Query():
    def __init__(self, sql_config, sql_Query, CRUD_Operation, target_Database = "0"):
        """Init a new query for a mysql server

        Args:
            sql_config (dict): ['key' = 'param' : 'value' = 'value']
            sql_Query (string): ['query']
            CRUD_Operation (string): [choose in : "CREATE","READ","UPDATE","DELETE"]
            target_Database (string): ["USE database_name;"]
        """

        self.config = sql_config
        self.sql_Query = sql_Query
        self.CRUD = CRUD_Operation
        self.target_Database = target_Database
        
        CRUD = {
        "CREATE" : self.creator_suppressor,
        "DELETE" : self.creator_suppressor,
        "READ" : self.reader,
        "UPDATE" : self.updater,
        "EXECUTE" : self.execute
        }
        
        try: 
            CRUD[self.CRUD].__call__()
        except KeyError as bad_key:
            print("{} 1".format(bad_key))

    def create_cursor_connection(self):
        try:
            self.connect = mys.connect(**self.config)
            self.cursor = self.connect.cursor()
        except mys.Error as err:
            self.connect.rollback() #rollback if exception
            print("Query canceled, SQL error : {}".format(err))
        
    def close_cursor_connection(self):
        if self.connect.is_connected():
                self.cursor.close()
                self.connect.close()
    
    def creator_suppressor(self):
        self.create_cursor_connection()
        if self.target_Database.isdigit() == False :
            self.cursor.execute(f"USE {self.target_Database}")
        self.cursor.execute(self.sql_Query)
        self.close_cursor_connection()

    def reader(self):
        self.create_cursor_connection()
        if self.target_Database != "0":
            self.cursor.execute(f"USE {self.target_Database}")
        self.cursor.execute(self.sql_Query)
        self.result = self.cursor.fetchall()
        return self.result

    def updater(self):
        self.create_cursor_connection()
        self.cursor.execute(f"USE {self.target_Database}")
        self.cursor.execute(self.sql_Query)
        self.connect.commit()
        self.close_cursor_connection()

    def execute(self):
        self.create_cursor_connection()
        self.cursor.execute(self.sql_Query)
        self.close_cursor_connection()