import sys,os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '\\..\\')
import dao


dao.create("CREATE TABLE IF NOT EXISTS user (id int, name varchar(64))")
dao.insert("INSERT INTO user(id, name) VALUES(?,?)", [123, "taro"])
dao.select("SELECT * FROM user", True)
dao.update("UPDATE user SET name=? WHERE id=?", ["goro", 123])
dao.delete("DELETE FROM user WHERE id=?", [123])
dao.select("SELECT * FROM user", True)
