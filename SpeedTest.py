

class SpeedTest():

    _speedTestId = []
    _startTime = []
    _endTime = []
    _serverName = []
    _uploadSpeed = []
    _downloadSpeed = []
    _ping = []
    _host = []
    def __init__(self, speedTestId, startTime, endTime, serverName, uploadSpeed, downloadSpeed, ping, host):
        self._speedTestId = speedTestId
        self._startTime = startTime
        self._endTime = endTime
        self._serverName = serverName
        self._uploadSpeed = uploadSpeed
        self._downloadSpeed = downloadSpeed
        self._ping = ping
        self._host = host
        return

