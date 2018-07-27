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

let customer_name;
let balance;
let logged_in = false;
let password;

//Task 1 & 2
function openAccount(name, pass, startBalance = 0) {
  balance = 0;
  balance += startBalance;
  // Set the value for customer_name equal to name below
  customer_name = name;
  password = pass;
  return (customer_name + " has opened a new account with a balance of $" + balance + "."); //write the statment you need to return here
}

//Extension
function logIn(name, pass) {
  if (name == customer_name && pass == password) {
    logged_in = true;
    return (customer_name + " has logged in.");
  } else {
    logged_in = false;
    return ("Incorret log in.")
  }
}

function logOut() {
  logged_in = false;
  return (customer_name + " has logged out.");
}

//Task 3
function deposit (value) {
  // update the value of balance
  if (logged_in == true) {
    balance += value;
    //return the correct statement
    return (customer_name + " has deposited $" + value + ". " + customer_name + "'s total balance is $" + balance + ".");
  } else {
    return ("User must log in.")
    }
  }

//Task 4 & 5
function withdraw(value) {
  if (logged_in == true) {
    if (value > balance) {
      let difference = value - balance;
      return ("Sorry, " + customer_name + ", you do not have enough money in your account. You need " + difference + " more dollars.");
    } else {
      balance -= value;
      //return the correct statement
      return (customer_name + " has withdrawn $" + value + ". " + customer_name + " has $" + balance + " remaining.");
    }
  } else {
    return ("User must log in.")
  }
}

console.log(openAccount("Megan", "cool", 100));
console.log(logIn("Megan", "cool"));
console.log(logOut());
console.log(deposit(40));
console.log(withdraw(180));

// Write your script below
console.log(openAccount("Annie", "smart", 300));
console.log(deposit(50));
console.log(withdraw(500));
console.log(logIn("Annie", "smart"));
