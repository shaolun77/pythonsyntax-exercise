def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase. 
    How can you change a word to uppercase? Ask Python for help on what you can do with strings!

    Turn that into a function, print_upper_words. Test it out. 
    (Dont forget to add a docstring to your function!)
    """  

    for word in words:
        print(word.upper())


# Change that function so that it only prints words that start with 
# the letter ‘e’ (either upper or lowercase).

def print_upper_wordsv2(words):

    for word in words:
        if word.startswith("e") or word.startswith("E"):
            print(word.upper())



# Make your function more general: you should be able to pass in a set of letters, 
# and it only prints words that start with one of those letters.

# For example:

# # this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_wordsv3(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})

def print_upper_wordsv3(words, must_start_with):
 
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())