# Challenge 5: Encrypt a string using repeating-key encryption

import sys

def encrypt(message, key):
    """Takes a message and encrypts it using the provided key."""

    encrypted = ""
    key_index = 0

    for c in message:
        char_val = ord(c)
        key_val = ord(key[key_index])
        
        new_val = char_val ^ key_val
        str_val = "%.2X" % new_val
        
        encrypted += str_val

        key_index += 1
        if(key_index == len(key)):
            key_index = 0
        
    return encrypted.lower()

def main():
    if len(sys.argv) < 2:
        message = raw_input("Enter the message to be encrypted: ")
    else:
        file = sys.argv[1]
        with open(file, 'r') as myfile:
            message = myfile.read()

    key = raw_input("Enter the key to be used: ")
    
    message = message[:len(message) - 1]

    print message
    print(encrypt(message, key))

if __name__ == "__main__":
    main()
