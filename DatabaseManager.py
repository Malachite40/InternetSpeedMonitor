import sqlite3

class DatabaseManager():

    _conn = []
    _cursor = []
    def __init__(self):
        self._conn = sqlite3.connect("speedtest.db")
        self._cursor = self._conn.cursor()   
        self.createSpeedTestTable()
        return

    def createSpeedTestTable(self):
        self._cursor.execute("""CREATE TABLE IF NOT EXISTS speedtest(
            speedTestID INTEGER PRIMARY KEY AUTOINCREMENT,
            startTime TEXT,
            endTime TEXT,
            serverName TEXT,
            uploadSpeed REAL,
            downloadSpeed REAL,
            ping REAL,
            host TEXT
        )""")
        return
    
    def addSpeedTest(self, speedTest):
        self._cursor.execute("""INSERT INTO speedtest(
            startTime,
            endTime,
            serverName,
            uploadSpeed,
            downloadSpeed,
            ping,
            host
        ) VALUES (?,?,?,?,?,?,?)""", (speedTest._startTime, speedTest._endTime, speedTest._serverName, speedTest._uploadSpeed, speedTest._downloadSpeed, speedTest._ping, speedTest._host))
        self._conn.commit()
        return

    def printSpeedTest(self):
        self._cursor.execute("""SELECT * FROM speedtest""")
        print(self._cursor.fetchall())
        return

    def deleteAllSpeedTests(self):
        self._cursor.execute("""DELETE FROM speedtest""")
        self._conn.commit()
        return

    def deleteSpeedTest(self, sid):
        self._cursor.execute("DELETE FROM speedtest WHERE speedTestId = '"+str(sid)+"'")
        self._conn.commit()
        return