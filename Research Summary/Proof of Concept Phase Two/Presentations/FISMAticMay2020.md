# ![](.//media/image1.png)

# FISMATIC

Encryption Methods and Implementation

May 2020 Updates

## Encryption Background

![Symmetric and Asymmetric Encryption - By Rafael
Almeida](.//media/image2.png)

### Symmetric Encryption

  - Define: Algorithm's that utilize only one key for both encryption
    and decryption.

  - Advanced Encryption Standard (AES) algorithm- NIST approved.

### Python Cryptography Library 

Fernet

  - Fernet Keys use 128 bit AES with Cipher Block Chaining (CBC).

### Current Set-Up 

Key is sent to users to use FISMAtic.

  - An email, separate from the FISMAtic Files, will be sent to the new
    user containing a file with the key as an attachment, using Secret
    Agent.

  - User is prompted to upload key file when FISMAtic is started, the
    program uses the key to decrypt the data and open FISMAtic.
    
      - Prevents error of user downloading key and FISMAtic files to
        different locations, also allows a user to safely keep the key
        separate.
    
      - Set-up allows for room to further protect key file down the
        road.

## Limitations & Security Issues

**There are current ways to bypass this encryption as it is, but it
should be improved in the future.**

  - **A user could very easily write a program that utilizes the key to
    decrypt the data files, since they have access to the key and
    files.**
    
      - **This could be fixed by changing the key utilization to the
        back-end and packaging FISMAtic into an executable file.**

  - **A user could potentially view the files while FISMAtic is
    running.**
    
      - **This could be fixed by re-encrypting the files immediately
        after reading them into memory, instead of upon close of the
        program.**
