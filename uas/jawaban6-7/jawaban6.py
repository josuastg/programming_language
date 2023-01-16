import mysql.connector

mydb = mysql.connector.connect(
  host="172.17.3.187", #based on your ip (localhost)
  port=13306,
  user="root",
  password="p455w0rd",
  database = "vehicle"
)

print(mydb)

db = mydb.cursor()

# CREATE DATABASE
db.execute("CREATE DATABASE vehicle")

# SHOW DATABASES
db.execute("SHOW DATABASES")

for x in db:
  print(x)

db.execute("use vehicle")

# CREATE TABLE
# db.execute("CREATE TABLE car (name VARCHAR (225), color VARCHAR(255))")

# SHOW TABLE
# db.execute("SHOW TABLES")

# PRINT TABLE
# for x in db:
#   print(x)






