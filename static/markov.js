
// ! A Javascript Markov Chain Generator, and Visualizer 

function makeChains(textString) {
    // Take input text as string; return dictionary of Markov chains.

    //e.g chainsDict = {["A","witch!"]:["A", "A", "We’ve", "Burn",“You"], .....}
    // keys = ["A","witch!"]
    // value i.e. chainsDict[["A","witch!"]] = ["A", "A", "We’ve", "Burn",“You"]
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

function makeMarkovText(chainsDict, minLength) {
    let outputSteps = [];
    
    // keys is an array of 'word-pair' strings acting as key in chainsDict
    // e.g. keys = ["Whoa,there!",
    //              "there!,Halt!",
    //              "Halt!,Who",]
    let keys = Object.keys(chainsDict); 

    // select a random word from a list of keys from chainsDict
    let randomIndex = Math.floor(Math.random() * keys.length); //randomIndex is the 'index' of key in keys list.
    let key = keys[randomIndex].split(','); // e.g. key = ["bridge.", "Then"]

    // Starting out (below) generatedWords is same as the key, but more words are added to the array in the while loop below
    let generatedWords = [key[0], key[1]]; 

    while (key in chainsDict) {
        // Keep looping until we have a key that isn't in the chainsDict
        // (which would mean it was the end of our original text).
        // Note: that for long texts this might mean it would run for a very long time

        // value i.e. chainsDict[["A","witch!"]] = ["A", "A", "We’ve", "Burn",“You"]
        let nextWordRandomIndex = Math.floor(Math.random() * chainsDict[key].length); 
        let nextWord = chainsDict[key][nextWordRandomIndex]; //nextWord is the next word added to generatedWords array
        generatedWords.push(nextWord);

        //making a copy of chainsDict[key] using 'slice()', so we can modify it with 'push()' without changing the original markov chainDict
        let valueArray = chainsDict[key].slice(); 
        valueArray.push(nextWordRandomIndex);

        // outputString.push([nextWord]);
        // outputSteps.push(chainsDict[key]);
        outputSteps.push(valueArray);
        // sample outputSteps is an array containing array of chainsDict values + nextWordRandomIndex
        // e.g. steps = [['I', 0],['am',0],['smart', 'dumb', 'crazy',3],['person',0],['and', 'but',1],['cute.',0]]

        key = [key[1], nextWord];
        // We don't use 'nextWord' after this, so it is safe to change it with pop()/slice()
        if ((generatedWords.length > minLength) && (nextWord.slice(-1) == '.')) {
            return outputSteps;
        }
    }
    return outputSteps;
}

// This function returns the steps of execution of a Markov chain algorith that is
// run on the given 'text'. The algorithm will be run till the output string reaches minLength.
// 
function returnStepsOfMarkovExecution(textString, minLength) {
    // e.g. steps = [['I', 0],['am',0],['smart', 'dumb', 'crazy',3],['person',0],['and', 'but',1],['cute.',0]]

    let chainsDict = makeChains(textString);
    let steps = makeMarkovText(chainsDict, minLength);

    return steps;
}

// This function will add a child div to 'parentDiv'.
// The text of the child div will be set to 'divText'.
// create 'newDiv' if there is just one element in steps[i]
function addTextDivAsChild(parentDivId = '#markov-div', divText) {
    
    let newDiv = $('<div id="divID">' + divText +'</div>');
    newDiv.addClass('one-word');
    $(parentDivId).append(newDiv);
}

// create 'newDiv2' if there are MORE than 1 elements/words in steps[i]
function addWordsToOutputDiv(parentDivId, wordArray, chosenWordIndex) {

    let divHtml = ''
    for (let i=0; i<wordArray.length; i++){
        if (i === chosenWordIndex){
            divHtml += '<div ' + 'class="multi-word"' + '>' +'<strong>'+ wordArray[i] +'</strong>'+ '</div>';
        }
        divHtml += '<div ' + 'class="multi-word"' + '>' + wordArray[i] + '</div>';
    }

    let newDiv2 = $('<div id="divID">' + divHtml + '</div>');
    // let newDiv2 = $('<div id="divID">' + divTextArray + '</div>').css("color", "red");
    newDiv2.addClass('one-word');
    $(parentDivId).append(newDiv2);
}


// ! This function animates/visualizes the steps of a markov chain algorithm execution run.
function animateStepsOfMarkovChain(parentDivId, steps) {
    let interval = 500; // Interval in milliseconds.
    // console.log('Calling setInterval!');
    let i = 0;
    let lenSteps = steps.length
    // let lenStep = steps[i].length //len of single array element, i.e. steps[i]

    //this point onwards acts like a loop, which stops executing at set interval once i>=lenSteps
    let timer = setInterval(function() {
        let indexOfChosenWord = steps[i].pop();
        if ( (steps[i].length) > 2){
            addWordsToOutputDiv(parentDivId, steps[i], indexOfChosenWord);
        } else {
            addTextDivAsChild(parentDivId, steps[i]);
        }
        i += 1;
        if (i >= lenSteps) {
            clearInterval(timer);
        } 
    }, interval);
}

// ! Main function - this gets loaded, every time I reload the page.
function processTweets(tweetsText, minLength = 10) {
    // console.log('In the main function!');
    let steps = returnStepsOfMarkovExecution(tweetsText, minLength);
    console.log(steps);
    animateStepsOfMarkovChain('#markov-div', steps);
}
