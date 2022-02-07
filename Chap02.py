#R2.1

#auto-drive software
#heartbeat monitor software
#fall down detector

#R2.2

#a software which will adjust the produce based on selling markets

#R2.3

#search keyword
#input keyword
#compare keyword with every word in the opening file
#highlight the matched word in the file

#R2.4

class Flower:
    def __init__(self, name = None, petal = None, price = None):
        self._name = self._petal = self._price = None

        self.set_name(name)
        self.set_petal(petal)
        self.set_price(price)
    
    def set_name(self, name):
        try:
            self._name  = str(name)
        except:
            print('Flower name must be a string')

    def set_petal(self, petal):
        try:
            if petal <= 0: raise ValueError
            self._petal = int(petal)
        except:
            print('Flower petal must be a positive integer')

    def set_price(self, price):
        try:
            self._price  = float(price)
        except:
            print('Flower price invalid')
    
    def get_name(self):
        return(self._name)
    
    def get_petal(self):
        return(self._petal)
    
    def get_price(self):
        return(self._price)

rose = Flower('Rose',20,88)
print(rose.get_name(), rose.get_petal(), rose.get_price())

#R2.5

