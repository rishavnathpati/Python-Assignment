str = "Input a sentence and find the number of words starting with S"

words = str.split()
num = 0
for i in range(len(words)):
    if(words[i][0] == 's' or words[i][0] == 'S'):
        num += 1

print("The number of words starting with'S' is: ", num)
