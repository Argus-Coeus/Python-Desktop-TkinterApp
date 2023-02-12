import mysql.connector



#database connection
connection = mysql.connector.connect(host="localhost", user="root", passwd="arthur0204455@", database="richieblurDB")
cursor = connection.cursor()
# Query for creating table
ArtistTableSql = """CREATE TABLE User_db(
Email varchar(200) NOT NULL PRIMARY KEY,
Password varchar(200) NOT NULL
)"""

cursor.execute(ArtistTableSql)
connection.close()



# CREATE TABLE `hostel` (
#   `HTLID` varchar(200) NOT NULL,
#   `HNAME` varchar(200) NOT NULL,
#   `ONAME` varchar(200) NOT NULL,
#   `LOCATION` varchar(200) NOT NULL,
#   `TEL` varchar(200) NOT NULL,
#   `PRICE` varchar(200) NOT NULL,
#   `QUANTITY` varchar(200) NOT NULL,
#   `ROOM` varchar(200) NOT NULL,
#    PRIMARY KEY (`STUDID`)
# );

# ArtistTableSql = """CREATE TABLE User_db(
# HTLID VARCHAR(3) PRIMARY KEY,
# HNAME  VARCHAR(50) NOT NULL,
# ONAME VARCHAR(50) NOT NULL,
# LOCATION VARCHAR(50) NOT NULL,
# TEL VARCHAR(13) NOT NULL,
# PRICE VARCHAR(20) NOT NULL,
# QUANTITY VARCHAR(20) NOT NULL,
# ROOM VARCHAR(20) NOT NULL
# )"""
