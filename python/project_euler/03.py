

"""
Problem 3
=========
The prime factors of 13195 are 5, 7, 13 and 29

What is the largest prime factor of the number 600851475143 ?

"""

def is_prime(number):
    """
    Utility function to determine whether a number is prime.
    """
    number *= 1.0
    for divisor in range(2, int(number**0.5)+1):
        if number/divisor == int(number/divisor):
            return False
    return True

def calculate_prime_factors(target, factor):
    """
    Recursive function that returns a list of prime factors of target
    """
    factors = []
    while (target % factor != 0):
        factor = factor + 1

    factors.append(factor)

    if target > factor:
        factors.extend(calculate_prime_factors(target / factor, factor))

    return factors

if __name__ == "__main__":
    prime_factors = calculate_prime_factors(600851475143, 2)

    print ', '.join(str(factor) for factor in prime_factors)

    total = 1
    for factor in prime_factors:
        total *= factor
    
    print str(total)
    print max(prime_factors)

        
        
        
    
    
    