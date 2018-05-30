'''Some example classes we can use in the notebook to test how importing works '''


class OperateOnTwoNumbers :
    def __init__(self, num1, num2, operation='division'):
        '''We initialize this class object with two numbers.  These are two attributes in the class'''
        self.num1 = num1
        self.num2 = num2
        # Example kwarg in intialization below.
        self.operation=operation
        
        
    def divide_me(self) :
        ''' This method divides num1 by num2'''
        return self.num1/self.num2
    
    def multiply_me(self) :
        ''' This method divides num1 by num2'''
        return self.num1*self.num2
    
    def add_me(self) :
        return self.num1 + self.num2
    
    def subtract_me(self) :
        return self.num1 - self.num2
    
    def execute_operation(self) :
        # Example control statement (if and elif)
        if self.operation == 'division' :
            return self.divide_me()
        elif self.operation == 'multiplication' :
            return self.multiply_me()
        elif self.operation == 'addition' :
            return self.add_me()
        elif self.operation == 'subtraction' :
            return self.subtract_me()
        else :
            print "Invalid Operation"
            
