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

import webapp2
import os
import jinja2
from google.appengine.api import urlfetch
from google.appengine.ext import ndb
import json
from random import randint
from random import shuffle
from models import Question
import urlparse

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        index = randint(0, len(Question.query().fetch()) - 1)

        question = Question.query().fetch()[index].question
        correct_answer = Question.query().fetch()[index].correct_answer
        incorrect_answers = Question.query().fetch()[index].incorrect_answers

        all_answers = [correct_answer]
        for answer in incorrect_answers:
            all_answers.append(answer)

        shuffle(all_answers)

        trivia_dict = {
        "q" : question,
        "ca" : correct_answer,
        "ia" : incorrect_answers,
        "aa" : all_answers
        }

        questions_template = jinja_current_dir.get_template("templates/welcome.html")
        self.response.write(questions_template.render(trivia_dict))

class SeedPage(webapp2.RequestHandler):
    def get(self):
        result = urlfetch.fetch("https://opentdb.com/api.php?amount=10&encode=url3986").content
        json_result = json.loads(result)["results"]

        for q in json_result:
            question = q["question"]
            final_question = urlparse.unquote(question)

            correct_answer = q["correct_answer"]
            final_correct_answer = urlparse.unquote(correct_answer)

            incorrect_answers = q["incorrect_answers"]
            final_incorrect_answers = []
            for answer in incorrect_answers:
                final_incorrect_answers.append(urlparse.unquote(answer))

            new_question = Question(question = final_question,
            correct_answer = final_correct_answer,
            incorrect_answers = final_incorrect_answers)

            new_question.put()
        self.redirect("/")

# class PlayTriviaQuestion(webapp2.RequestHandler):
#      def get(self):
#          all_questions = Question.query().fetch()[index].question
#          correct_answer = Question.query().fetch()[index].correct_answer
#         incorrect_answers = Question.query().fetch()[index].incorrect_answers
#
#          all_answers = []
#          all_answers.append(correct_answer)
#              for answer in incorrect_answers:
#                  all_answers.append(answer)
#
#          shuffle(all_answers)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    #('/play-trivia', PlayTriviaQuestion),
    ('/seed-trivia-data', SeedPage),
], debug=True)
