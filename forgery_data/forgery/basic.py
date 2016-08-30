# -*- coding: utf-8 -*-

"""

    forgery_data.forgery.basic
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    stamaimer 08/29/16

"""


import codecs
import random


class ForgeryData:

    locale = "basic"

    data_cache = dict()

    def get_data(self, data_name):

        if data_name not in self.data_cache:

            try:

                data_file = codecs.open(filename="data/" + self.locale + "/" + data_name,
                                        mode='r', encoding="utf-8")

            except Exception as e:

                raise

            else:

                self.data_cache[data_name] = data_file.readlines()

                data_file.close()

        return self.data_cache[data_name]

    def email(self):

        return random.choice(self.get_data("email")).strip()

    def password(self):

        return random.choice(self.get_data("password")).strip()
