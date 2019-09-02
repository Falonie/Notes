import sqlite3

with sqlite3.connect('test3.db') as conn:
    cursor = conn.cursor()
    base_command = "ALTER TABLE users ADD COLUMN addresses"
    drop_table="DROP TABLE users"
    cursor.execute(drop_table)
    conn.commit()
