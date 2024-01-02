class Mailing:

    def __init__(self, to_addr, from_addr, cost, track):

        self.to_address = to_addr.getAddress()
        self.from_address = from_addr.getAddress()
        self.cost = int(cost)
        self.track = str(track)

    def getToAddr(self):
        return self.to_address

    def getFromAddr(self):
        return self.from_address

    def getCost(self):
        return self.cost

    def getTrack(self):
        return self.track
