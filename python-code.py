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
mycursor.execute("SELECT * FROM wp_posts")

# Ergebnis abrufen
result = mycursor.fetchall()

print("affected rows", mycursor.rowcount)

# Ergebnis anzeigen
# for row in result:
#   print(row)

# Verbindung schließen
mydb.close()
