'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # Verify the lenght of the word 
    if len(word) < 2:
        return 0
    # Make word lower case and verify if following 2 words equal to "th"
    elif word[0:2] == "th":
        # If it is return count + 1
        return count_th(word[2:]) + 1 
    else:
        return count_th(word[1:])

print(count_th("brniothbwnrwivqnieorth"))