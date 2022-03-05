# RSA
import sys

import functions as fn
import digest as dg

# from functions import *

"""
Steps:
1:
2 Large co-prime num gen (p,q)
calculate n=pq (1024bits)
calculate toitent Q(toi)=(p-1)(q-1)
choose e, 1<e<Q  &  gcd(e,Q)=1 //co-prime(e,Q)
calculate d, 1<d<Q  &  ed==1modQ

d,p,q,Q are secret
n = known MOD
e = public/encryption exponent
d = private/secret/decryption exponent

public key is (n,e) private key is (d,p,q) or (n,d)

2:
encryption:
public key (n,e)
ciphertext = plaintext^e mod n

decrpytion:
private key (d,p,q)/(n,d)
plaintext = ciphertext^d mod n

"""
# print(fn.is_co_prime(29, 89))
# print(fn.calculate_d(13, 40))
choice = 0
while choice != 4:
    try:
        choice = int(input("\n1.Generate Keys\n2.Encrypt\n3.Decrypt\n4:Exit\n"))

        # Generate Keys
        if choice == 1:

            p = int(input("Enter two large prime numbers\np: "))
            q = int(input("q: "))

            if fn.is_co_prime(p, q):
                key_pair = fn.generate_key(p, q)

        elif choice == 2:

            plaintext = input("Enter plaintext:\n")
            n = int(input("Enter public key pair {n,e}\nn: "))
            e = int(input("e: "))

            ciphertext = ""

            for i in plaintext:
                ciphertext += str(fn.encrypt(int(dg.letter_to_int(str(i))), n, e))+"-"

            # Neutral bit
            ciphertext += "0"

            # ciphertext = fn.encrypt(plaintext_int, n, e)
            print("Ciphertext: "+str(ciphertext))

        elif choice == 3:

            ciphertext = input("Enter ciphertext:\n")
            n = int(input("Enter private key pair {n,d}\nn: "))
            d = int(input("d: "))

            listNumbers = ciphertext.split("-")
            plaintext_num = ""

            for i in listNumbers:
                if int(i) == 0:
                    break
                else:
                    plaintext_num += str(fn.decrypt(int(i), n, d))+"-"

            plaintext_num += "0"

            listLetters = plaintext_num.split("-")
            plaintext = ""

            for i in listLetters:
                if int(i) == 0:
                    break
                else:
                    plaintext += str(dg.int_to_letter(int(i)))

            # plaintext = fn.decrypt(int(ciphertext), n, d)
            print("Plaintext: "+str(plaintext))

        elif choice == 4:
            print("Terminating process")
            # sys.exit()

        else:
            print("Invalid choice")

    except ValueError as e:
        print(e)

# print(fn.generate_key(7, 17))

# print(fn.encrypt(45, 119, 5))

# print(fn.decrypt(61, 119, 77))
