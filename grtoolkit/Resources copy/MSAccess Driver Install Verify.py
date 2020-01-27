def SampleTest():
    dataFile = "sample.accdb"
    databaseFile  = os.getcwd() + "\\" + dataFile
    connectionString = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s" % databaseFile
    dbConnection = pyodbc.connect(connectionString)
    cursor = dbConnection.cursor()
    cursor.execute("select top 5 * from JobInfo")
    cursor.execute("select * from JobInfo")
    rows = cursor.fetchall()
    for row in rows:
        print(row.JOBNO)

def readSQL(dbFile, SQL):
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
    databaseFile  = dbFile
    connectionString = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s" % databaseFile
    dbConnection   = pyodbc.connect(connectionString)
    cursor = dbConnection.cursor()
    cursor.execute(SQL)
    cursor.commit()
    cursor.close()
    dbConnection.close()
    
def RefreshTemplate(dbFile):
    commitSQL(dbFile, "DELETE FROM Variables WHERE Name Like 'Path%'")
    commitSQL(dbFile, "DELETE FROM Variables WHERE Name='pts'")
    commitSQL(dbFile, "DELETE FROM Variables WHERE Name='PATHS_TOTAL'")


try:
    import os
    import pyodbc
    import time

    #The easiest way to check if one of the Microsoft Access ODBC drivers is available to your Python environment (on Windows) is to do
    #If you see an empty list then you are running 64-bit Python and you need to install the 64-bit version of the "ACE" driver. If you only see ['Microsoft Access Driver (*.mdb)'] and you need to work with an .accdb file then you need to install the 32-bit version of the "ACE" driver.

    driver = [x for x in pyodbc.drivers() if x.startswith('Microsoft Access Driver')]
    print(driver)

    if not driver:
        print("Driver list is empty. You need the 64 bit driver.")
        time.sleep(1)
    else:
        if 'Microsoft Access Driver (*.mdb, *.accdb)' in driver:
            print("Driver installed.")
            SampleTest()
            time.sleep(1)
        elif 'Microsoft Access Driver (*.mdb)' in driver:
            print("You need the 32 bit driver")
            time.sleep(1)

except:
    time.sleep(2)