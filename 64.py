def removeCharRecursive(str, X):

    if (len(str) == 0):
        return ""

    return str.replace(X, "")


str = "RishavNathPati"

X = "Rishav"

str = removeCharRecursive(str, X)

print(str)
