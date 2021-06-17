# -*- coding: utf-8 -*-

from send_query import make_Query
import constants as cst

class Stores():
    def find_stores():
        black_mail = make_Query(cst.user, "SELECT DISTINCT store_product FROM product", "READ", cst.use_dtb)
        return black_mail