# Cryptography Ciphers in Python

This repository contains Python implementations of various classical cryptographic ciphers. These ciphers demonstrate fundamental encryption techniques and their evolution over time. The following encryption algorithms are included:

## Implemented Ciphers

- **Caesar Cipher** - A simple substitution cipher that shifts characters by a fixed number of positions in the alphabet.
- **Monoalphabetic Cipher** - A substitution cipher where each letter in the plaintext is replaced with a corresponding letter from a fixed shuffled alphabet.
- **Playfair Cipher** - A digraph substitution cipher that encrypts pairs of letters using a 5x5 matrix.
- **Hill Cipher** - A polygraphic substitution cipher based on matrix multiplication.

## Prerequisites

Ensure you have Python installed on your system. You can check by running:

```sh
python --version
```

If Python is not installed, download and install it from [python.org](https://www.python.org/).

## Running the Programs

Each cipher program is a standalone script. Follow these steps to run them:

### Clone the Repository

```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### Run a Specific Cipher

```sh
python ceaserCipher.py
python monoCipher.py
python playfairCipher.py
python hillCipher.py
python Des.py
python VignereCipher.py
python FiestelCipher.py
```

Follow the on-screen instructions to encrypt or decrypt messages using the respective ciphers.

## Contributions

Feel free to contribute by submitting issues or pull requests to improve the ciphers or add new features. Suggestions and optimizations are always welcome!

---

### License

