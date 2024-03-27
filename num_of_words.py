string = input("enter string:")
words = string.split()
word_count = {}
for word in words:
    word_count[word]=words.count(word)
for key, value in word_count.items():
    print(f"the word \"{key}\" is repeated{value} times")  

