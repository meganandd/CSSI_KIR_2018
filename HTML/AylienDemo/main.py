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
from models import Dream
from aylienapiclient import textapi

#remember, you can get this by searching for jinja2 google app engine
jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        # text = 'John is a very good football player'
        # sentiment = client.Sentiment({'text': text})
        # print sentiment

        start_template = jinja_current_dir.get_template("templates/welcome.html")
        self.response.write(start_template.render())

    def post(self):
        client = textapi.Client("f02d5bcf", "f1bd4de2fe8c8bf3ea53946580b1afd4")
        dream = self.request.get('user-dream')
        sentiment = client.Sentiment({'text': dream})
        dream_sentiment = sentiment["polarity"]
        print dream_sentiment

        #put into database (optional)
        dream_record = Dream(dream_text = dream, sentiment = dream_sentiment)
        dream_record.put()

        #pass to the template via a dictionary
        dream_info = { "dream_summary" : dream,
        "sentiment" : dream_sentiment
        }
        end_template = jinja_current_dir.get_template("templates/results.html")
        self.response.write(end_template.render(dream_info))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    # ('/showfavs', ShowFoodHandler)
], debug=True)
