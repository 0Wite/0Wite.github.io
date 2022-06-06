hello=1

def test():
    global hello
    hello = 2
    print(hello)
test()
print(hello)
