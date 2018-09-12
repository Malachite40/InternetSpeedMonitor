import matplotlib.pyplot as plt
import matplotlib
from DatabaseManager import DatabaseManager
import datetime
class VisualizeData():
    _db = {}
    def __init__(self):
        self._db = DatabaseManager()
        return
    def createScatterFromDatabase(self):
        # plt.style.use('fivethirtyeight')
        x = self.createListOfTimesSameDay()
        y = self.createListOfDownloadSpeeds()
        mpl = matplotlib        
        mpl.style.use('dark_background')
        
        # plt.xlabel('')
        plt.ylabel('Mb/s')
        plt.title('Internet Speed Monitor')
        # plt.legend()


        plt.scatter(x,y, color = "c", marker="+", s=1, edgecolors="w", cmap="b")
        plt.xticks(rotation=35)
        
        # custom stuff
        end = datetime.datetime.today().replace(year = 2018,month=1,day=1,hour=23,second=59,minute=59)
        start = datetime.datetime.today().replace(year = 2017,month=12,day=31,hour=23,second=59,minute=59)
        plt.xlim(start,end)  
        plt.grid(True, color='grey', linewidth=.25)
        
        
        plt.show()
    def createListOfTimesSameDay(self):
        stList = self._db.getAllSpeedTests()
        
        times = []
        for test in stList:
            # time = datetime.datetime.strptime(test._startTime, "%Y-%m-%d %H:%M:%S.%f")
            time = datetime.datetime.strptime(test._startTime[0:19], "%Y-%m-%d %H:%M:%S")
            newTime = time.replace(year = 2018, month = 1, day=1)
            times.append(newTime)

        return times
    def createListOfDownloadSpeeds(self):
        dsList = self._db.getAllSpeedTests()

        downloadSpeeds = []
        for ds in dsList:
            downloadSpeeds.append(round(ds._downloadSpeed/1000000, 2))
        return downloadSpeeds

_vd = VisualizeData()
_vd.createScatterFromDatabase()
# _vd.createListOfTimesSameDay()
# _vd.createListOfDownloadSpeeds()
