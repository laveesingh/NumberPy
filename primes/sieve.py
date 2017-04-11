'''
This file contains segmented sieve of eratosthenes that generates all the prime
numbers given in a range.
'''


def sieve(start, end, bool_array=False):
    '''
    This function takes a range and produces all the prime numbers in that
    range.
    Usage:
    >>> sieve(start, end, bool_array=False)
    parameters:
        start: starting number
        end: ending number
        bool_array: If it's true only the generated boolean array for that
        range is returned instead of the actual primes. First index in
        bool_array represents start number and 1 repsents if number is prime
        0 otherwise.
    '''
    end += 1  # end is excluded like all the time
    # First generate primes upto sqrt(end)
    sqrt_end = int(end**0.5 + 1.5)
    isprime = [1] * sqrt_end
    isprime[0] = isprime[1] = 0
    for i in xrange(4, sqrt_end, 2):
        isprime[i] = 0
    for i in xrange(3, int(sqrt_end**0.5 + 1.5), 2):
        if isprime[i]:
            for j in xrange(i*i, sqrt_end, 2*i):
                isprime[j] = 0
    primes = [i for i, s in enumerate(isprime) if s]
    # Generating primes upto sqrt(end) ends here

    # Using above primes generate prime in actual range
    isprime = [1] * (end - start)
    if start == 1:
        isprime[0] = 0
    for prime in primes:
        st = (start / prime) * prime + prime
        if start % prime == 0:
            st = start
        if st == prime:
            st += prime
        for i in xrange(st, end, prime):
            isprime[i-start] = 0
    final_primes = [i+start for i, s in enumerate(isprime) if s]
    if bool_array:
        return isprime
    return final_primes
