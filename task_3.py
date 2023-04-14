class funcmapper:

    def __init__(self):
        print("Within init")
        self.funcdict ={}

    def route(self,pattern):
        def wrap(func):
            print("Within wrap")
            self.funcdict[pattern] = func
            return func
        return wrap
    
    def call_by_route(self,name,*args,**kwargs):
        print("Within call_by_route")
        if name in self.funcdict:
            self.funcdict[name](*args,**kwargs)

app = funcmapper()  

@app.route('/')
def hello():
    print("Hello World")

app.call_by_route('/')
print(hello)