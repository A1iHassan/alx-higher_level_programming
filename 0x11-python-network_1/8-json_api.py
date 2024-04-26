#!/usr/bin/python3
"""
a module for task 8 answer

sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    q = {'q': argv[1]} if len(argv) == 2 else {'q': ""}
    url = 'http://0.0.0.0:5000/search_user'
    r = requests.post(url, data=q)
    try:
        r_dict = r.json()
        id, name = r_dict['id'], r_dict['name']
        if len(r_dict) == 0 or not id or not name:
            print("No result")
        else:
            print(f"[{id}] {name}")
    except Exception:
        print("Not a valid JSON")
