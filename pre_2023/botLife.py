import datetime
import time

lifeFile = "life.txt"
class Life:
    def __init__(self):
        self.__startingTime__ = datetime.datetime.now()
        self.__pulses__ = 900
        self.__lastHeartBeat__ = self.__startingTime__

    def __heartBeat__(self):
        self.__lastHeartBeat__ = datetime.datetime.now()

    def get_heartbeat(self):
        return  self.__lastHeartBeat__

    def get_infos(self):
        s = f"Pulses: 1 each {self.__pulses__} secondes" \
            f"\nLast heartbeat: {self.get_heartbeat().strftime('%m/%d/%Y, %H:%M:%S')}" \
            f"\nBirthDate: {self.__startingTime__.strftime('%m/%d/%Y, %H:%M:%S')}"
        return s

    def write_infos(self):
        self.__heartBeat__()
        f = open(lifeFile, "w")
        f.write(self.get_infos())
        f.close()

    def live_your_life(self):
        while (True):
            self.write_infos()
            time.sleep(self.__pulses__)


