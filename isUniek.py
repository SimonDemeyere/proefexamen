def isUniek(arr):
    unique = set(arr)  
    if len(unique) == len(arr):
        print('Deze lijst is uniek')
        return True
    else:
        print('Deze lijst is niet uniek')
        return False