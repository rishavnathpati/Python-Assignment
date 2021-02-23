name = input("Enter your name:")
words = name.split()
short = ""
for i in range(len(words)):
    short = short+words[i][0].upper()
    short = short+". "

print(short)
