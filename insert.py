import mysql.connector

# Verbindung zur Datenbank herstellen
mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    password="test",
    database="myDb"
)

# Cursor erstellen
mycursor = mydb.cursor()

# SQL-Abfrage ausführen
sql = "INSERT INTO foo (name) VALUES (%s)"
val = ("Sample content of the post",)  # Note the comma to make it a tuple

mycursor.execute(sql, val)

# Änderungen an der Datenbank vornehmen
mydb.commit()

# Anzahl der betroffenen Zeilen anzeigen
affected_rows = mycursor.rowcount
print("Number of affected rows:", affected_rows)

# Verbindung schließen
mydb.close()
