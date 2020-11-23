# ! old markov chain code

"""A Markov chain generator that can tweet random messages."""
"""Generate Markov text from _______text files_______"""
import sys
from random import choice


def open_and_read_file(filenames):
    """Take list of files. Open them, read them, and return one long string."""

    body = ''
    for filename in filenames:
        text_file = open(filename)
        body = body + text_file.read()
        text_file.close()

    return body



def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = {}

    words = text_string.split()
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)

    return chains


def make_text(chains):
    """Take dictionary of Markov chains; return random text."""

    keys = list(chains.keys())
    key = choice(keys)

    generated_words = [key[0], key[1]]
    while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text).

        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

        word = choice(chains[key])
        generated_words.append(word)
        key = (key[1], word)

    return ' '.join(words)


# Get the filenames from the user through a command line prompt, ex:
# python markov.py green-eggs.txt shakespeare.txt
# filenames = sys.argv[1:]
filenames = ['sampletext.txt']

# Open the files and turn them into one long string
text = open_and_read_file(filenames)

# Get a Markov chain
# chains = make_chains(text)
# print(chains)

# random_text = make_text(chains)
# print(random_text)
###################################################
# *******************************

# def open_and_read_file(file_path):
#     """Take file path as string; return text as string.

#     Takes a string that is a file path, opens the file, and turns
#     the file's contents as one string of text.
#     """

#     file_1 = open(file_path)
#     file_text = file_1.read()
#     return file_text

# def make_chains(text_string):
#     """Take input text as string; return dictionary of Markov chains.

#     A chain will be a key that consists of a tuple of (word1, word2)
#     and the value would be a list of the word(s) that follow those two
#     words in the input text.

#     For example:

#         >>> chains = make_chains('hi there mary hi there juanita')

#     Each bigram (except the last) will be a key in chains:

#         >>> sorted(chains.keys())
#         [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

#     Each item in chains is a list of all possible following words:

#         >>> chains[('hi', 'there')]
#         ['mary', 'juanita']

#         >>> chains[('there','juanita')]
#         [None]
#     """
#     chains = {}
#     text_string_list = text_string.split()

#     #parsing through text string using the loop
#     for i in range(0, len(text_string_list)):
#         #create a tuple of current word and next word 
#         # eg: if input string = "Would you could"; output would be: ('Would', 'you,')('you,', 'could')
#         if i < len(text_string_list)-1:
#             dict_key = (text_string_list[i], text_string_list[i + 1])

#             if i < len(text_string_list)-2:
#                 dict_key_val = [text_string_list[i + 2]]
#                 chains[dict_key]= chains.get(dict_key, []) + dict_key_val
                 
#     return chains


# def make_text(chains):
#     """Return text from chains."""

#     # Randomly select a dictionary key from chains
#     keys_list = list(chains.keys())
#     current_key = choice(keys_list)
#     words = [current_key[0], current_key[1]]

#     def generate_rand_current_word(chains, current_key):
#         dict_value_of_current_key= chains[current_key]
#         rand_current_word = choice(dict_value_of_current_key)
#         return rand_current_word
    
#     words.append(generate_rand_current_word(chains, current_key))
#     current_key = (words[1], words[2])

#     # Main function program
#     while current_key in chains:
#         words.append(generate_rand_current_word(chains, current_key))
#         len_words = len(words)
#         current_key = (words[len_words-2], words[len_words-1])

#     return ' '.join(words) 
    
# input_path = 'gettysburg.txt'

# # Open the file and turn it into one long string
# input_text = open_and_read_file(sampletext.txt)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print(random_text)













