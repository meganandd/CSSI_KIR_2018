// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Use querySelector to store the div in a variable.

// function display (selected) {
//   if (selected == 'red') {
//     let texttoshow = "Red";
//   } else if (selected == 'blue') {
//     let texttoshow = "Blue";
//     }
//   document.getElementById("responseBox").innerHTML = texttoshow;
//   }

let bigBox = document.querySelector("#responseBox");
//bigBox.style.background = "red";
//bigBox.innerHTML = "Red";

colorStr = "";

function click(id) {
  if (id == "Red") {
    console.log("You clicked the red button!");
    bigBox.style.background = "red";
  } else if (id == "Green") {
    console.log("You clicked the green button!");
    bigBox.style.background = "green";
  } else {
    console.log("You clicked the blue button!");
    bigBox.style.background = "blue";
  }

  let showText = id;
  colorStr += showText + " ";
  bigBox.innerHTML = colorStr + "\n";
}

let redButton = document.querySelector('#red');

// Use addEventListener to respond to a click event.
redButton.addEventListener('click', e => {
  // console.log("You clicked the red button!");
  // document.getElementById("responseBox").style.background = "red";
  // // let showText = "Red";
  // // document.getElementById("responseBox").innerHTML = showText;
  // showText("Red");
  click("Red");
})

let greenButton = document.querySelector('#green');

greenButton.addEventListener('click', e=> {
  // console.log("You clicked the green button!");
  // document.getElementById("responseBox").style.background = "green";
  // // let showText = "Green";
  // // document.getElementById("responseBox").innerHTML = showText;
  // showText("Green");
  click("Green");
})

let blueButton = document.querySelector('#blue');

blueButton.addEventListener('click', e=> {
  // console.log("You clicked the blue button!");
  // document.getElementById("responseBox").style.background = "blue";
  // // let showText = "Blue";
  // // document.getElementById("responseBox").innerHTML = showText;
  // showText("Blue");
  click("Blue");
})

let clearButton = document.querySelector('#clear');

clearButton.addEventListener('click', e=> {
  document.getElementById("responseBox").style.background = "white";
  colorStr = "";
  let showText = "";
  document.getElementById("responseBox").innerHTML = showText;
})
