from math import log

#defines the field itself
#responsible for creating elements and performing operations
#all elements contain a pointer to the field that created them
#elements from different fields can't interact, even if they're equivalent

class GF:
    def __init__(self, *args):
        
        def characteristic(a):
            if a%2 == 0:
                b = log(a, 2)
                if b != int(b):
                    raise ValueError('%i is not a prime power' % a)
                return 2, int(b)
            i = 3
            while i <= 23:
                if a%i == 0:
                    b = log(a, i)
                    if b != int(b):
                        raise ValueError('%i is not a prime power' % a)
                    return i, int(b)
                i += 2
        
        if len(args) == 1:
            p, n = characteristic(args[0])
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
        pol = pol.split(',')
        #integer coefficients of defining polynomial
        #index is the exponent 
        self.poly = [None]*n + [1]
        if p == 2:
            self.poly[0] = 1
        for i in pol