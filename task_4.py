class MyClass:
    def __init__(self,name):
        self.ivar1 = name
        print("Inside init")

    def __call__(self,x,y):
        print("Inside Call")
        print("Hello: {0}".format(self.ivar1))
        sum = x+y
        print("The sum is {0}".format(sum))
        return sum
    
foo = MyClass('brad')

foo(2,9)