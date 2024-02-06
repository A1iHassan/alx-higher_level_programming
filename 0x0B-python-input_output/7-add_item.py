#!/usr/bin/python3
"""a module for task 7

a script that adds all arguments to a
Python list, and then save them to a file
"""

import sys


content = sys.argv[1:]
load = __import__("6-load_from_json_file").load_from_json_file
save = __import__("5-save_to_json_file").save_to_json_file

content.append(load("add_item.json"))
save(content, "add_item.json")
