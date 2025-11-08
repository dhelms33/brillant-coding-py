class DifferentialEquations:
    def __init__(self, derivative1, derivative2):
        self.derivative1 = derivative1
        self.derivative2 = derivative2
    
    def basic_diffeq_d1(self, derivative1,derivative2):
        try:
            return(f"dy/g(y) = f(x)dx")
        except ValueError as e:
            return("This is not a diff eq!")
        
    def first_order_derivatives(self, function1, exponent):
        try:
            return(f"{function1} **({exponent-1})/({exponent-1}))"
        except ValueError as e:
            return("Please input a first order derivative")
            