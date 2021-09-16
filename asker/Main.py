#-*- coding: utf-8 -*-

from asker import Asker
from launch_dtb import Init_Dtb
from constants import DTB, CATEGORIES


if __name__ == '__main__':
    #App home msg.
    Asker.home()
    #Check or create dtb
    Init_Dtb(DTB, CATEGORIES)
    #User interface launch.
    Asker()