'''program using *args -> collects positional arguments'''
def total(*args):
    total = 0

    for i in args:
        total+=i

    return total
print(total(10, 20, 30))
print(total(5, 10, 15, 20, 25))

def multiply(*args):
    product = 1

    for i in args:
        product*=i

    return product
print(multiply(2, 3, 4))