# -*- coding: utf-8 -*-

import os

def list_all_shp(path):
    shapes = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if ".shp" in file[-4:]:
                shapes.append(os.path.join(root, file))
    return shapes