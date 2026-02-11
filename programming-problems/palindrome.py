#2001-2002 Int Division Programming Problem - Contest 3
path = "programming-problems/palindrome.txt"

with open(path, 'r') as file:
    inputs = file.readlines()

inputs = [i.strip().split(",") for i in inputs]

#recursive function
def find_palindrome(num, base, steps = 0):
    #base case: if num IS a palindrome
    if (is_palindrome(num,base)):
        return toBase(num,base)
    #once hit 10 steps -- return NONE and num
    if steps == 10:
        return "NONE " + toBase(num, base)
    return find_palindrome((num + reverse_num(num, base)), base, steps+1)

#checks if number in base is palindrome    
def is_palindrome(n,base):
    s = toBase(n, base)
    return s == s[::-1]

#reverses num
def reverse_num(n, base):
    base_str = toBase(n, base)
    reversed_str = base_str[::-1]
    return int(reversed_str, base)

#converts back to base number
def toBase(n, base):
    if n == 0:
        return 0
    s = ""
    while n>0:
        s = str(n%base) + s
        n//=base
    return s

#main program here --
for t in inputs:
    base = int(t[1])
    num = int(t[0], base)
    #print(num, base)

    print(find_palindrome(num,base))

#print(inputs)