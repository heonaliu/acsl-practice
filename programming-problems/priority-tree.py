def add(w):
    new_word =input("Enter a new word to add: ")
    word = list("".join(w)+ new_word)
    i = len(word) - 1
    parent_less_than_child = True
    while parent_less_than_child:
        parent_index = (i-1) // 2
        if parent_index < 0:
            break
        if word[parent_index] > word[i]:
            #swap
            word[parent_index], word[i] = word[i], word[parent_index]
            i = parent_index
        else:
            parent_less_than_child = False

    return list(word)


word = list(input("Enter a word: "))

#add multiply by 2 to get the left children and add multiply by 2 and add 1 to get the right children
#get parent: floor divsion by 2

priority_tree = []

#set up the tree ---
for i in range(len(word)):
    parent_less_than_child = True
    while parent_less_than_child:
        parent_index = (i-1) // 2
        if parent_index < 0:
            break
        if word[parent_index] > word[i]:
            #swap
            word[parent_index], word[i] = word[i], word[parent_index]
            i = parent_index
        else:
            parent_less_than_child = False



print("Priority Tree: ", word)
while True:
    print(add(word))
    #print("Priority Tree: ", word)