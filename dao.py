import sqlite3
conn = sqlite3.connect('./db/user.db')

c = conn.cursor()
create_table="CREATE TABLE user (id int, name varchar(64))"
c.execute(create_table)
conn.commit()
conn.close()