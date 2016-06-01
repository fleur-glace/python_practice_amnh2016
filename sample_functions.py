#this will be a collection of out first functions

#our first function
def max_of_three(arg1, arg2, arg3):
    '''this function takes in thee arguments and returns the largest value'''
    if arg1 > arg2 and arg1 > arg3 :
        return  arg1
    elif arg2> arg3 :
        return arg2 
    else :
        return arg3

def list_ends(L):
    '''this function takes in a list and MAKES a new list with the first and last entry. It re'''
    
    print L[0]
    print L.pop()
    return [L[0], L.pop()]


