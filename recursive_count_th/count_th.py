'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
    subString = "th"
    l1 = len(word)
    l2 = len(subString)
    # base case | edge cases
    if (l1 == 0 or l1 < l2):
        return 0
    if word == subString:
        return 1
    # recursive case
    if (word[0 : l2] == subString): 
        return count_th(word[l2 - 1:]) + 1
    # Otherwise, return the count 
    # from the remaining index 
    else:
        return count_th(word[l2 - 1:])


print(count_th("this is the worst"))


   



# #call recursive helper function
#     count_th(word)
# #return a count of how many times 'th' appears
#     return count


    
    