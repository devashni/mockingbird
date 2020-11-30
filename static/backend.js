// This file contains functions to talk to our flask backend.

// This function will make a call to our flask backend via
// a http GET request. We will provide the username as the parameter
// to the request, the return value from the request will be the full
// text of all the tweets for the provided username.
function getTweetsFromBackend(usernane, resultCallback) {
    $.get('http://0.0.0.0:5000/gettweets/' + usernane, resultCallback);
}
