#!/usr/bin/python

"""
Four FizzBuzz Solutions    

"""

def generator():
    number = 0
    while 1:
        yield number
        number = number + 1

#    numbers = range(1,101)
#    for num in numbers:
#        yield num

def fizzbuzz_1():
    for number in range(1,101):
        if number % 3 == 0:
            if number % 5 == 0:
                print "fizzbuzz"
            else:
                print "fizz"
        elif number % 5 == 0:
            print "buzz"
        else:
            print number

def fizzbuzz_2():
    for number in range(1,101):
        print "Fizz"*(not number%3) + "Buzz"*(not number%5) or number
        
def fizzbuzz_3():
    print '\n'.join( "Fizz"*(not number%3) + "Buzz"*(not number%5) or str(number ) for number in range(1,101))

def fizzbuzz_4():
    fizzbuzz = ["Fizz"*(not number%3)+"Buzz"*(not number%5) or number for number in range(1,101)]

    for item in fizzbuzz:
        print str(item)

"""
Infinite FizzBuzz
"""
def fizzbuzz_5():
    for number in generator():
        print "Fizz"*(not number%3) + "Buzz"*(not number%5) or number

if __name__ == "__main__":
    fizzbuzz_1()
    fizzbuzz_2()
    fizzbuzz_3()
    fizzbuzz_4()
    fizzbuzz_5()