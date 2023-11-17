#Word replacement program 
# This strengthens my knowledge of replace in python

def replace_word():

    str = "Hi guys, I am Nicholas, and hi hi hi"
    word_to_replace = input('Enter the word word to replace: ')
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()