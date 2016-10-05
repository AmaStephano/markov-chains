# Write a function that takes sentence as a str.  Reverse words in sentence, 
# including more than one space

def reverse_sentence_with_spaces(sentence):
    words_and_spaces = sentence.split(" ")
    words_and_spaces.reverse()
    return " ".join(words_and_spaces)

# print reverse_sentence_with_spaces("Dogs are so  much  better.")


# Write a function that takes word as a str; true if palindrome

def is_palindrome(phrase):
    for index in range(len(phrase) / 2):
        if phrase[index] != phrase[-index - 1]:
            return False

    return True

# print is_palindrome("tacocat")


# Checks is word is anagram of a palindrome

def is_anagram_palindrome(word):
    
    count_dict = {}

    for letter in word:
        count_dict[letter] = count_dict.get(letter, 0) + 1

    flag = 0

    for number in count_dict.values():
        if number % 2 == 1:
            flag += 1

    if flag > 1:
        return False
    else:
        return True

print is_anagram_palindrome("a")
