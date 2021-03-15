import * as Plotly from 'plotly.js';

document.getElementById("submit").addEventListener("click", process_input);

// Configuring how to handle the API Requests
// function to handle success
function success() {
    var data = JSON.parse(this.responseText); //parse the string to JSON
    update_image(data['sentiment'])
    update_plot(data['probabilities'])
}

// function to handle error
function error(err) {
    console.log('Request Failed', err); //error details will be in the "err" object
}

var xhr = new XMLHttpRequest(); //invoke a new instance of the XMLHttpRequest
xhr.onload = success; // call success function if request is successful
xhr.onerror = error;  // call error function if request failed


function process_input() {
    var user_input = document.getElementById('user_input').value;
    // open a POST request
    xhr.open('POST', "http://127.0.0.1:8000/predict");
    xhr.send(JSON.stringify({'text': user_input})); // send the request to the server.
}

function update_plot(predicted_data){
    var layout = {  margin: {l: 25, r: 20, b: 25, t: 25, pad: 5 },
                    title: 'Probabilities',
                    font:{ family: 'Raleway, sans-serif'},
                }

    var data = [{predicted_data,
            x: Object.keys(predicted_data),
            y: Object.values(predicted_data),
            type: 'bar'
        }];
      Plotly.newPlot('myDiv', data, layout, {displayModeBar: false});
}

function update_image(sentiment){
    if (sentiment === "positive"){
        document.getElementById("imgClickAndChange").src = "assets/positive.png";
    }
    else if (sentiment === "neutral"){
        document.getElementById("imgClickAndChange").src = "assets/neutral.png";
    }
    else if (sentiment === "negative"){
        document.getElementById("imgClickAndChange").src = "assets/negative.png";
    }
}