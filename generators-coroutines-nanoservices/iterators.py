def myfor(data):

    i = iter(data)

    while True:

        try:
            print(next(i))
        except StopIteration:
            break

#   Assume you want to make instances of your class iterable
        
#   Requirements
        
#   When iter() is invoked on the object, should return an iterator
        
#   This means that we will need to get an object on which we can invoke next()
#   and get either the next object or the StopIteration exception

#   Easiest way to do this: define both __iter__ and __next__ methods
#
        
#   An object is considered iterable if it has the __iter__ dunder method defined for it
#   An object is considered an iterator if it has the __iter__ as well as the __next__ dunder methods declared
        
#   In an iterator, there is no previous or reset - all you can do is move forward, 
#   one at a time until you get to the end

class myIter(object):

    def __init__(self, data):

        self.data = data 
        self.index = 0 
    
    def __iter__(self):
        return self
    
    def __next__(self):

        if self.index >= len(self.data):

            raise StopIteration
        
        value = self.data[self.index]

        self.index += 1

        return value
        

class myIterRev(object):

    def __init__(self, data):

        self.data = data 
        self.index = len(data) - 1
    
    def __iter__(self):

        return self
    
    def __next__(self):

        if self.index < 0:

            raise StopIteration
        
        value = self.data[self.index]

        self.index -= 1

        return value
    

m = myIterRev("abc")

for letter in m:

    print(letter)
