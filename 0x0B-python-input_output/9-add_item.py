#!/usr/bin/python3
"""
Script to load and save
"""
import json
import sys
import os.path as path

save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

fname = "add_item.json"
if path.exists(fname):
    lista = load(fname)
else:
    lista = []

if len(sys.argv) > 1:
    for args in sys.argv[1:]:
        lista.append(args)

save(lista, fname)
