#-*- coding: utf-8 -*-

from asker import Asker_p5
from launch_dtb import check_dtb

if __name__ == '__main__':
    #App home msg.
    Asker_p5.home()

    #Check or create dtb
    check_dtb()

    #User interface launch.
    Asker_p5()
    
