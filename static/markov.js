// ! A Javascript Markov Chain Generator, and Visualizer

function makeChains(textString) {
  // Take input text as string; return dictionary of Markov chains.

  //e.g chainsDict = {["A","witch!"]:["A", "A", "We’ve", "Burn",“You"], .....}
  // keys = ["A","witch!"]
  // value i.e. chainsDict[["A","witch!"]] = ["A", "A", "We’ve", "Burn",“You"]
  let chainsDict = {};

  let words = textString.split(" ");
  for (let i = 0; i < words.length - 2; i++) {
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
  let key = keys[randomIndex].split(","); // e.g. key = ["bridge.", "Then"]

  // Starting out (below) generatedWords is same as the key, but more words are added to the array in the while loop below
  let generatedWords = [key[0], key[1]];

  while (key in chainsDict) {
    // Keep looping until we have a key that isn't in the chainsDict
    // (which would mean it was the end of our original text).
    // Note: that for long texts this might mean it would run for a very long time

    // value i.e. chainsDict[["A","witch!"]] = ["A", "A", "We’ve", "Burn",“You"]
    let nextWordRandomIndex = Math.floor(
      Math.random() * chainsDict[key].length
    );
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
    if (generatedWords.length > minLength && nextWord.slice(-1) == ".") {
      return outputSteps;
    }
  }
  return outputSteps;
}

function rejectChain(steps, minLength, maxLength) {
  if (steps.length < minLength) {
    return true;
  }

  if (steps.length > maxLength) {
      return true;
  }

  for (step of steps) {
    if (step.length > 2) {
      // We found at least one multiple word step, do not reject chain.
      console.log(
        "Found a choice word!" +
          String(step[0]) +
          " - " +
          String(step[1]) +
          " - " +
          String(step[2])
      );
      return false;
    }
  }
  // We didn't find any words that weren't choices, so reject chain.
  return true;
}

// This function returns the steps of execution of a Markov chain algorith that is
// run on the given 'text'. The algorithm will be run till the output string reaches minLength.
//
function returnStepsOfMarkovExecution(textString, minLength, maxLength) {
  // e.g. steps = [['I', 0],['am',0],['smart', 'dumb', 'crazy',3],['person',0],['and', 'but',1],['cute.',0]]

  let chainsDict = makeChains(textString);
  do {
    var steps = makeMarkovText(chainsDict, minLength);
  } while (rejectChain(steps, minLength, maxLength));
  return steps;
}

// This function will add a child div to 'parentDiv'.
// The text of the child div will be set to 'divText'.
// create 'newDiv' if there is just one element in steps[i]
function addTextDivAsChild(parentDivId = "#markov-div", divText) {
  let newDiv = $('<div id="divID">' + divText + "</div>");
  newDiv.addClass("one-word");
  $(parentDivId).append(newDiv);
}

// create 'newDiv2' if there are MORE than 1 elements/words in steps[i]
function addWordsToOutputDiv(parentDivId, wordArray, chosenWordIndex) {
  let divHtml = "";
  for (let i = 0; i < wordArray.length; i++) {
    if (i === chosenWordIndex) {
      divHtml +=
        "<div " +
        'class="multi-word"' +
        ">" +
        "<strong>" +
        wordArray[i] +
        "</strong>" +
        "</div>";
    } else {
      divHtml += "<div " + 'class="multi-word"' + ">" + wordArray[i] + "</div>";
    }
  }

  const maxWords = 5;
  const wordSizeEm = 3.0;
  const paddingFromTop = 0.8;
  marginFromTop =
    (maxWords - (chosenWordIndex + 1)) * wordSizeEm + paddingFromTop;
  //console.log('chosenWordsIndex is ' + String(chosenWordIndex));    marginFromTop = ((maxWords - chosenWordIndex) * wordSizeEm) + minPaddingEm;
  let containerDivStyle = "margin-top: " + marginFromTop + "em;";
  let containerDiv = $(
    '<div id="multi-word-container" style="' +
      containerDivStyle +
      '">' +
      divHtml +
      "</div>"
  );
  // let newDiv2 = $('<div id="divID">' + divTextArray + '</div>').css("color", "red");
  // Each word takes 2em space, so if we have
  $(parentDivId).append(containerDiv);
}

// ! This function animates/visualizes the steps of a markov chain algorithm execution run.
function animateStepsOfMarkovChain(parentDivId, steps, intervalMs, enableButtonsCallback) {
  // console.log('Calling setInterval!');
  let i = 0;
  let lenSteps = steps.length;
  // let lenStep = steps[i].length //len of single array element, i.e. steps[i]

  //this point onwards acts like a loop, which stops executing at set interval once i>=lenSteps
  let timer = setInterval(function () {
    // Create a copy of the input, don't change it.
    let step = steps[i].slice();
    let indexOfChosenWord = step.pop();
    if (step.length > 1) {
      addWordsToOutputDiv(parentDivId, step, indexOfChosenWord);
    } else {
      addTextDivAsChild(parentDivId, step[0]);
    }
    i += 1;
    if (i >= lenSteps) {
      clearInterval(timer);
      enableButtonsCallback();
    }
  }, intervalMs);
}

function printStepsOfMarkovChain(parentDivId, steps) {
  for (step of steps) {
    let indexOfChosenWord = step.slice(-1);
    addTextDivAsChild(parentDivId, step[indexOfChosenWord]);
  }
}

function saveChain(tweetsSource, steps) {
  let chain = "";
  for (step of steps) {
    let indexOfChosenWord = step.slice(-1);
    chain += step[indexOfChosenWord] + " ";
  }
  localStorage.currentMarkovChain =
    "<strong>" + tweetsSource + ": </strong>" + chain.slice(0, -1);
}

function acceptWordMarkov(word) {
  const dntIncludeWords = [
    ",",
    "_",
    "-",
    "!",
    "?",
    ".",
    "—",
    "–",
  ];

  const dontStartWith = [
    "http",
    "@",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
  ];

  if (dntIncludeWords.includes(word)) {
    return false;
  } else if (String(parseInt(word)) === word) {
    return false;
  }

  for (dontStart of dontStartWith) {
    if (word.startsWith(dontStart)) {
      return false;
    }
  }

  if (word.trim().length == 0) {
      return false;
  }

  return true;
}

function cleanTextForMarkov(tweetText) {
    let words = tweetText.split(' ');
    let returnString = '';
    for (word of words) {
        if (acceptWordMarkov(word)) {
            returnString += word + ' ';
        }
    }
    return returnString;
}

// ! Main function - this gets loaded, every time I reload the page.
function processTweets(tweetsSource, tweetsText, outputDivId, minLength = 10, maxLength = 30, intervalMs = 100, enableButtonsCallback) {
  // console.log('In the main function!');
  let steps = returnStepsOfMarkovExecution(cleanTextForMarkov(tweetsText), minLength, maxLength);
  console.log(steps);
  let checkBoxJqueryObject = $("#viz-checkbox");
  if (checkBoxJqueryObject.prop("checked")) {
    animateStepsOfMarkovChain(outputDivId, steps, intervalMs, enableButtonsCallback);
  } else {
    printStepsOfMarkovChain(outputDivId, steps);
    enableButtonsCallback();
  }

  saveChain(tweetsSource, steps);
}
