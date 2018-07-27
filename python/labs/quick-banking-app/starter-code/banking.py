#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(self, label, balance):
        self.label = label
        self.balance = balance
    pass

    def __str__(self):
        labelInfo = "Label: " + self.label
        balanceStatus = "Balance: " + str(self.balance)
        return labelInfo + " " + balanceStatus

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            return self.balance
        elif withdraw_amount < 0:
            return self.balance
        else:
            self.balance -= withdraw_amount
            return self.balance

    def deposit(self, deposit_amount):
        if deposit_amount < 0:
            return self.balance
        else:
            self.balance += deposit_amount
            return self.balance

    def rename(self, newLabel):
        if newLabel == "":
            return self.label
        else:
            self.label = newLabel
            return self.label

    def transfer(self, dest_account, amount):
        if amount > dest_account.balance or amount < 0:
            return self.balance
        else:
            dest_account.balance -= amount
            self.balance += amount
            return self.balance
