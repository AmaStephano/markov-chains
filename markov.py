from random import choice
import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path) as file_to_string:

        return file_to_string.read()


def make_chains(text_string, n):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """
    words = text_string.split()
    chains = {}

    for index in range(len(words) - n):

        # temp_list = []
        # for number in range(n):
        #     temp_list.append(words[index + number])
        # OR
        # temp_list = words[index:index+n]
        #
        # THEN
        # tup = tuple(temp_list)

        tup = tuple(words[index:index + n])

        # if chains.get(tup):
        #     chains[tup].append(words[index + n])
        # else:
        #     chains[tup] = [words[index + n]]

        chains.setdefault(tup, []).append(words[index + n])

    # print chains        
    return chains


def make_text(chains, max_words):
    """Takes dictionary of markov chains; returns random text."""

    # tup = choice(chains.keys())
    # first_letter = tup[0][0]

    # while not first_letter.isupper():
    #     tup = choice(chains.keys())
    #     first_letter = tup[0][0]

    #Could use istitle() instead on the whole word
    #or could do a list comprehension of all keys with first letter captalized
    capital_keys = [key for key in chains.keys() if key[0].istitle()]
    tup = choice(capital_keys)

    text = list(tup)


    # text = []
    # for word in tup:
    #     text.append(word)

    # while chains.get(tup):
    #     new_word = choice(chains[tup])

        # can slice tuples. Don't need a list to do this
        # then adding new word to the slice
        # tup = tup[1:] + (new_word,)
        # text.append(new_word)
        
    while len(text) < max_words:
        new_word = choice(chains[tup])
        tup = tup[1:] + (new_word,)
        text.append(new_word)

    # while True:
    #     if text[-1][-1] in (".", "?", "!"):
    #        return " ".join(text)
    #     else:
    #         text = text[:-1]

    for index, word in reversed(list(enumerate(text))):
        if word[-1] in (".", "?", "!") or word[-2:] == ".\"":
            return " ".join(text[:index + 1])
            


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 2)

# Produce random text
random_text = make_text(chains, 100)

print random_text
