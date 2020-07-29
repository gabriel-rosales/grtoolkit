import sqlite3
#server-less database

class db():
    def __init__(self,path):
        self.path = path
        self.connect = sqlite3.connect(self.path)

    def read(self, query):
        # if cursor:
        #     <tuple> = cursor.fetchone()  # First row.
        #     <list>  = cursor.fetchall()  # Remaining rows.
        db = self.connect
        return db.execute(query)

    def write(self,query):
        db = self.connect
        db.execute(query)
        db.commit()
    

