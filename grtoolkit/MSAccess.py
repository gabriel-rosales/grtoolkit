import pyodbc

def SQLQuery(dbFile, SQL, fetch="all", commit=False):
    """commit False = SELECT, commit True = CREATE, UPDATE, DELETE"""
    databaseFile  = dbFile
    connectionString = "Driver={Microsoft Access Driver (*.mdb, *.accdb)};Dbq=%s" % databaseFile
    dbConnection   = pyodbc.connect(connectionString)
    cursor = dbConnection.cursor()
    cursor.execute(SQL)
    if commit:
        cursor.commit()
        cursor.close()
        dbConnection.close()
    else:
        if fetch == "all":
            rows = cursor.fetchall() 
        elif fetch == "one":
            rows = cursor.fetchone() 
        elif fetch == "val":
            rows = cursor.fetchval()
        else:
            assert fetch == "all" or fetch == "one" or fetch == "val", print("Incorrect fetch mode.")
        cursor.close()
        dbConnection.close()
        if rows:
            return rows

    #HOW TO CALL ON ROWS
    # for row in cursor:
    # print(row.user_id, row.user_name)

    # for row in rows:
    #     print(row.temp)