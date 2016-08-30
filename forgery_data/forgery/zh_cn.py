# -*- coding: utf-8 -*-

"""

    forgery_data.forgery.zh-cn
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/29/16

"""

from basic import *


class ForgeryDataZH_CN(ForgeryData):

    locale = "zh-cn"

    def name(self):

        return random.choice(self.get_data("name")).strip()

    def province(self):

        return random.choice(self.get_data("province")).strip()

