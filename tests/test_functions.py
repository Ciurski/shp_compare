# -*- coding: utf-8 -*-

import unittest
import os
from main_module.functions import list_all_shp, list_shp_fields, compare_headers

class TestListAllShp(unittest.TestCase):
    def test_listing(self):
        path = os.getcwd()+"/files/list_test"
        shp_list = list_all_shp(path)
        self.assertEqual(len(shp_list), 4)


class TestListShpFields(unittest.TestCase):
    def test_fields(self):
        path = os.getcwd()+"/files/list_test"
        shp_list = list_all_shp(path)
        headers, field_names, field_params, incompatibilities = list_shp_fields(shp_list)
        self.assertEqual(len(incompatibilities), 0)

    def test_incompatibilities(self):
        path = os.getcwd()+"/files/list_test"
        shp_list = list_all_shp(path)
        headers, field_names, field_params, incompatibilities = list_shp_fields(shp_list)
        self.assertEqual(len(incompatibilities), 0)


class TestCompareHeaders(unittest.TestCase):
    def test_order(self):
        path = os.path.dirname(os.getcwd()) + "/tests/files/headers_differ/order/pattern_one"
        shp_list_one = list_all_shp(path)
        headers_one, field_names_one, field_params_one, incompatibilities_one = list_shp_fields(shp_list_one)
        path = os.path.dirname(os.getcwd()) + "/tests/files/headers_differ/order/pattern_two"
        shp_list_two = list_all_shp(path)
        headers_two, field_names_two, field_params_two, incompatibilities_two = list_shp_fields(shp_list_two)
        error = compare_headers(headers_one, headers_two)
        self.assertEqual(error, "order")

    def test_subset(self):
        path = os.path.dirname(os.getcwd()) + "/tests/files/headers_differ/subset/pattern_one"
        shp_list_one = list_all_shp(path)
        headers_one, field_names_one, field_params_one, incompatibilities_one = list_shp_fields(shp_list_one)
        path = os.path.dirname(os.getcwd()) + "/tests/files/headers_differ/subset/pattern_two"
        shp_list_two = list_all_shp(path)
        headers_two, field_names_two, field_params_two, incompatibilities_two = list_shp_fields(shp_list_two)
        error = compare_headers(headers_one, headers_two)
        self.assertEqual(error, "subset")

    def test_superset(self):
        path = os.path.dirname(os.getcwd()) + "/tests/files/headers_differ/superset/pattern_one"
        shp_list_one = list_all_shp(path)
        headers_one, field_names_one, field_params_one, incompatibilities_one = list_shp_fields(shp_list_one)
        path = os.path.dirname(os.getcwd()) + "/tests/files/headers_differ/superset/pattern_two"
        shp_list_two = list_all_shp(path)
        headers_two, field_names_two, field_params_two, incompatibilities_two = list_shp_fields(shp_list_two)
        error = compare_headers(headers_one, headers_two)
        self.assertEqual(error, "superset")

    def test_bad_name(self):
        path = os.getcwd()+"/files/headers_differ/bad_name/pattern_one"
        shp_list_one = list_all_shp(path)
        headers_one, field_names_one, field_params_one, incompatibilities_one = list_shp_fields(shp_list_one)
        path = os.getcwd()+"/files/headers_differ/bad_name/pattern_two"
        shp_list_two = list_all_shp(path)
        headers_two, field_names_two, field_params_two, incompatibilities_two = list_shp_fields(shp_list_two)
        compare_headers(headers_one, headers_two)

    def test_bad_type(self):
        path = os.getcwd() + "/files/headers_differ/bad_type/pattern_one"
        shp_list_one = list_all_shp(path)
        headers_one, field_names_one, field_params_one, incompatibilities_one = list_shp_fields(shp_list_one)
        path = os.getcwd() + "/files/headers_differ/bad_type/pattern_two"
        shp_list_two = list_all_shp(path)
        headers_two, field_names_two, field_params_two, incompatibilities_two = list_shp_fields(shp_list_two)
        compare_headers(headers_one, headers_two)


if __name__ == '__main__':
    unittest.main()