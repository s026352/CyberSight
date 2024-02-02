import sqlite3


def read_db():
    # Connect to database
    conn = sqlite3.connect('Couche_Tard_1_Aisle.db')
    c = conn.cursor()

    # Query database
    c.execute("SELECT * FROM Items;")
    rows = c.fetchall()

    # Close connection
    conn.close()

    return rows

for row in read_db():
    print(row)