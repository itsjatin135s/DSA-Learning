# capitalizeWords Solution

def cap(s):
    if len(s)<=1:
        return s[0].upper()
    return s[0].upper()+cap(s[1:])

#Exmaple
print(cap('Hello mr jatin'))

#for array

def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])



words = ['i', 'am', 'learning', 'recursion']

#Example
print(capitalizeWords(words)) # ['I', 'AM', 'LEARNING', 'RECURSION']