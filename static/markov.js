// A Javascript Markov chain generator.

function makeChains(textString) {
    // Take input text as string; return dictionary?? of Markov chains.
    let chains = {};

    let words = textString.split(' ');
    for (let i = 0; i < words.length -2; i++) {
        let chainsKey = [words[i], words[i + 1]];
        let value = words[i + 2];
        if (!(chainsKey in chains)) {
            chains[chainsKey] = [];
        }
        chains[chainsKey].push(value);
        // console.log(chains);
    }
    return chains;
}

function makeMarkovText(chains, minLength) {
    let output_objects = [];
    
    // keys is a 'word pair' e.g. (word1, word2), acting as key in chains dict
    let keys = Object.keys(chains); 

    // select a random word from a list of keys from chains dict
    let random_location = Math.floor(Math.random() * keys.length);
    let key = keys[random_location].split(',');

    let generated_words = [key[0], key[1]];

    while (key in chains) {
        // Keep looping until we have a key that isn't in the chains
        // (which would mean it was the end of our original text).

        // Note: that for long texts this might mean it would run for a very long time
        let word_random_location = Math.floor(Math.random() * chains[key].length);
        let word = chains[key][word_random_location];
        generated_words.push(word);
        // Check if we only had one word as an option
        if (chains[key].length == 1) {
            // Then just add the new generated words as a single element list, to the output.
            output_objects.push([generated_words.join(' ') + '<br>']);
        } else {
            // First add the full sentence.
            output_list = [generated_words.join(' ') + '<br>']
            // Now add all the words.
            for (let i = 0; i < chains[key].length; i++) {
                output_list.push(chains[key][i] + '<br>');
            }
            // Add our output list of strings to the output_objects.
            output_objects.push(output_list);
        }
        key = [key[1], word];
        // We don't use 'word' after this, so it is safe to change it with pop()
        if ((generated_words.length > minLength) && (word.slice(-1) == '.')) {
            return output_objects;
//            return generated_words.join(' ');
        }
    }
    return output_objects;
}

function processTweets(tweetsText) {
    let jsMarkovChain = makeMarkovText(makeChains(tweetsText), 20);
    let i = 0;
    setInterval(function() {
        if (i >= jsMarkovChain.length) {
            clearInterval();
        }
        $('#markov-output-div').html(jsMarkovChain[i]);
        i += 1;
    }, 300);
}

$(function() {
    // console.log('final markov chain:');
    // let markovChain = makeMarkovText(makeChains(trumpTweets));
    // console.log(markovChain);

    // let d = $('#output-text');
    // d.text(markovChain);
})
