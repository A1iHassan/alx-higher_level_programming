#!/usr/bin/python3
"""
task 4 answer
"""
if __name__ == '__main__':

    import MySQLdb
    import sys

    user_name = sys.argv[1]
    pass_word = sys.argv[2]
    d_b = sys.argv[3]

    database = MySQLdb.connect(
        host='localhost',
        user=user_name,
        password=pass_word,
        db=d_b,
        port=3306
    )

    cursor = database.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = {}
                   ORDER BY cities.id ASC;""", (sys.arg[4],))
    results = cursor.fetchall()
    for line in results:
        print(line)
