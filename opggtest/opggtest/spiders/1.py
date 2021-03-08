class Machine:
    # implementation omitted
    pass

class Calculator(Machine):
    # implementation omitted
    pass

class FourFunctionCalculator(Calculator):
    # implementation omitted
    pass
    
if __name__ == '__main__':
    m = Machine()
    c = Calculator()
    f = FourFunctionCalculator()
    


    print(type(f) == type(c))

    isinstance(m, Calculator)

    type(m) == type(f)

    isinstance(f, Calculator)

    isinstance(c, Machine)

    print(isinstance(f, Machine))

    type(m) == type(c)