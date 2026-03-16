class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

rootVal = int(input("Enter the root value: "))
root = Node(rootVal, None, None)

def insert(value, node):
    if value <= node.value:
        if node.left is None:
            node.left = Node(value, None, None)
        else:
            insert(value, node.left)
    else:
        if node.right is None:
            node.right = Node(value, None, None)
        else:
            insert(value, node.right)


def search(value, node):
    if node is None:
        return False
    if node.value == value:
        return True
    elif value < node.value:
        return search(value, node.left)
    else:
        return search(value, node.right)
    
def delete(value, node):
    if node is None:
        return None
    if value < node.value:
        node.left = delete(value, node.left)
    elif value > node.value:
        node.right = delete(value, node.right)
    else:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        temp = find_min(node.right)
        node.value = temp.value
        node.right = delete(temp.value, node.right)
    return node

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current
    

while True:
    value = int(input("Enter a value to insert (or -1 to stop), -2 to search: "))
    if value == -1:
        break
    elif value == -2:
        search_value = int(input("Enter a value to search: "))
        if search(search_value, root):
            print(f"{search_value} is in the tree.")
        else:
            print(f"{search_value} is not in the tree.")
    else:
        insert(value, root)