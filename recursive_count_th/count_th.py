'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
'''
understand the problem
    -takes in a string
    -counts the "th"
    -can't use loops
plan
    -edge cases
    -set empty variable
    -recursively 
'''
def count_th(word):
    if len(word) < 3:
        return 0
    if word == "th":
        return 1
    else:
        return word.lower().count("th")

count_th("this is the worst")


#     if len(word) == 0:
#         return 0
#     def help_me_count(letters, new_count=0)
    
#     #th does not appear in the word "base case"
#         return count
#     elif #th does appear, recursively iterate with index + 1 and count + 1]

   



# #call recursive helper function
#     count_th(word)
# #return a count of how many times 'th' appears
#     return count


    
    