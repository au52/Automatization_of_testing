class Address:

    def __init__(self, index, city, street, house, flat):
        self.index = str(index)
        self.city = str(city)
        self.street = str(street)
        self.house = str(house)
        self.flat = str(flat)

    def getAddress(self):
        return (self.index + ', ' + self.city + ', ' +
                self.street + ', ' + self.house + ' - ' +
                self.flat)

#addr = Address('123321', 'Moscow', 'Tverskaya', '1', '52')
#print(addr.getAddress())