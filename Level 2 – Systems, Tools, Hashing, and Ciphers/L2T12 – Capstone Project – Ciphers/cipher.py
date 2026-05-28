# Practical Task (L2T12): Capstone Project

"""
Cipher Program

The program shifts letters by 15 places.
"""

# Function for encoding the message
def encode_message(message):

    # A string to store encoded text
    encoded = ""

    # For-loop to loop through every character in the message
    for char in message:

        # if for low characters
        if char.islower():
            ascii_value = ord(char)

            # Converting ascii to alphabet position
            position = ascii_value - ord("a")
            new_position = (position + 15) % 26

            # Converting back to ascii
            new_ascii = new_position + ord("a")
            # Converting ascii back to character
            encoded += chr(new_ascii)

        # if for upper characters
        elif char.isupper():
            ascii_value = ord(char)
            position = ascii_value - ord("A")
            new_position = (position + 15) % 26
            new_ascii = new_position + ord("A")
            encoded += char
        
        # Keeping spaces and punctuation unchanged
        else:
            encoded += char

    # Returning encode message
    return encoded

# User input
user_inputmsg = input("Please Enter Message: ")

result_message = encode_message(user_inputmsg)

print(f"Encode Message: {result_message}")

