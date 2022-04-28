import sys
import random
from math import ceil
from decimal import Decimal

p = 2**20
# c = 5
print(p)


def ENC(secret, c):
    secret_num = ""
    for i in secret:
        x = ord(i) + c
        if (x > 99):
            print("Only Capital letters")
            sys.exit("Only Capital Letters")
        secret_num = secret_num + str(x)
    return(int(secret_num))


def DEC(secret, c):
    str(secret)
    x = ""
    secret_string = ""
    j = 0
    for i in range(int(len(secret)/2)):
        x = secret[j] + secret[j+1]
        x = chr(int(x)-c)
        secret_string = secret_string + x
        j = j+2
    return(secret_string)


def reconstruct(shares):

    sum = 0
    i = 0

    for s_i in shares:
        x1, y1 = s_i
        # print(share_j)
        prod = 1
        # print(prod)
        j = 0
        for s_j in shares:
            x2, y2 = s_j
            if i != j:
                prod = prod * Decimal(Decimal(x2)/(x2-x1))
                # print(prod)
            # print(j)
            j = j+1

        prod *= y1
        sum = sum + Decimal(prod)
        # print(i)
        i = i+1
    # print(sum)
    sum = round(Decimal(sum), 0)

    return sum


def generate(n, m, secret):

    coefficients = []
    for i in range(0, m-1):
        x = random.randrange(0, p)
        coefficients.append(x)
        # print("Hello")
    # print(coefficients)
    coefficients.append(secret)
    # print(coefficients)
    shares = []

    for i in range(1, n+1):
        x = random.randrange(1, p)
        point = 0
        k = len(coefficients) - 1
        # print(k)
        for j in coefficients:
            point = point + (x ** k * j)
            k = k-1
        y = point
        shares.append((x, y))

    return shares


secret = input("ENTER A WORD IN ALL CAPITALS: ")
n = int(input("ENTER NUMBER OF SHARES(N): "))
m = int(input("ENTER THE THRESHOLD(M): "))
c = random.randrange(0, 9)
print("Original Secret")
print(secret)

secret_num = ENC(secret, c)

print(secret_num)


print()
print("The Key is - ")
print(c)
print()
print("The shares are -")
shares = generate(n, m, secret_num)
for share in shares:
    print(share)

pool = []

print()
k = int(input("Enter the KEY: "))

print()
print("Enter the shares one by one -")
for i in range(1, m+1):
    print(i)
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    pool.append((x, y))
# pool = random.sample(shares, m)
print()
print('Combining shares -')
for share in pool:
    print(share)


print()
print("Reconstructed secret - ")
recon = reconstruct(pool)
print(recon)
recon = str(recon)
recon_string = DEC(recon, k)
print(recon_string)
