# Password Cracking Assignment

Coded in Python, As assigned by the 2022 CSHS Cybersecurity course

*- <3 Stephen*
### Rubric (50/50)

- [x] Top 10,000 most common passwords can be cracked
- [x] MD5 hashed passwords can be checked
- [x] BCrypt hashed passwords can be checked
- [x] SHA-256 hashed passwords can be checked
- [x] Brute force approach option
- [x] Dictionary Attack option
- [X] Command line arguments can be taken in

### FLAGS

```
-h               // HELP 

/** Encryption Algorithms **/
-d               // DICTIONARY ATTACK
-m               // md5 ATTACK
-s               // sha256 ATTACK
-b               // BCrypt ATTACK

/** Encrypt or Decrypt **/
-
-

/** Dictionary or Brute Force **/
-
-
-
```

### DEPENDENCIES
 - Python3 (duh)
 - hashlib
 - sys
 - getopt
 - bcrypt (pip install bcrypt)
 - basehash (pip install BaseHash)

### RUNNING THIS PROGRAM LOCALLY

To run this program on a local machine you will need to install all of the nessecary dependencies, and then call `main.py` along with any flags you may want to have

### FORMATTING

```
~$ python3 main.py <ENCRYPTION ALGORITHM> <ENCRYPT OR DECRYPT> <DICTIONARY OR BRUTE FORCE>
```
The program will then promt you through the encryption or decryption process.
