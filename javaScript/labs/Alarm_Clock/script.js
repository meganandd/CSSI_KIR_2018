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

console.log("script is running...");

// function Basic_Alarm(alarmMessage){
//   return alarmMessage;
// }
// console.log(Basic_Alarm("My alarm!"));

//Task 1:
function My_Alarm(wakeUpTime) {
  return ("Hey, Megan, wake up! It's " + wakeUpTime + ".");
}
console.log(My_Alarm("7:00am"));

//Task 2
function Mom_Alarm(wakeUpTime) {
  return ("Hey, Mom, wake up! It's " + wakeUpTime + ".");
}
console.log(Mom_Alarm("6:00am"));

//Task 3
function Family_Alarm(wakeUpTime, familyMember) {
  return ("Hey, " + familyMember + ", wake up! It's " + wakeUpTime + ".");
}
console.log(Family_Alarm("6:30am", "Ryan"));

//Task 4
function Important_Alarm(message) {
  return (message.toUpperCase());
}
console.log(Important_Alarm("wake up, wake up, wake UP!!"));

//Task 5
function Snooze_Alarm(numTime) {
  return ("The alarm for " + numTime + " has been changed to " + (numTime + 1) + ".");
}
console.log(Snooze_Alarm(6));

//Extension
function Multi_Alarm(numPeople) {
  var count;
  for (count = 0; count < numPeople; count++) {
    console.log("Wake Up!");
  }
}
console.log(Multi_Alarm(9));
