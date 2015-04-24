__author__ = 'sci-lmw1'

s = "This is a string with words in it"
s = "Th,is ? is /a       string*& wi^th words; in it!?!"

newString = ""

for ch in s:
    if ch.isalpha() or ch.isspace():
        newString += ch

while "  " in newString:
    newString = newString.replace("  ", " ")

print(newString)

words = newString.split(" ")

print(words)


# for ch in s:
#     print(ch)

# i = 0
# while i <= len(s):
#     print(s[i])
#     i += 1
