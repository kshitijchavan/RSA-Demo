# Functions

# Checks if a given number is prime
def is_prime(n):
    print("Prime check for " + str(n) + " started")
    if n <= 1:
        return False

    for i in range(2, int((n / 2) + 1)):
        if (n % i) == 0:
            return False

    print("Prime check for " + str(n) + " complete")

    return True


# Checks if given two numbers are co-prime
def is_co_prime(p, q):
    print("Co-prime check for " + str(p) + "," + str(q))
    if p == q:
        return False

    if is_prime(p) and is_prime(q):

        print("Co-prime check for " + str(p) + "," + str(q) + " started")
        if q > p:
            print("Switching p and q")
            temp = q
            q = p
            p = temp

        r = -1

        while r != 0:
            r = p % q
            print(r)
            p = q
            q = r

        if p == 1:
            print("Co-prime check complete")
            return True
        else:
            return False

    else:
        print("p or q are not prime")
        return False


# Checks for co_prime only
def is_co_prime_toi(p, q):
    if p == q:
        return False
    print("Co-prime check for " + str(p) + "," + str(q) + " started")
    if q > p:
        print("Switching p and q")
        temp = q
        q = p
        p = temp

    r = -1

    while r != 0:
        r = p % q
        print("Reminder = "+str(r))
        p = q
        q = r

    if p == 1:
        print("Co-prime check complete")
        return True
    else:
        return False


# Calculates smallest co_prime number of toitent
def calculate_e(toi):
    """
    e = 2
    gcd = -1
    while gcd != 1:
        temp = e
        while toi != temp:
            if toi > temp:
                toi = toi - temp
            else:
                temp = temp - toi
        e += 1
        gcd = temp
        print(gcd)
    return e
    """
    e = 2
    if 1 < e < toi:
        while not (is_co_prime_toi(e, toi)):
            e += 1
    else:
        print("No co_prime found for toitent Q(" + toi + ")")
    return e


def calculate_d(e, toi):
    # e*d = 1 mod toi // 1 < d < Q
    print(toi + 1)
    x = 1  # dump value
    d = 1.1  # dump value
    if 1 < d < toi:
        while not (d.is_integer()):
            d = ((toi * x) + 1) / e
            x += 1
    else:
        print("Error calculating d")
    print("Multiplied toitent x="+str(x-1)+" times")
    return int(d)


def generate_key(p, q):
    n = int(p) * int(q)
    toi = (int(p) - 1) * (int(q) - 1)
    # Public
    e = calculate_e(toi)

    # Private
    d = calculate_d(e, toi)

    # Printing data
    print("Value of e="+str(e)+" and d="+str(d))
    print("Public key pair {n,e}:{"+str(n)+","+str(e)+"}")
    print("Private key pair {n,d}:{" + str(n) + "," + str(d) + "}")

    # 0-Public 1-Private
    key_pair = [[n, e], [n, d]]

    return key_pair


def encrypt(plaintext, n, e):
    ciphertext = (pow(plaintext, e)) % n
    return ciphertext


def decrypt(ciphertext, n, d):
    plaintext = (pow(ciphertext, d)) % n
    return plaintext
