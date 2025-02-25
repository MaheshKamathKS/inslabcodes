
S = input("Enter a string: ")
result = "".join(format(ord(i), '08b') for i in S)
print("Result:", result)

l = int(len(result) / 2)
left = result[:l]
right = result[l:]

K = input("Enter a key: ")
key = "".join(format(ord(i), '08b') for i in K)

S = bin(int(right, 2) + int(key, 2))
answer = bin(int(S[2:], 2) ^ int(left, 2))

newr = answer[2:]
newl = right

newr, newl = newl, newr

S = bin(int(S[2:], 2) ^ int(newl, 2))
nl = newr
nr = answer[2:]
nl, nr = nr, nl

cipher = nr + nl
if len(cipher) != len(result):
    while len(cipher) <= len(result):
        cipher = "0" + cipher

print(cipher)

plainText = ""
for i in range(0, len(cipher), 8):
    temp = cipher[i:i + 8]
    d = int(temp, 2)
    plainText = plainText + chr(d)

print(plainText)