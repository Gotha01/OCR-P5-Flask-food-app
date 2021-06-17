# -*- coding: utf-8 -*-

import mysql.connector as mys
import constants as cst

class make_Query():
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
        "CREATE" or "DELETE" : self.sql_Query_Creator_Suppressor,
        "READ" : self.sql_Query_Reader,
        "UPDATE" : self.sql_Query_Updater,
        "EXECUTE" : self.sql_Query_execute
        }
        
        try: 
            CRUD[self.CRUD].__call__()
        except KeyError as bad_key:
            print("{}".format(bad_key))

    def create_Cursor_Connection(self):
        try:
            self.connect = mys.connect(**self.config)
            self.cursor = self.connect.cursor()
        except mys.Error as err:
            self.connect.rollback() #rollback if exception
            print("Query canceled, SQL error : {}".format(err))
        
    def close_Cursor_Connection(self):
        if self.connect.is_connected():
                self.cursor.close()
                self.connect.close()
    
    def sql_Query_Creator_Suppressor(self):
        self.create_Cursor_Connection()
        if self.target_Database.isdigit() == False :
            self.cursor.execute(self.target_Database)
        self.cursor.execute(self.sql_Query)
        self.close_Cursor_Connection()

    def sql_Query_Reader(self):
        self.create_Cursor_Connection()
        if self.target_Database != "0":
            self.cursor.execute(self.target_Database)
        self.cursor.execute(self.sql_Query)
        self.result = self.cursor.fetchall()
        return self.result

    def sql_Query_Updater(self):
        self.create_Cursor_Connection()
        self.cursor.execute(self.target_Database)
        self.cursor.execute(self.sql_Query)
        self.connect.commit()
        self.close_Cursor_Connection()

    def sql_Query_execute(self):
        self.create_Cursor_Connection()
        self.cursor.execute(self.sql_Query)
        self.close_Cursor_Connection()