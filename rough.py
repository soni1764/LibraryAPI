# import mysql.connector

# conn = mysql.connector.connect(host="localhost", database="APIDevelop", user="root", password="root")
# cursor = conn.cursor()
# query = "select * from Books2;"
# cursor.execute(query)
# row = cursor.fetchone()
# print(row)
# conn.close()

from utilities.payload import *

query = "select * from Books2;"
print(buildPayloadfromDB(query))

