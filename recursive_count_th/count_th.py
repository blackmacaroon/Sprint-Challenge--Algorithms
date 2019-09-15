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
    -recursively ?????
'''
def count_th(word):
    counth = 0
    if len(word) == 0:
            return 0
    if len(word) < 3:
        return 0
    if word == "th":
        return 1
    # else:
    #     return word.count("th")

    def help_me_count(word):
        if word[0:2] == "th":
            counth += 1
    
        return count
    elif #th does appear, recursively iterate with index + 1 and count + 1]

count_th("this is the worst")

   



# #call recursive helper function
#     count_th(word)
# #return a count of how many times 'th' appears
#     return count


    
    