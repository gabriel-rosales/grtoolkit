import pyodbc

def readSQL(dbFile, SQL):
    """SELECT"""
    databaseFile  = dbFile
    connectionString = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s" % databaseFile
    dbConnection   = pyodbc.connect(connectionString)
    cursor = dbConnection.cursor()
    cursor.execute(SQL)
    rows = cursor.fetchall()
    cursor.close()
    dbConnection.close()
    if rows:
        return rows

def commitSQL(dbFile, SQL):
    """CREATE, UPDATE, DELETE"""
    databaseFile  = dbFile
    connectionString = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s" % databaseFile
    dbConnection   = pyodbc.connect(connectionString)
    cursor = dbConnection.cursor()
    cursor.execute(SQL)
    cursor.commit()
    cursor.close()
    dbConnection.close()