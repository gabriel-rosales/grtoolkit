import pyodbc, os, sys
from MSAccess import readSQL, commitSQL

PropertyTables = os.path.dirname(sys.argv[0]) + "\\PropertyTables.accdb"
PT = PropertyTables

def Farenheit(Celcius):
    return 9.0/5.0*Celcius+32.0

def Celcius(Farenheit):
    return (Farenheit-32.0)/9.0*5.0

def tblCode(shortcutName):
    return readSQL(PT, f"Select tblName from A00_VBA_Table_References where sqlFromVal='{shortcutName}'")[0][0]


# print(tblCode("water_t"))
print(readSQL(PT, f"Select temp from {tblCode('water_t')} where temp>55"))


# def read_db():
#     "Select all from A04_Saturated_Water_Temperature"

# print(readSQL(os.path.dirname(sys.argv[0]) + "\\PropertyTables.accdb", "Select * from A04_Saturated_Water_Temperature"))