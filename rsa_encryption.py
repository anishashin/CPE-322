import random

def calc_n(p, q):
    return p * q

def calc_phi(p, q):
    return (p - 1) * (q - 1)

def modexp(b, e, m):
    # returns b^e % m efficiently
    if m == 1:
        return 0
    result = 1
    b = b % m
    while e > 0:
        if e % 2 == 1:
            result = (result * b) % m
        e = e >> 1
        b = (b * b) % m
    return result

def RSA_enc(plaintext, key):
    # key should be a tuple (n, e)
    n = key[0]
    e = key[1]
    result = []
    for char in plaintext:
        result += [modexp(ord(char), e, n)]
    return result

def RSA_dec(ciphertext, key):
    # key should be a tuple (n, e)
    n = key[0]
    e = key[1]
    result = ""
    for elem in ciphertext:
        result += chr(modexp(elem, e, n))
    return result

def egcd(b, n):
    # runs the extended Euclidean algorithm on b and n
    # returns a triple (g, x, y) s.t. bx + ny = g = gcd(b, n)
    x = 1
    x1 = 0
    y = 0
    y1 = 1
    while n != 0:
        q = b // n
        b, n = n, b % n
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
    return b, x, y

def mulinv(e, n):
    # returns the multiplicative inverse of e in n
    g = egcd(e, n)[0]
    x = egcd(e, n)[1]
    if g == 1:
        return x % n

def checkprime(n, size):
    # determine if a number is prime
    if n % 2 == 0 or n % 3 == 0: return False
    i = 0

    # fermat primality test, complexity ~(log n)^4
    while i < size:
        if modexp(random.randint(1, n - 1), n - 1, n) != 1: return False
        i += 1

    # division primality test
    i = 5
    while i * i <= n:
        if n % i == 0: return False
        i += 2
        if n % i == 0: return False
        i += 4
    return True

def primegen(size):
    # generates a <size> digit prime
    if(size == 1): return random.choice([2, 3, 5, 7])
    lower = 10 ** (size - 1)
    upper = 10 ** size - 1
    p = random.randint(lower, upper)
    p -= (p % 6)
    p += 1
    if p < lower: p += 6
    elif p > upper: p -= 6
    q = p - 2
    while p < upper or q > lower:
        if p < upper:
            if checkprime(p, size): return p
            p += 4
        if q > lower:
            if checkprime(q, size): return q
            q -= 4
        if p < upper:
            if checkprime(p, size): return p
            p += 2
        if q > lower:
            if checkprime(q, size): return q
            q -= 2

def keygen(size):
    # generate a random public/private key pair
    # size is the digits in the rsa modulus, approximately. must be even, >2
    # return a tuple of tuples, [[n, e], [n, d]]
    assert(size % 2 == 0 and size > 2)
    p = primegen(size/2)
    q = primegen(size/2)
    while q == p:
        q = primegen(size/2)
    n = calc_n(p, q)
    phi = calc_phi(p, q)
    e = random.randint(2, phi - 1)
    while egcd(e, phi)[0] != 1:
        e = random.randint(2, phi - 1)
    d = mulinv(e, phi)
    return [[n, e], [n, d]]

def keytest(text, size):
    keypair = keygen(size)
    
    print("Public key:",keypair[0])
    print("Private key:",keypair[1])
    
    ciphertext = RSA_enc(text,keypair[0])
    plaintext  = RSA_dec(ciphertext,keypair[1])

    print("Original message:",text)
    print("Encrypted message:",ciphertext)
    print("Decrypted message:",plaintext)

if __name__ == "__main__":
    keytest("Hello, World!", 8)
