#!/usr/bin/python3
"""a module for task 7

a script that adds all arguments to a
Python list, and then save them to a file
"""

import sys


content = sys.argv[1:]
load = __import__("6-load_from_json_file").load_from_json_file
save = __import__("5-save_to_json_file").save_to_json_file

try:
    old_content = load("add_item.json")
    old_content.extend(content)
except:
    old_content = content

save(old_content, "add_item.json")
