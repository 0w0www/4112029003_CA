import sqlite3


conn = sqlite3.connect('BBq.db')

conn.execute('''
    CREATE TABLE IF NOT EXISTS meat (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER,
        quantity INTEGER
    )
''')


conn.execute("INSERT INTO meat (name, price, quantity) VALUES ('chicken',30,5)")
conn.execute("INSERT INTO meat (name, price, quantity) VALUES ('beaf',55,10)")
conn.execute("INSERT INTO meat (name, price, quantity) VALUES ('pork',40,15)")

conn.commit()
cursor = conn.execute("SELECT * FROM meat")
print("表格內容:")
for row in cursor:
    print(row)

conn.execute("UPDATE meat SET price = 35 WHERE name = 'pork'")
conn.execute("UPDATE meat SET quantity = 30 WHERE name = 'chicken'")

conn.commit()
cursor = conn.execute("SELECT * FROM meat")
print("\n表格內容 (更新後):")
for row in cursor:
    print(row)

conn.execute("DELETE FROM meat WHERE price =40")

conn.commit()
cursor = conn.execute("SELECT * FROM meat")
print("\n表格內容 (刪除後):")
for row in cursor:
    print(row)


conn.close()