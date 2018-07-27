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
import json
import random
from random import shuffle
from random import randint

jinja_current_dir = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        api_key = "0WJYmD3THimcyDaPouOa0IlLFmnhD2WC"
        giphy_endpoint = "http://api.giphy.com/v1/gifs/search?q=ocean&api_key=" + api_key
        response = urlfetch.fetch(giphy_endpoint).content
        json_response = json.loads(response)
        index = randint(0, len(json_response["data"]) - 1)
        gif_url = json_response["data"][index]["images"]["original"]["url"]

        self.response.write("<img src='{}'/>".format(gif_url))

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
