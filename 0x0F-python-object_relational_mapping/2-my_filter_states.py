#!/usr/bin/python3
"""
task 2 answer
"""
if __name__ == '__main__':
    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    d_b = sys.argv[3]
    search = sys.argv[4]

    database = MySQLdb.connect(
        host='localhost',
        user=user_name,
        password=pass_word,
        db=d_b,
        port=3306
    )

    cursor = database.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE '{}' ORDER BY id ASC;"
        .format(search))
    results = cursor.fetchall()
    for line in results:
        print(line)
