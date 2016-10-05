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


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    tup = choice(chains.keys())
    text = list(tup)

    # text = []
    # for word in tup:
    #     text.append(word)

    while chains.get(tup):
        new_word = choice(chains[tup])
        tup = tup[1:] + (new_word,)
        text.append(new_word)
    
    return " ".join(text)

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 8)

# Produce random text
random_text = make_text(chains)

print random_text
