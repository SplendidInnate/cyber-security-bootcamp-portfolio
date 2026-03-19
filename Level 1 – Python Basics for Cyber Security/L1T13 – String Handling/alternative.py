#Auto-Grade Task:

#1:
text = input("Enter any string/text: ")
text_output = ""

for i in range(len(text)):
    if i % 2 == 0:
        text_output += text[i].upper()
    else:
        text_output += text[i].lower()

print(f"Text character change: {text_output}")
print(" ")

#2:
user_input = input("Enter any string/text: ")
string = user_input.split()
string_result = []

for i in range(len(string)):
    # If the index is even, make the whole word lowercase; if odd, make it uppercase
    if i % 2 == 0:
        string_result.append(string[i].lower())
    else:
        string_result.append(string[i].upper())

# Join the list back into a single string with spaces
user_input_result = " ".join(string_result)

print(f"String transformation: {user_input_result}")