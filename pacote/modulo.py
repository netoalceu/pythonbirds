

def soma(*args):
    total=0
    for n in args:
        total += n
    return total

print (__name__)

if __name__ == '__main__':
    print(soma())
    print(soma(1))
    print(soma(1,2))
    print(soma(1,2,3))
    print(soma(1,2,3,4))
