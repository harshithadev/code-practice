# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:

# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

# count_word_frequency(words)
# Output:

#  {'apple': 3, 'orange': 2, 'banana': 1}


dic = {}


def count_word_frequency(words):
    for word in words:
        if word in dic.keys():
            dic[word] += 1
        else:
            dic[word] = 1


print(dic)
