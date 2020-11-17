import sys
import os
import time

from random import choice, shuffle

def make_sentence(words):
    """Take a list of strings as input and join them together (with spaces in between) to form a sentence."""
    return ' '.join(words)

def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains."""

    chains = {}

    words = text_string.split()
    for i in range(len(words) - 2):
        key = (words[i], words[i + 1])
        value = words[i + 2]

        if key not in chains:
            chains[key] = []
        #else:
        chains[key].append(value)

    return chains

# * Temporary markov chain visualization in the terminal.
def clear_screen():
    """Check the operating system, then clear the screen using the appropriate clear screen command"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def make_text(chains, min_words):
    """Take dictionary of Markov chains; return random text."""

    keys = list(chains.keys())
    key = choice(keys)

    words = [key[0], key[1]]
    while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text).

        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.
        terminating_word = None
        for c in chains[key]:
            if (c[-1] == '.'):
                terminating_word = c
        
        # Choose a word from the words in the chain associated with our key.
        chosen_word = choice(chains[key])
        # Only if we have more than one word in the chain, do a visualization.
        if len(chains[key]) > 1:
            # If the chosen word is also the first word in the chain (i.e., we
            # happened to pick the first word in the chain)
            if chosen_word == chains[key][0]:
                # in this special case, print the sentence with the word
                # joined, but add a * on both sides.
                print(make_sentence(words) + ' *' + chains[key][0] + '*')
            else:
                # otherwise, print the sentence, with the first word of the
                # chain appended.
                print(make_sentence(words) + ' ' + chains[key][0])

            # Go through the rest of the words in the chain (if any).
            for i in range(1, len(chains[key])):
                c = chains[key][i]
                # If the current word in the chain is the chosen word,
                if (c == chosen_word):
                    # Print it with '*' on both sides.  Make sure we justify
                    # the length of the sentence till now,
                    # so Python will automatically put the same number of
                    # spaces in front of this word as is the length
                    # of the sentence.
                    print(('*' + chosen_word + '*').rjust(len(make_sentence(words)) + len(chosen_word) + 3))
                else:
                    # otherwise just print it.  Again, make sure we justify the
                    # length of the sentence till now,
                    # so Python will automatically put the same number of
                    # spaces in front of this word as is the length
                    # of the sentence.
                    print(c.rjust(len(make_sentence(words)) + len(c) + 2))

            # # At this point, we have printed the sentence, and also all the
            # # words in the chain.  Sleep for a second so the user can see the
            # # full sentence, along with the words in the chain.
            # time.sleep(1.0)
            clear_screen()
            # # Now just print the sentence as it would be after the word chosing
            # # process is over.

            print(make_sentence(words) + ' ' + chosen_word)
            # # Sleep for another half a second so the user gets to see the full
            # # sentence with the word now added in.
            # time.sleep(0.5)
        else:
            # Else, if we only had one word, just join that to the list of
            # words
            print(make_sentence(words))
            # Sleep for 0.1s.  This will allow the user to see the sentence
            # with the new word momentarily before we replace the sentence with a new one.
            # time.sleep(0.1)

        # If we already have the number of words we need, and have a
        # terminating word available?
        if len(words) > min_words and terminating_word != None:
            # then append the terminating word to the words list.
            words.append(terminating_word)
            # clear the screen before we exit, since we are done with
            # visualization and are now just returning the actual string.
            clear_screen()
            return make_sentence(words)
        else:
            word = chosen_word
        words.append(word)
        key = (key[1], word)
        # clear the screen, we're done visualizing.  The next iteration will
        # visualize the next word being added, so let's make sure that the
        # screen is clear before then.
        clear_screen()
    return make_sentence(words)

min_words = 10
# shuffle(trump_tweets)

# ! ONLY for Algorithm testing below; functions are being called in a separate file
# chains = make_chains(make_sentence(trump_tweets))
# text = make_text(chains, min_words)

# print(text)