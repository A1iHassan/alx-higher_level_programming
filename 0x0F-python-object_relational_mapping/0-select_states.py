#!/usr/bin/python3
"""
task 0 answer
"""
if __name__ == '__main__':

    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    d_b = sys.argv[3]

    database = MySQLdb.connect(
        host='localhost',
        username=user_name,
        password=pass_word,
        db=d_b,
        port=3306
    )

    cursor = database.cursor()
    cursor.execute(f'SELECT * FROM {d_b}')
    results = cursor.fetchall()
    for line in results:
        print(line)
