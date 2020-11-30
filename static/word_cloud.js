// This file contains functions to create a word cloud using the D3 API.

function applyScaleFactor(originalFontSize, scaleFactor) {
    let maxFontSize = 60;
    scaleFunction = d3.scaleLog().domain([1,50]).range([10, maxFontSize]);
    return originalFontSize * scaleFunction(scaleFactor);
  }
  
  function createWordListWithSize(words) {
    // Dictionary of word/wordFrequency (keys/values).
    let wordsFrequencyDict = {}
    let fontScale = 10;
  
    // Put the words in a dictionary first.
    for (let word of words) {
      // In case we have seen this word already
      if (word in wordsFrequencyDict) {
        // Increment our word count for that word.
        wordsFrequencyDict[word]++;
      } else {
        // Else, create a key/value for the word, with the value
        // being set to 1, since we have only seen the word once till now
        wordsFrequencyDict[word] = 1;
      }
    }
    // Convert the dictionary to a list of objects, with data and size now.
    returnArray = [];
  
    // Iterate over the KEYS of the dict, which are words
    for (let word in wordsFrequencyDict) {
      returnArray.push({word: word, fontSize: applyScaleFactor(wordsFrequencyDict[word], fontScale)});
    }
  
    return returnArray;
  }
  
  function createCloudFromWords(wordsText, outputDivId, scaleType = 'logarithmic') {
    myWords = createWordListWithSize(wordsText.split(' '));
  
    // set the dimensions and margins of the graph
    var margin = {top: 10, right: 10, bottom: 10, left: 10},
        width = 450 - margin.left - margin.right,
        height = 450 - margin.top - margin.bottom;
  
    // append the svg object to the body of the page
    var svg = d3.select(outputDivId).append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
      .append("g")
        .attr("transform",
              "translate(" + margin.left + "," + margin.top + ")");
  
    // Constructs a new cloud layout instance. It run an algorithm to find the position of words that suits your requirements
    var layout = d3.layout.cloud()
      .size([width, height])
      .words(myWords.map(function(d) { return {text: d.word, fontSize: d.fontSize}; }))
      .padding(10)
      .rotate(0)
      .fontSize(function(d) { console.log('returning size: ' + String(d.fontSize)); return d.fontSize; })
      .on("end", draw);
    layout.start();
  
    // This function takes the output of 'layout' above and draw the words
    // Better not to touch it. To change parameters, play with the 'layout' variable above
    function draw(words) {
      svg
        .append("g")
          .attr("transform", "translate(" + layout.size()[0] / 2 + "," + layout.size()[1] / 2 + ")")
          .selectAll("text")
            .data(words)
          .enter().append("text")
            .style("font-size", function(d) { return d.fontSize; })
            .attr("text-anchor", "middle")
            .style("font-family", "Impact")
            .attr("transform", function(d) {
              return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
            })
            .text(function(d) { return d.text; });
    }
  }
  