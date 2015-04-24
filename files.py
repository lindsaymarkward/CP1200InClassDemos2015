__author__ = 'sci-lmw1'

# writeFile = open("data.txt", 'a')
# # writeFile.write("CP1200 is such\n\n a good\nSubject!!!")
# # writeFile.write("Goodbye")
# writeFile.write("\nHappy!\n")
# writeFile.close()

# file = open("data.txt", 'r')
# # text = file.read()
# countLines = 0
# for line in file:
#     line = line.strip()
#     print(repr(line))
#     countLines += 1
#     # if line == "\n":
#     #     break
#
#
# file.close()
# print(countLines)
#
# # print(text)
# # print(repr(text))

"""
Write pseudocode for a program that opens a file and toggles
"on" and "off" each time it's run. 
So, if the file contains "on", change it to "off" and vice versa

file = open "switch.txt" file for reading
line = read line from file
close file
file = open "switch.txt" file for writing
if line == "on"
    write "off" to file
else
    write "on" to file
close file
"""

file = open("switch.txt")
line = file.read().strip()
file.close()
file = open("switch.txt", 'w')
if line == "on":
    file.write("off")
else:
    file.write("on")
file.close()
