def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def RSA(p, q, msg):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Find e such that gcd(e, phi) = 1
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            e = i
            break

    # Find d such that (d * e) % phi = 1
    j = 0
    while True:
        if (j * e) % phi == 1:
            d = j
            break
        j += 1

    # Encrypt the message
    c = pow(msg, e, n)
    print("Encrypted message:", c)

    # Decrypt the message
    m = pow(c, d, n)
    print("Decrypted message:", m)

# Input values
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
msg = int(input("Enter a message: "))

# Call the RSA function
RSA(p, q, msg)