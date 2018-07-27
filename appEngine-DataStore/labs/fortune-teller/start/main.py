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

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import random
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list = ['Tomorrow, you will meet a life-changing new friend.',
                  'Fame and Instagram followers are headed your way.',
                  'On the Tuesday after next, an odd meeting will lead to a new opportunity.',
                  'Despite dry skies, bring an umbrella tomorrow.',
                  'A thrilling time is in your immediate future.',
                  'Someone has Googled you recently.',
                  'Stay alert. You will be part of a rescue mission.',
                  'You will beat Watson in a game of Jeopardy. Start studying though.']
    random_fortune = random.choice(fortune_list)
    return(random_fortune)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        # str = get_fortune()
        # self.response.write(str)
        start_template = JINJA_ENVIRONMENT.get_template('templates/fortune_start.html')
        self.response.write(start_template.render())

    def post(self):
        random_fortune = get_fortune()
        user_astro_sign = self.request.get("user_astrological_sign")

        the_variable_dict = {"sign" : user_astro_sign,
        "fortune" : random_fortune}

        results_template = JINJA_ENVIRONMENT.get_template('templates/fortune-results.html')
        self.response.write(results_template.render(the_variable_dict))

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/predict', FortuneHandler), #maps '/predict' to the FortuneHandler
    #('/farewell', GoodbyeHandler),
], debug=True)

# class HelloHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('Hello World. Welcome to the root route of my app')
#
# class GoodbyeHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.write('My response is Goodbye World')
