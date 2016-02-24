#pyinstaller --onefile script.py
import mysql.connector

conn = mysql.connector.connect(user='#', password='#', host='#', database='#')
cr = conn.cursor()
query = "SELECT * FROM logs"
cr.execute(query)
for (id, info) in cr:
	print(info, end="")

cr.close()
conn.close()