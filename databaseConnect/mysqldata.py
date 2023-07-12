import mysql.connector

hostAddress="dbIpaddress/domain" #Input your IP/Domain name where your DB is residing
userName="Database_UserName" #Input your DB user name
dbPassword= "Database_UserPassword" #Input your DB Password
dbName="Database_Name" #Input your DB Name
dbPort = 1234 #Input your DB Port Number
values = ("Dev123",20,45) #(x,y,z.....) add your values according to the values


def mysqlDataSend(hostAddress, userName, dbPassword, dbName,dbPort, values):
  try:
      myDatabase = mysql.connector.connect(
      host=hostAddress,
      user=userName,
      password= dbPassword,
      database=dbName,
      port = dbPort
      )
      myCursor = myDatabase.cursor()
      sql = "INSERT INTO DummyTable (dev_name, voltage,temperature) VALUES (%s, %s,%s)"
      myCursor.execute(sql, values)
      myDatabase.commit()
      print("[INFO] ",myCursor.rowcount, "record inserted.")
      myDatabase.close()
  except Exception as errors:
    print("[Error] Error occured :", errors)


mysqlDataSend(hostAddress, userName, dbPassword, dbName,dbPort, values)
  