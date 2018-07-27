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

console.log("Running Click Events Script");
let redBox = document.querySelector("#box1");
let pinkBox = document.querySelector("#box2");
let orangeBox = document.querySelector("#box3");
let yellowBox = document.querySelector("#box4");
let blueBox = document.querySelector("#box5");

redBox.addEventListener('click', e => {
  redBox.style.background = "red";
  pinkBox.style.background = "red";
  orangeBox.style.background = "red";
})

pinkBox.addEventListener('click', e => {
  pinkBox.style.background = "pink";
  redBox.style.background = "pink";
  orangeBox.style.background = "pink";
})

orangeBox.addEventListener('click', e => {
  orangeBox.style.background = "orange";
  redBox.style.background = "orange";
  pinkBox.style.background = "orange";
})

yellowBox.addEventListener('click', e => {
  yellowBox.classList.toggle("active");
})

blueBox.addEventListener('click', e => {
  blueBox.classList.toggle("active");
})
