def sayHello():
    s = raw_input('Enter the hello key:')
    print s # block belonging to the function

sayHello() # call the function


def printMax(a, b):
    if a > b:
        print a, 'is maximum'
    else:
        print b, 'is maximum'

printMax(3, 4) # directly give literal values
a = raw_input ('The 1st number is:')
b = raw_input ('The 2nd number is:')
printMax(a,b)

x = 5
y = 7

printMax(x, y) # give variables as arguments


def say(message, times = 2):
    print message * times

say('Hello ')
say('World', 5)
say(100,2)


def maximum(x, y):
    if x > y:
        return x
    else:
        return 

n = maximum(22,11)
print n

def someFunction():
    return
print someFunction()



def printMax(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)

    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3, 5)
print printMax. __doc__
