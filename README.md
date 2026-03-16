# Cipher Toolkit 

## Overview
A command-line cryptography toolkit built in Python implementing two classic
encryption ciphers. Built to explore the math behind cryptography and 
how encryption works at a foundational level.

## Ciphers
**Caesar Cipher**
Shifts each letter in a message by a fixed number. One of the oldest 
encryption techniques, famously used by Julius Caesar.

**Vigenère Cipher**
An extension of Caesar that uses a keyword to apply a different shift 
to each letter, making it significantly harder to crack.

**Brute Force Cracker**
Tries all 26 possible Caesar shifts to crack an encrypted message 
without knowing the original key.

## How to Run
```bash
python3 cipher_toolkit.py
```

## Example
```
Caesar:   "Hello World" + shift 3  → "Khoor Zruog"
Vigenère: "Hello World" + key "KEY" → "Rijvs Ambpb"
Brute Force: paste any Caesar encrypted text to crack it
```

## Built With
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## What I Learned
- How substitution ciphers work mathematically using modular arithmetic
- The difference between single-key and polyalphabetic encryption
- How brute force attacks work against weak encryption
- Foundations of cryptography as part of an interest in cybersecurity

> ⚠️ **Note:** This is a personal learning project — built to explore the 
> foundations of cryptography and practice Python while diving into 
> cybersecurity concepts for the first time.
