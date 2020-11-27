
// A Javascript Markov chain generator.

function makeChains(textString) {
    // Take input text as string; return dictionary of Markov chains.

    //e.g chainsDict = {["A","witch!"]:["A", "A", "We’ve", "Burn",“You"], .....}
    let chainsDict = {};

    let words = textString.split(' ');
    for (let i = 0; i < words.length -2; i++) {
        let chainsKey = [words[i], words[i + 1]];
        let chainsValue = words[i + 2];
        if (!(chainsKey in chainsDict)) {
            chainsDict[chainsKey] = [];
        }
        chainsDict[chainsKey].push(chainsValue);
    }
    // console.log(chainsDict);
    return chainsDict;
}
//////////////////////////////////////////////////////////////////////////////////
function makeMarkovText(chainsDict, minLength) {
    let outputString = [];
    
    // keys is an array of 'word-pair' strings acting as key in chainsDict
    // e.g. keys = ["Whoa,there!",
    //              "there!,Halt!",
    //              "Halt!,Who",
    //              "Who,goes",
    //              "goes,there?"]
    let keys = Object.keys(chainsDict); 

    // select a random word from a list of keys from chainsDict
    let randomLocation = Math.floor(Math.random() * keys.length); //random_location is the 'index' of key in keys list.
    let key = keys[randomLocation].split(','); // e.g. key = ["bridge.", "Then"]

    // Starting out (below) generatedWords is same as the key, but more words are added to the arrays in the while loop below
    let generatedWords = [key[0], key[1]]; 

    while (key in chainsDict) {
        // Keep looping until we have a key that isn't in the chains
        // (which would mean it was the end of our original text).

        // Note: that for long texts this might mean it would run for a very long time
        let wordRandomLocation = Math.floor(Math.random() * chainsDict[key].length);
        let word = chainsDict[key][wordRandomLocation];
        generatedWords.push(word);

        let outputString = outputString.push([generated_words.join(' ')]

        // // Check if we only had one word as an option
        // if (chainsDict[key].length == 1) {
        //     // Then just add the new generated words as a single element list, to the output.
        //     outputString.push([generatedWords.join(' ') + '<br>']);
        // } 
        if (chains[key].length > 1) {
            // // First add the full sentence.
            // outputList = [generatedWords.join(' ') + '<br>']
            // // Now add all the words.
            for (let i = 0; i < chainsDict[key].length; i++) {
                outputList.push('<br>' + chainsDict[key][i] + '<br>');
            }
            // Add our outputList of strings to the outputString.
            outputString.push(outputList);
        }
        key = [key[1], word];
        // We don't use 'word' after this, so it is safe to change it with pop()
        if ((generated_words.length > minLength) && (word.slice(-1) == '.')) {
            return outputString;
            // return generated_words.join(' ');
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
