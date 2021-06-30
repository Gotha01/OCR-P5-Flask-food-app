#-*- coding: utf-8 -*-

from asker import Asker_p5
from launch_dtb import init_dtb
from constants import dtb, categories


if __name__ == '__main__':
    #App home msg.
    Asker_p5.home()
    #Check or create dtb
    init_dtb(dtb, categories)
    #User interface launch.
    Asker_p5()