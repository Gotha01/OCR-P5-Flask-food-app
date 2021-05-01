# -*- coding: utf-8 -*-


import mysql.connector as MC


try:
    conn = MC.connect(host = 'localhost', 
                      database = 'projet5',
                      user = 'root', 
                      password = "")
    cursor = conn.cursor()

    req = 'SELECT * FROM '#table
    cursor.execute(req)

    productlist = cursor.fetchall()

    for n in productlist:
        print('nom : {}'.format(n[4]))
except MC.Error as err:
    print(err)
finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()