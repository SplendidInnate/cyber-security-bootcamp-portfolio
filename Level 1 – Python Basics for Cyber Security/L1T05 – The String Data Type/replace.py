#Task 2:

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence.replace("!", " "))
print(" ")
print(sentence.replace("!", " ").upper())
print(" ")
sentence_fix = sentence.replace("!", " ").upper()
print(sentence_fix[::-1])