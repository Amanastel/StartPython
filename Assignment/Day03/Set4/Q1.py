def is_anagram(word1, word2):

    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()


    return sorted(word1) == sorted(word2)


# Test the function
word1 = "cinema"
word2 = "iceman"
result = is_anagram(word1, word2)
print(result)  # This will print: True
