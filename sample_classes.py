class simple_arithmetic :
    '''this argument takes two arguments at intialization. 
    There are four methods that will return simple arithmetic 
    operations'''
    
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        return
        pass
    def add(self) :
        return self.arg1+self.arg2
        pass
    def sub(self) :
        return self.arg1-self.arg2
        pass
    def div(self) :
        return float(self.arg1)/self.arg2
        pass
    def mul(self) :
        return float(self.arg1)*self.arg2
        pass
    
        
