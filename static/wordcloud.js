// This file contains functions to create a word cloud using the D3 API.

function applyScaleFactor(wordFrequency, frequencyDomainMax, scaleType) {
  let minFontSize = 20;
  let maxFontSize = 100;
  var scaleFunction = null;
  if (scaleType == 'logarithmic') {
    scaleFunction = d3.scaleLog().domain([1, frequencyDomainMax]).range([minFontSize, maxFontSize]);
  } else {
    scaleFunction = d3.scaleLinear().domain([1, frequencyDomainMax]).range([minFontSize, maxFontSize]);
  }
  return scaleFunction(wordFrequency);
}

function acceptWord(word) {
  // include: I, me, she, he, you, not
  // get rid of integers as well
  const dntIncludeWords = ['a','to', 'of', 'in', 'it', 'is', 'as', 'at',
                          'be', 'so', 'on', 'an', 'or', 'do', 'if', 'up',
                          'by', 'my', 'the', 'and', 'are', 'for', 'but',
                          'had', 'has', 'was', 'all', 'any', 'one', 'out',
                          'his', ' her', 'and', 'too', 'from', ',', '_', '-', '!', '?', '.', '—', '–'];

  const dontStartWith = ['http', '@', '#', '$', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'];

  if (dntIncludeWords.includes(word)) {
    return false;
  } else if (String(parseInt(word)) === word ) {
    return false;
  }
  
  for (dontStart of dontStartWith) {
    // console.log('--begin--');
    // console.log('|' + word + '|');
    // console.log('|' + dontStart + '|');
    // console.log('--end--');
    if (word.startsWith(dontStart)) {
      // console.log('returning false!');
      return false;
    }
  }

  if (word.trim().length == 0) {
    return false;
  }

  return true;
}

function createWordListWithSize(words, scaleType) {
  console.log('Creating list for words of length: ' + String(words.length));
  // Dictionary of word/wordFrequency (keys/values).
  let wordsFrequencyDict = {};
 
  // Put the words in a dictionary first. Save the highest frequency seen
  let highestFrequency = 0;
  for (let word of words) {
    // dntIncludeWords from the list in the word cloud
    word = word.toLowerCase();
    if (acceptWord(word)) {
      // In case we have seen this word already
      if (word in wordsFrequencyDict) {
        // Increment our word count for that word.
        wordsFrequencyDict[word]++;
      } else {
        // Else, create a key/value for the word, with the value
        // being set to 1, since we have only seen the word once till now
        wordsFrequencyDict[word] = 1;
      }
      // Update highest seen frequency.
      if (wordsFrequencyDict[word] > highestFrequency) {
        highestFrequency = wordsFrequencyDict[word];
      }
  }
  }
  // Convert the dictionary to a list of objects, with data and size now.
  returnArray = [];

  // Iterate over the KEYS of the dict, which are words
  for (let word in wordsFrequencyDict) {
    returnArray.push({
      word: word,
      fontSize: applyScaleFactor(wordsFrequencyDict[word], highestFrequency, scaleType),
    });
  }

  return returnArray;
}

function createWordCloudWithName(sourceName, wordsText,
  outputDivId,
  scaleType = "logarithmic") {

    let wcDivId = sourceName.slice(1) + String(Math.floor(Math.random() * 100)) +'Id';
    // Create a div to contain the source name and the word cloud
    let newDiv = $('<div></div>');
    newDiv.addClass('single-word-cloud-container');
    $(outputDivId).append(newDiv);

    let sourceNameLabel = $('<label>' + sourceName + ' (' + scaleType + ')</label>');
    newDiv.append(sourceNameLabel);

    let wcDiv = $('<div id="' + wcDivId + '"></div>');
    newDiv.append(wcDiv);

    createCloudFromWords(wordsText, '#' + wcDivId, scaleType);
}

// ! DONOT touch this function anymore
function createCloudFromWords(
  wordsText,
  outputDivId,
  scaleType = "logarithmic") {
  myWords = createWordListWithSize(wordsText.split(" "), scaleType);

  // set the dimensions and margins of the graph
  var margin = { top: 10, right: 10, bottom: 10, left: 10 },
    width = 450 - margin.left - margin.right,
    height = 450 - margin.top - margin.bottom;

  // append the svg object to the body of the page
  var svg = d3
    .select(outputDivId)
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  // Constructs a new cloud layout instance. It run an algorithm to find the position of words that suits your requirements
  var layout = d3.layout
    .cloud()
    .size([width, height])
    .words(
      myWords.map(function (d) {
        return { text: d.word, fontSize: d.fontSize };
      })
    )
    .padding(10)
    .rotate(0)
    .fontSize(function (d) {
      return d.fontSize;
    })
    .on("end", draw);
  layout.start();

  // This function takes the output of 'layout' above and draw the words
  // ! Better not to touch it. To change parameters, play with the 'layout' variable above
  function draw(words) {
    svg
      .append("g")
      .attr(
        "transform",
        "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")"
      )
      .selectAll("text")
      .data(words)
      .enter()
      .append("text")
      .style("font-size", function (d) {
        return d.fontSize;
      })
      .attr("text-anchor", "middle")
      .style("font-family", "Impact")
      .attr("transform", function (d) {
        return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
      })
      .text(function (d) {
        return d.text;
      });
  }
}
