def announce(f):
    def wrapper():
        print("Function")
        f()
        print("Done function")
    return wrapper
def announce1(f):
    def wrapper1():
        print("It'll be string")
        f()
        print("Done with string")
    return wrapper1

@announce
def hello():
    print("Assalomu Aleykum, Xush Kelibsizlar")


hello()

@announce1
def salom():
    print("Nima hizmat kerak")

salom()