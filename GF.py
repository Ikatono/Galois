import math

#defines the field itself
#responsible for creating elements and performing operations
#all elements contain a pointer to the field that created them
#elements from different fields can't interact, even if they're equivalent

class GF:
    def __init__(self, *args):
        
        def getcharacteristic(a):
            for i in (2, 3, 5, 7, 11, 13, 17, 19, 23):
                if a%i == 0:
                    b = math.log(a, i)
                    if not math.isclose(b, int(b+1e-6), abs_tol=1e-6) :
                        raise ValueError('%i is not a prime power' % a)
                    return i, int(b+1e-6)
        
        if len(args) == 1:
            p, n = getcharacteristic(args[0])
        elif len(args) > 2:
            raise TypeError('too many arguments')
        else:
            p, n = args
        self.characteristic = p
        self.order = p**n
        self.degree = n
        file = open('gf' + str(p) + '.txt', 'r')
        pol = file.readlines()[n-2]
        file.close()
        #removes newline then splits into individual terms
        pol = pol[:-1].split(',')
        #(exponent, coefficient) for each term of the polynomial
        self.poly = []
        for i in pol:
            if '(' in i:
                a, b = i.split('(')
                #constant term isn't given an exponent in the txt file
                a = a if a else 0
                self.poly.append((int(a), int(b[:-1])))
            else:
                self.poly.append((int(i),1))
        if p == 2:
            self.poly.append((0,1))
        
    
    #creates a new element with the given value
    def new(val):
        
        #splits integers into their binary components
        def bisplit(bal):
            pass
        
        if isisntance(val, int):
            if self.characteristic != 2:
                raise TypeError('integer definition of field elements is only allowed in fields of characteristic 2')
        #covers the case that the value is an iterable of individual terms
        #first term is for exponent zero, etc.
        #accepts integers or strings
        else:
            pol = [0] * self.degree
            for i in range(len(val)):
                if isinstance(val[i], int):
                    pol[i] = val[i]
                else:
                    #TODO for christs sake refactor this
                    try:
                        pol[i] = val[i]
                    except ValueError:
                        try:
                            pol[i] = int(val[i])
                        except ValueError:
                            a = ord(val[i].tolower())
                            if 97 <= a <= 122:
                                pol[i] = a - 87
                            else:
                                raise ValueError('polynomial coefficient is uninterprettable')
            
                    
            

class GFElement:
    def __init_(self, value, field):
        self.field = field