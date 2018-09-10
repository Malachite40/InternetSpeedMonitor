import speedtest
from time import sleep
from DatabaseManager import DatabaseManager
from SpeedTest import SpeedTest
import datetime

_intervalSpeed = 600 #10 minutes
_intervals = 144

s = speedtest.Speedtest()
info = s.get_best_server()

_db = DatabaseManager()
# _db.printSpeedTest()

x = 0
while(True):
    _startTime = datetime.datetime.today()
    _downloadSpeed = s.download()
    _uploadSpeed = s.upload()
    _ping = info['latency']
    _name = info['name']
    _host = info['host']
    _endTime = datetime.datetime.today()
    _speedTest = SpeedTest(1,_startTime,_endTime,_name,_uploadSpeed,_downloadSpeed,_ping,_host)
    _db.addSpeedTest(_speedTest)
    print("Successfully added: " + str(x))
    _uploadSpeed = round(_uploadSpeed / 1000000, 2)
    _downloadSpeed = round(_downloadSpeed / 1000000, 2)
    print("Upload: " + str(_uploadSpeed) +  "/Mbps -- Download: " + str(_downloadSpeed) +"/Mbps -- "+ str(_startTime))
    x += 1
    sleep(_intervalSpeed)
