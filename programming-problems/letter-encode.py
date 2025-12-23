#2001 - 2002 ACSL Wrap Around Code
#Heona Liu 12/23/25

def get_alpha_pos(char):
    if not char.isalpha() or len(char) != 1:
        return "Invalid Character"
    pos = ord(char.lower()) - ord('a') + 1
    return int(pos)

def to_letter(num):
    return chr(ord("A") + num - 1)

def largest_factor(n):
    for i in range(n//2, 0, -1):
        if n%i == 0:
            return i  
    return 1

def getMethod(char):
    m1, m2, m3, m4, m5 = "ABCDE", "FGHIJ", "KLMNO", "PQRST", "UVWXYZ"
    if char in m1:
        return 1
    if char in m2:
        return 2
    if char in m3:
        return 3
    if char in m4:
        return 4
    if char in m5:
        return 5
    
    #example usage: (1, 2, 1) --> (A, B, 1) returns 5
    #example usage: (25, 2, 1) --> (Y, B, 1) 
def new_character(prev, curr, method):
    if (method == 1): #multiply by 2
        curr*=2
        new = int((prev+curr))%26
        return to_letter(new)
    elif(method == 2): #divide num by 3, multiply rem by 5
        new = int(curr % 3) * 5
        new = int((prev+new))%26
        return to_letter(new)
        
    elif(method == 3): #divide num by 4, multiply int of quot by 8
        new = int(curr/4) * 8
        new = int((prev+new))%26
        return to_letter(new)
    
    elif(method == 4): #mult. sum of digits by 10 
        sum =0
        #count the number of digits
        while curr > 0:
            digit=curr%10
            sum += digit
            curr = int(curr/10)
        new = (sum * 10)%26
        new = int((prev+new))%26
        return to_letter(new)
    elif(method == 5): #find largest factor then mult. by. 12
        new = int(largest_factor(curr) * 12) % 26
        new = int((prev+new))%26
        return to_letter(new) 
    else:
        return " - ELSE"

inputs = []
prev = ""

for i in range(5):
    sample = input(str(i+1) + ". ")
    sample = sample.replace(" ", "")
    w = sample.split(",")
    inputs.append(w)
    
#print(inputs)
for i in range(len(inputs)):
    word = ""
    for j in range(len(inputs[i])-1):
        letter = inputs[i][j]
        alpha_pos = get_alpha_pos(letter)
        if prev == "": #means it's the first letter
            prev = 1 #set it to A
        converted = new_character(prev, alpha_pos, getMethod(letter))
        word += " " +converted
        #reassign previous letter to position
        prev = get_alpha_pos(converted)
    
    print(str(i+1) + ". " + word)    
    prev = ""