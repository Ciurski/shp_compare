# -*- coding: utf-8 -*-

import unittest
import os
from main_module.functions import list_all_shp

class TestListAllShp(unittest.TestCase):
    def test_listing(self):
        path = os.getcwd()+"/files/list_test"
        shp_list = list_all_shp(path)
        self.assertEqual(len(shp_list), 4)
