BASE_64_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def string_to_hex_val(str):
    """Takes a string as input and returns the hex value of the string."""
    hex_val = 0
    
    #Convert the string to uppercase and interate through it. 
    for c in str.upper(): 
        char_val = ord(c)
        hex_val *= 16
        
         # If we have an actual number, just add that number.
        if char_val >= ord("0") and char_val <= ord("9"):
            hex_val += char_val - ord("0")

        #If we have a letter, add the corresponding value.
        elif char_val >= ord("A") and char_val <= ord("F"):
            # Add 10 because that is the value of 'A'
            hex_val += char_val - ord("A") + 10

        # If it is neither 0-9 nor A-F, it is not a hex character
        else: 
            print("Invalid format!")
            return -1

    return hex_val

def val_to_64(val):
    """Takes a value as input and returns its base-64 representation."""
    total = val
    my_string = ""
    while(total > 0):
        temp_val = total % 64
        my_string += BASE_64_CHARS[temp_val]
        total -= temp_val
        total >>= 6

    return my_string[::-1]

def main():
    user_input = raw_input()
    print(val_to_64(string_to_hex_val(user_input)))
    
if __name__ == "__main__":
    main()
