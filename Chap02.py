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

# stop-start is the total number of elements for step=1
# considering step, we need add step-1 to get the last element by using // which is floor integer

#R2.17

class Goat(object):
    def __init__(self, tail):
        super().__init__()
        self._tail = tail
    
    def __milk()
        return
    
    def __jump()
        return
    
#R2.18

class Progression():
    def __init__(self, start=0):
        self._current = start
    def _advance(self):
        self._current += 1
    def __next__(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    def __iter__(self):
        return self
    def print_progression(self, n):
        print (' '.join(str(next(self)) for j in range(n)))

class FibonacciProgression(Progression):
    def __init__(self, first=0, second=1):
        super().__init__(first)
        self._prev = second - first
    
    def _advance(self):
        self._prev, self._current = self._current, self._prev + self._current

    def print(self, n):
        m = 0
        for j in range(n):
            m = next(self)
        print (m)

f = FibonacciProgression(2,2)    
f.print(8)

#R2.19

max(0, (stop - start + step - 1) // step) = 2**63 / 2**7 = 2**56

#R2.20

# If behaviour changes in A without D knowing (ex. different teams or people working on it), 
# it can be very difficult to troubleshoot the problems


# You also have a larger chance of namespace conflicts that you aren't aware of 
# (ex. C overrides a function from B that you don't know about)

#R2.21

# If any of the classes change, it will mess up the entire Z subclass

#R2.22

from abc import ABCMeta, abstractmethod

class Sequence(metaclass = ABCMeta):
    @abstractmethod
    def __len__(self):
        pass
        
    @abstractmethod
    def __getitem__(self, index):
        pass
        
    def __contains__(self, val):
        for i in range(len(self)):
            if self[j] == val: return True
        return False #if it wasn't found
    
    def count(self, val):
        k = 0
        for j in range(len(self)):
            if self[j] == val: k+=1
        return k

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        else:
            for i in range(len(self)):
                if self[i] != other[i]: return False
        return True
    
#R2.23    

    def __lt__(self, other):
        for i in range(min(len(self), len(other))):
            if self[i] < other[i]: return True
            elif self[i] > other[i]: return False
        
        if len(self) < len(other): return True
        else: return False
        
#R2.24

# variables: account, book_list
# methods: purchase_book, view_purchase_list, read_book

#R2.25

# check R2.14

#R2.26

class SequenceIterator():
    def __init__(self, sequence):
        self._seq = sequence
        self._k = -1
        
    def __next__(self):
        self._k += 1
        if self._k < len(self._seq):
            return (self._seq[self._k])
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self

class ReversedSequenceIterator():
    def __init__(self, sequence):
        self._seq = sequence
        self._k = len(self._seq)
        
    def __next__(self):
        self._k -= 1
        if self._k >= 0:
            return (self._seq[self._k])
        else:
            raise StopIteration()
    
    def __iter__(self):
        return self        

print([x for x in ReversedSequenceIterator([1,2,3,4,5,6,7,8])])

#R2.27

class Range():
    def __init__(self, start, stop = None, step = 1):
        if step == 0: raise ValueError('step cannot be 0')
        if stop is None:    #This is more robust than if stop == None, since it's ambiguous sometimes (ex. custom classes)
            start, stop = 0, start
            
        self._length = max(0, (stop-start + step -1)//step)
        
        self._start = start
        self._step = step
        
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k<0:
            k+= len(self)
        if not 0<=k<self._length:
            raise IndexError('index out of range')
            
        return self._start + k*self._step

    def __contains__(self, k):
        factor, reminder = divmod(k-self._start, self._step)
        if reminder == 0:
            if factor >= 0 and factor < len(self): return True
        
        return False

r = Range(1,100,2)
print (len(r), r[3], 4 in r, 5 in r)

r = Range(-100, step = -1)
print (len(r), r[101], 4 in r, -5 in r)

#R2.28

class PredatoryCreditCard(CreditCard):
    MAX_CHARGES = 10
    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._num_charges = 0
        
    def charge(self, price):
        success = super().charge(price)
        if not success:
            self._balance += 5
        else:
            self._num_charges += 1
            if self._num_charges > self.MAX_CHARGES:
                self._balance += 1
            
        return success
    
    def process_month(self):
        if self._balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            self._balance *= monthly_factor
        self._num_charges = 0 #reset the counter at the beginning of each month

#R2.29

class CreditCardLateFee(PredatoryCreditCard):
    MINIMUM_PAYMENT_PERCENTAGE = 0.1
    LATE_FEE = 10

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._minimum_payment = 0

    def process_month(self):
        super().process_month()
        if self._minimum_payment > 0:
           self._balance += self.LATE_FEE 
        if self._balance > 0:
            self._minimum_payment = self._balance * self.MINIMUM_PAYMENT_PERCENTAGE

    def make_payment(self, value):
        if super().make_payment(value):
            self._minimum_payment = max(0, self._minimum_payment - value)

#R2.30

class PredatoryCreditCard2(CreditCard):
    MAX_CHARGES = 10

    def __init__(self, customer, bank, acnt, limit, apr):
        super().__init__(customer, bank, acnt, limit)
        self._apr = apr
        self._num_charges = 0
        
    def charge(self, price):
        success = super().charge(price)
        if not success:
            super()._set_balance(super()._get_balance + 5)
        else:
            self._num_charges += 1
            if self._num_charges > self.MAX_CHARGES:
                super()._set_balance(super()._get_balance + 1)
            
        return success
    
    def process_month(self):
        if super()._get_balance > 0:
            monthly_factor = pow(1+self._apr, 1/12)
            super()._set_balance(super()._get_balance * monthly_factor)
        self._num_charges = 0 #reset the counter at the beginning of each month
        
#R2.31        
