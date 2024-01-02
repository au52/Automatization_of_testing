class Smartphone:

    def __init__(self, Marka, Model, Number):
        self.marka = str(Marka)
        self.model = str(Model)
        self.number = str(Number)

    def getSmartAttr(self):
        return self.marka + ' - ' + self.model + '. ' + self.number

smartphone0 = Smartphone('Ulefone', 'ArmorX5', '+79998887766')
print(smartphone0.getSmartAttr())