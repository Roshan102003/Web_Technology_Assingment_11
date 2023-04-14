def call_counter(func):
    print("Within Call Counter")
    def wrap(*args, **kwargs):
        print("Incrementing wrap counter")
        wrap.counter +=1
        return func(*args,**kwargs)
    print("Initializing wrap counter")
    wrap.counter = 0
    return wrap

@call_counter
def fib(n):
    print("Within fib function")
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
# print("Calling call_counter")
# fib = call_counter(fib)

for i in range(3):
    print(f"Fib counter value before calling fib{i} is {fib.counter}")
    print("Within Loop", i)
    print(fib(i), fib.counter)
    print("Resetting fib counter")
    fib.counter = 0