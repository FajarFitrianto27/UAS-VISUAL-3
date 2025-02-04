import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",
password="", database="db_penjualan")

myscursor = mydb.cursor()
sql = "INSERT INTO kategori (id, name) VALUES (%s, %s)"
val = [("3", "Drinks"),("4","Tepung")]
myscursor.executemany(sql, val)

print(myscursor.rowcount, "Data Berhasil Ditambahkan.")