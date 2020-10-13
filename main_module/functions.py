# -*- coding: utf-8 -*-

import os
import fiona


def list_all_shp(path):
    shapes = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if ".shp" in file[-4:]:
                shapes.append(os.path.join(root, file))
    return shapes


def list_shp_fields(shp_list):
    headers = set()
    field_names = set()
    field_params = {}
    incompatibilities = {}
    for shp in shp_list:
        with fiona.open(shp, "r") as source:
            shp_schema = source.schema

        fields = shp_schema['properties']

        table = []
        for field in fields.keys():
            field_names.add(field)
            table.append(field)

            if field in field_params.keys():
                if field_params[field] != fields[field]:
                    incompatibilities_list = incompatibilities.get(field, [])
                    incompatibilities_list.append((field_params[field], fields[field]))
                    incompatibilities[field] = incompatibilities_list

            else:
                field_params[field] = fields[field]
        headers.add(tuple(table))

    return headers, field_names, field_params, incompatibilities

def compare_list_index(list_one, list_two):
    res = []
    for i, element in enumerate(list_two):
        index = list_one.index(element)
        res.append((i, index))
    return tuple(res)

def compare_headers(headers_patern, headers_to_check):
    for check_header in headers_to_check:
        if check_header not in headers_patern:
            check_header_set = set(check_header)
            for patern in headers_patern:
                error_type = "Not_found"
                patern_set = set(patern)
                # if same set
                if (check_header_set == patern_set):
                    new_index = compare_list_index(patern, check_header)
                    error_type = "order"

                    # order
                # if subset
                elif check_header_set.issubset(patern_set):
                    error_type = "subset"
                    # bad name
                    # bad type
                    # not enough fields
                # if superset
                elif check_header_set.issuperset(patern_set):
                    error_type = "superset"
                    # to many fields
                # partial match
                else:
                    z = check_header_set.intersection(patern_set)
                    if len(z)>0:
                        pass
                # if none not match

            return error_type
    pass


def compare_field_names(names_patern, names_to_check):
    pass


def compare_field_params(params_patern, params_to_check):
    pass


def unify_shp(shp, headers_patern, names_patern, params_patern):
    pass

if __name__ == '__main__':
    path = os.path.dirname(os.getcwd()) + "/tests/files/headers_difer/order/pattern_one"
    shp_list_one = list_all_shp(path)
    headers_one, field_names_one, field_params_one, incompatibilities_one = list_shp_fields(shp_list_one)
    path = os.path.dirname(os.getcwd()) + "/tests/files/headers_difer/order/pattern_two"
    shp_list_two = list_all_shp(path)
    headers_two, field_names_two, field_params_two, incompatibilities_two = list_shp_fields(shp_list_two)
    compare_headers(headers_one, headers_two)