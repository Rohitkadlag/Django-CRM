import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Rohit$2002',

)

cursorObject = dataBase.cursor()


cursorObject.execute("CREATE DATABASE rohit")

print('alldone!')

