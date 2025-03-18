q = int(input("Enter a prime number: "))
a = int(input("Enter a primitive root: "))
Xa = int(input("Enter the private key of A: "))
Xb = int(input("Enter the private key of B: "))

# Calculate public keys
Ya = pow(a, Xa, q)
Yb = pow(a, Xb, q)

print("Public key of A:", Ya)
print("Public key of B:", Yb)

# Calculate shared keys
Ka = pow(Yb, Xa, q)
Kb = pow(Ya, Xb, q)

print("Shared key for A:", Ka)
print("Shared key for B:", Kb)