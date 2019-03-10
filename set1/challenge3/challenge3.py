# File: challenge 3.py
# Program: Cryptopals Crypto Challenges - Single-Byte XOR Cipher
# Description: The hex encoded string below has been XOR'ed against a single character.
#                    Find the key, decrypt the message.

# Cryptopals Set 1 Challenge 3
# The string has been XOR'd against a single character

import sys

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
ALPHA_PCTS = {
    'e' : 12.02,
    't' : 9.10,
    'a' : 8.12,
    'o' : 7.68,
    'i' : 7.31,
    'n' : 6.95,
    's' : 6.28,
    'r' : 6.02,
    'h' : 5.92,
    'd' : 4.32,
    'l' : 3.98,
    'u' : 2.88,
    'c' : 2.71,
    'm' : 2.61,
    'f' : 2.30,
    'y' : 2.11,
    'w' : 2.09,
    'g' : 2.03,
    'p' : 1.82,
    'b' : 1.49,
    'v' : 1.11,
    'k' : 0.69,
    'x' : 0.17,
    'q' : 0.11,
    'j' : 0.10,
    'z' : 0.07}
    
def print_dict(dict):
    """Print out the given dictionary in a pretty format."""
    for c in sorted(dict):
        print(c + ": " + str(dict[c]))

        
def compute_freqs(input):
    """This takes an input string and returns the letter frequencies in the string."""

    # Initialize a dictionary to keep track of letter frequencies within the input
    letter_freq = {}
    for c in ALPHABET:
        letter_freq[c] = 0

    # Calculate the letter frequencies within the input
    for c in input.lower():
        if c in ALPHABET:
            letter_freq[c] += 1
        
    return letter_freq


def score_string(input):
    """Takes a string as input and scores it based on how closely it resembles English."""

    # Calculate the number of letters in the string
    total_let = 0
    for c in input.lower():
        if c in ALPHABET:
            total_let += 1
    
    letter_freq = compute_freqs(input)
    
    #Calculate the score. Lower is better.
    score = 0
    for c in letter_freq:
        if total_let == 0:
            return 9999
        letter_pct = (float(letter_freq[c]) / total_let) * 100
        deviation = abs(letter_pct - ALPHA_PCTS[c])
        score += deviation
        
    return score


def decode(input, char_val):
    """Takes an input message and tries each character as the key."""

    decrypted = ""
    for i in range(0, len(input), 2):
        sub_str = input[i:i+2]
        plaintext = chr(int(sub_str, 16) ^ char_val)
        decrypted += plaintext

    return decrypted


def decrypt(message):
    """Puts it all together!"""

    best_score = 9999
    best_string = ""
    key_char = ''
    
    for char_val in range(0, 256):
        decoded = decode(message, char_val)
        score = score_string(decoded)
        if(score < best_score):
            best_score = score
            best_string = decoded
            key_char = chr(char_val)

    return (key_char, best_string)
        

def main():
    if len(sys.argv) < 2:
        input = raw_input()
    else:
        file = sys.argv[1]
        with open(file, 'r') as myfile:
            input = myfile.read()

    answer = decrypt(input)
    print("Message: " + answer[1] + "\nKey: " + answer[0])


if __name__ == "__main__":
    main()
