import sqlite3

def createDB():
    cnt = sqlite3.connect("mtzDB.db")

    cnt.execute('CREATE TABLE record (date INTEGER,title TEXT,tag TEXT,amount INTEGER)')
    cnt.commit()
    cnt.close()



if __name__ == '__main__':
    createDB()
    print("izDB.py")