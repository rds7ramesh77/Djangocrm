import mysql.connector
dataBase=mysql.connector.connect(
    host=   "localhost",
    user=   "root",
    passwd= "@Rds7@Ramesh@",
)


cursorObjec=dataBase.cursor()

cursorObjec.execute("CREATE DATABASE merodb")
print("Database Created Successfully")