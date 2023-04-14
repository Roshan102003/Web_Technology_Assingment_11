class ccc:
    def __init__(self,start_val,current_time):
        print("Within init")
        self.counter = start_val
        self.define_time = current_time

    def __call__(self,func):
        def wrap(*args, **kwargs):
            print("Within wrap")
            self.counter += 1
            print(*args)
            print(**kwargs)
            return func(*args,**kwargs)
        wrap.wrapper = self
        return wrap
    
import time

@ccc(0,time.time())
def fib(n):
    print("Within fib")
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(2))
print(fib.wrapper.counter)
print(fib.wrapper.define_time)