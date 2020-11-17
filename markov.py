trump_tweets = ['''Sorry losers and haters, but my I.Q. is one of the highest -and you all know it! Please don't feel so stupid or insecure,it's not your fault", "Lowest rated Oscars in HISTORY. Problem is, we don’t have Stars anymore - except your President just kidding, of course", "Deals are my art form. Other people paint beautifully or write poetry. I like making deals, preferably big deals. That's how I get my kicks.", "Robert I'm getting a lot of heat for saying you should dump Kristen- but I'm right. If you saw the Miss Universe girls you would reconsider.", "Amazing how the haters & losers keep tweeting the name “F**kface Von Clownstick” like they are so original & like no one else is doing it...", "Time Magazine called to say that I was PROBABLY going to be named “Man (Person) of the Year,” like last year, but I would have to agree to an interview and a major photo shoot. I said probably is no good and took a pass. Thanks anyway!", "Arnold Schwarzenegger isn't voluntarily leaving the Apprentice, he was fired by his bad (pathetic) ratings, not by me. Sad end to great show", "Crazy Joe Biden is trying to act like a tough guy. Actually, he is weak, both mentally and physically, and yet he threatens me, for the second time, with physical assault. He doesn’t know me, but he would go down fast and hard, crying all the way. Don’t threaten people Joe!", "I am happy to announce that the original Apprentice --which will offer job opportunities to those in need--is coming back.", Thank you so much. That's so nice. Isn't he a great guy. He doesn't get a fair press; he doesn't get it. It's just not fair. And I have to tell you I'm here, and very strongly here, because I have great respect for Steve King and have great respect likewise for Citizens United, David and everybody, and tremendous resect for the Tea Party. Also, also the people of Iowa. They have something in common. Hard-working people. They want to work, they want to make the country great. I love the people of Iowa. So that's the way it is. Very simple. With that said, our country is really headed in the wrong direction with a president who is doing an absolutely terrible job. The world is collapsing around us, and many of the problems we've caused. Our president is either grossly incompetent, a word that more and more people are using, and I think I was the first to use it, or he has a completely different agenda than you want to know about, which could be possible. In any event, Washington is broken, and our country is in serious trouble and total disarray. Very simple. Politicians are all talk, no action. They are all talk and no action. And it's constant; it never ends. And I'm a conservative, actually very conservative, and I'm a Republican. And I'm very disappointed by our Republican politicians. Because they let the president get away with absolute murder. You see always, oh we're going to do this, we're going to--. Nothing ever happens; nothing ever happens. You look at Obamacare. A total catastrophe and by the way it really kicks in in '16 and it is going to be a disaster. People are closing up shops. Doctors are quitting the business. I have a friend of mine who's a doctor, a very good doctor, a very successful guy. He said, I have more accountants than I have patients. And he needs because it is so complicated and so terrible and he's never had that before and he's going to close up his business. And he was very successful guy. But it's happening more and more. Look at Obamacare with a $5 billion website. I have many websites, many, many websites. They're all over the place. But for $10, okay? Now everything about Obamacare was a lie. It was a filthy lie. And when you think about it, lies, I mean are they prosecuted? Does anyone do anything? And what are the Republican politicians doing about it? He lied about the doctor, he lied about every aspect. You can keep your plan. And you've all heard that hundreds of times. That's like the real estate location, location. I don't even say it anymore because everybody goes location, location. But you have heard this about Obamacare. And it's disgraceful. It's a big, fat, horrible lie. Your deductibles are going through the roof. You're not going to get--unless you're hit by an army tank, you're not going to get coverage.''']

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
            # clear_screen()
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
            #clear_screen()
            return make_sentence(words)
        else:
            word = chosen_word
        words.append(word)
        key = (key[1], word)
        # clear the screen, we're done visualizing.  The next iteration will
        # visualize the next word being added, so let's make sure that the
        # screen is clear before then.
        #clear_screen()
    return make_sentence(words)

min_words = 10
# shuffle(trump_tweets)

# ! ONLY for Algorithm testing below; functions are being called in a separate file
# chains = make_chains(make_sentence(trump_tweets))
# text = make_text(chains, min_words)

# print(text)