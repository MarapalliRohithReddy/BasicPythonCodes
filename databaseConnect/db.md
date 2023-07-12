# databaseConnect

## Function to Connect python to mySQL Database
```
mysqlDataSend(hostAddress, userName, dbPassword, dbName,dbPort, values)
```

**_parameter1:_**  IP/Domain name where your DB is residing <br />
**_parameter2:_** Database Username <br />
**_parameter3:_**  Database Password <br />
**_parameter4:_**  Database Name where your table is residing to store data <br />
**_parameter5:_**  Port Number where Database is accessible <br />
**_parameter6:_**  Data to be stored <br />

```
sql = "INSERT INTO **_DummyTable_** (**_dev_name_**, **_voltage_**,**_temperature_**) VALUES (%s, %s,%s)"
myCursor.execute(sql, values)
myDatabase.commit()
```

In above line **_DummyTable_** is name of the Table where data to stored so you need to be replacing that with your table name <br />
**_dev_name_**, **_voltage_**,**_temperature_** are the column names which you requre it can be added according to application. Accordingly Values will be inserted from the VALUES part. <br />
