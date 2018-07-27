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

console.log("Running Window Events Script");
window.addEventListener("keypress", e=> {
console.log(e.keyCode);


})

// insert a function that prints out the key code of a key pressed
let purpleBox = document.querySelector("#box6");
let tomatoBox = document.querySelector("#box7");

window.addEventListener('keypress', e => {
  let key = e.which || e.keyCode;
  if (key == 99) {
    purpleBox.classList.add("smaller");
  } else if (key == 115) {
    purpleBox.classList.remove("smaller");
  }
})

let h = window.innerHeight;
