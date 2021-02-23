str = input("Enter the string : ")
vowels = 0
digits = 0
consonants = 0
spaces = 0
symbols = 0
str = str.lower()
for i in range(0, len(str)):
    if(str[i] == 'a' or str[i] == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
        vowels = vowels + 1
    elif((str[i] >= 'a' and str[i] <= 'z')):
        consonants = consonants + 1
    elif(str[i] >= '0' and str[i] <= '9'):
        digits = digits + 1
    elif (str[i] == ' '):
        spaces = spaces + 1
    else:
        symbols = symbols + 1

print("Vowels: ", vowels)
print("Consonents: ", consonants)
print("Digits: ", digits)
print("White Spaces: ", spaces)
print("Symbols: ", symbols)
