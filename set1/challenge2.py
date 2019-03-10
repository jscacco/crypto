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

def string_to_bin_val(str):
    """Takes a string as input and returns the binary value of the string."""

    bin_val = 0

    #Iterate through the string, multiplying by 2 and then adding one if appropriate
    for c in str:
        #Subtract 48 because that is the ascii value of '0'
        char_val = ord(c) - 48
        bin_val *= 2

        if char_val != 0 and char_val != 1:
            print("Invalid format!")
            return -1
        else:
            bin_val += char_val

    return bin_val

        
def bin_val_to_string(val):
    """Takes a value and returns the corresponding UNSIGNED binary string"""
    if(val == 0):
        return "0"
    elif(val < 0):
        return("Please enter a natural number!")
    
    my_string = ""
    while val > 0:
        if (val % 2) == 1:
            my_string = "1" + my_string
            val -= 1
        else:
            my_string = "0" + my_string
        val /= 2
        
    return my_string

def xor(str1, str2):
    """Takes two strings as input and returns the XOR of the two."""

    #Convert both from their hex representations to their binary representations
    val_1 = bin_val_to_string(string_to_hex_val(str1))
    val_2 = bin_val_to_string(string_to_hex_val(str2))

    #Add leading zeros to a string until both are the same length
    while(len(val_1) != len(val_2)):
        if len(val_1) > len(val_2):
            val_2 = "0" + val_2
        else:
            val_1 = "0" + val_1

    new_string = ""

    for i in range(len(val_1)):
        if val_1[i] != val_2[i]:
            new_string += '1'
        else:
            new_string += '0'

    return "%x" % string_to_bin_val(new_string)
    
def main():
    str1 = raw_input()
    str2 = raw_input()
    print(xor(str1, str2))

if __name__ == "__main__":
    main()
