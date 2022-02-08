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

    def charge(self, price):
        try:
            price = float(price) 
        except:
            print ('Invalid price')
            return False       
        if price+self._balance >self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        try:
            amount = float(amount) 
        except:
            print ('Invalid payment')
            return False 
        self._balance -= amount
        return True

#R2.6

    def make_payment(self, amount):
        try:
            amount = float(amount) 
        except:
            print ('Invalid payment')
            return False 
        
        if amount < 0:
            raise ValueError('payment cannot be negative')
        else:
            self._balance -= amount
            return True

#R2.7

class CreditCardBalance(CreditCard):
    def __init__(self, customer, bank, acnt, limit, balance = 0):
        super().__init__(customer, bank, acnt, limit)

        self._balance = balance

#R2.8

#The 3rd card California Finance

#R2.9

    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range (len(self)):
            result[j] = self[j] - other[j]
        return result

#R2.10

class VectorwNeg(Vector):
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = -self[i]
        return result        

v1 = VectorwNeg(5)
v2 = VectorwNeg(5)

for i in range(5):
    v1[i] = 8
    v2[i] = i

print(v1,v2)
print(v1-v2)    
print(v1,-v2)

#R2.11

    def __radd__(self, other):
        if len(self)!=len(other):
            raise ValueError('Dimensions must match')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

#R2.12

    def __mul__(self, factor):
        try:
            factor = float(factor)
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * factor
            return result
        except:
            print('Invalid factor')
            return False

#R2.13

    def __rmul__(self, factor):
        try:
            factor = float(factor)
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * factor
            return result
        except:
            print('Invalid factor')
            return False

#R2.14

    def __mul__(self, other):
        try:
            if len(self) == len(other):
                result = 0
                for j in range(len(self)):
                    result += self[j] * other[j]
                return result
        except:
            try:
                other = float(other)
                result = Vector(len(self))
                for j in range(len(self)):
                    result[j] = self[j] * other
                return result
            except:
                print('Invalid factor')
                return False

#R2.15

class VectorD(Vector):
    def __init__(self, d):
        if isinstance(d, int):
            super().__init__(d)
        else:
            self._coords = d

#R2.16            

