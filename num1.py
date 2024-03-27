from collections import Counter
#words = ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two', 'three']
words = ('''Split your string into a list of words using string.split()
Create an empty dictionary to store the word counts
Loop through the list of Sort the in descending order''')
# use the Counter function to count the words
count = Counter(words)
print(count)
print(count['the'])
# print the count of the word 'one'
#print(count['one'])
