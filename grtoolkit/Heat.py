import pyodbc, os, sys
from grtoolkit.MSAccess import SQLQuery

PropertyTables = os.path.dirname(sys.argv[0]) + "\\PropertyTables.accdb"
PT = PropertyTables

def Farenheit(Celcius):
    return 9.0/5.0*Celcius+32.0

def Celcius(Farenheit):
    return (Farenheit-32.0)/9.0*5.0
    
def tblCode(shortcutName):
    return SQLQuery(PT, f"Select tblName from A00_VBA_Table_References where sqlFromVal='{shortcutName}'", fetch="val")

def SQLPT(SQL, fetch="all"):
    return SQLQuery(PT, SQL, fetch)


# sample = SQLPT(f"Select temp from {tblCode('water_t')} where temp>55")

