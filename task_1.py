def call_counter(func):
    print("Within Call Counter")
    def wrap(*args, **kwargs):
        print("Within Wrap")
        wrap.counter +=1
        return func(*args,**kwargs)
    wrap.counter = 0
    return wrap

def fib(n):
    print("Within fib")
    if n<=1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
fib = call_counter(fib)
print(fib)

for i in range(20):
    print("Within Loop")
    print(fib(i), fib.counter)
    fib.counter = 0