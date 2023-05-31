class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.traveltimes = {} 

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName , t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstation , starttime = self.checkin[id]
        traveltime = t - starttime
        key = (startstation , stationName)
        if key in self.traveltimes:
            totaltime , count = self.traveltimes[key]
            self.traveltimes[key] = (totaltime + traveltime , count +1)
        else:
            self.traveltimes[key] = (traveltime , 1)
        del self.checkin[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation , endStation)
        totaltime , count = self.traveltimes[key]
        return totaltime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)