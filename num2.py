#write a function to print the number of words in a sentence
s= " you must be the change you wish to see the world."
def count_words(sentence):
    num_words=len(sentence.split())
    return num_words
print("original sentence:",s)
print("number of words in original sentence:",count_words(s))