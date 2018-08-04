# Copyright 2016 Google Inc.
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

import webapp2
import jinja2
import os
from model import Dream
import requests
import requests_toolbelt.adapters.appengine
from google.appengine.api import urlfetch
import json
import datetime
import operator

requests_toolbelt.adapters.appengine.monkeypatch()

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage (webapp2.RequestHandler):
    def get(self):
        home_template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(home_template.render())

class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = JINJA_ENVIRONMENT.get_template('templates/submit.html')
        self.response.write(welcome_template.render())

class ShowDreamHandler(webapp2.RequestHandler):
    def get(self):
        results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')
        #self.response.headers['Content-Type'] = 'text/plain'
        self.response.write(results_template.render(dream_dict))

    def post(self):
        results_template = JINJA_ENVIRONMENT.get_template('templates/results.html')

        dream_title = self.request.get("dream-title") #get the title from the respective input tag in submit.html
        dream_date = self.request.get("dream-date")
        dream_summary = self.request.get("dream-summary") #get the summary from the rescpetive input tag in submit.html
        url = "https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&text=" + dream_summary

        r = requests.get(url, auth=("12b8c206-770b-4989-9909-2c1c625c9a8d", "nMHwFGhjTHIT"))

        try:
            dream_sentiment = json.loads(r.text)["document_tone"]["tones"][0]["tone_name"]
        except IndexError:
            dream_sentiment = "None"

        dream = Dream(title=dream_title,
                    dream_date=dream_date,
                    dream_text=dream_summary,
                    dream_sentiment=dream_sentiment)

        dream.put()

        all_dreams = Dream.query().fetch()

        dream_dict = {"title" : dream_title,
        "date" : dream_date,
        "dream_summary" : dream_summary,
        "sentiment" : dream_sentiment,
        "all_dreams" : all_dreams}

        self.response.write(results_template.render(dream_dict))

class DreamDataHandler(webapp2.RequestHandler):
    def get(self):
        data_template = JINJA_ENVIRONMENT.get_template('templates/data.html')
        #Get occurance of each sentiment in all dreams in DataStore
        sentiments = []
        possible_sentiments = ["Fear", "Anger", "Joy", "Confident", "Analytical", "Sadness", "Tentative", "None"]

        vardict = {}
        for i in possible_sentiments:
            vardict[i] = 0
            vardict[i] = len(Dream.query().filter(Dream.dream_sentiment==i).fetch())

        #date frequency
        all_dates = []
        for dream in Dream.query().fetch():
            all_dates.append(dream.dream_date.split("-"))

        for entry in all_dates:
           for datepart in entry:
               datepart = int(datepart)

        new_all_dates = []
        for entry in all_dates:
            date_list = []
            for datepart in entry:
                date_list.append(int(datepart))
            new_all_dates.append(date_list)

        all_dates = new_all_dates

        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        weekdays = []
        for entry in all_dates:
            day = datetime.date(entry[0], entry[1], entry[2])
            weekdaynum = day.weekday()
            weekdays.append(days[weekdaynum])

        for day in days:
            vardict[day] = 0
            for d in weekdays:
                if d == day:
                    vardict[day] += 1

        #word frequency
        def get_stop_words():
            with open('stop-words.txt') as f:
                content = ' '.join(f.readlines()).replace('\n','').replace('\r','').lower()
                return content.split(' ')

        all_text = []

        for dream in Dream.query().fetch():
            all_text.append(dream.dream_text)

        word_count = {}

        words = []
        for text in all_text:
            words.append(text.split())

        for entry in words:
            for word in entry:
                 if not word in word_count:
                     word_count[word] = 0
                 word_count[word] += 1

        sorted_map = list(reversed(sorted(word_count.items(), key=operator.itemgetter(1))))

        sorted_words = [sort[0] for sort in sorted_map]
        print sorted_words

        top_words = []
        for word in sorted_words:
            if word.lower() not in get_stop_words():
                top_words.append(word)

        print top_words

        places = ["first", "second", "third", "fourth", "fifth"]
        # Fixed bug here -- add to TeamDream
        if len(top_words) < 5:
            for i in range(len(top_words)):
                vardict[places[i]] = top_words[i]
        else:
            for i in range(5):
                vardict[places[i]] = top_words[i]

        print vardict

        self.response.write(data_template.render(vardict))


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/submit', EnterInfoHandler),
    ('/showdream', ShowDreamHandler),
    ('/showdata', DreamDataHandler),
], debug=True)



# try:
#     dream_sentiment = json.loads(r.text)["document_tone"]["tones"][0]["tone_name"]
# except IndexError:
#     dream_sentiment = "Null"

# possible_sentiments = ["Fear", "Anger", "Joy", "Confident", "Analytical", "Sadness", "Tentative", "Null"]

# Sentiment Found:

# <img class="responsive-img" src="https://78.media.tumblr.com/c08ba1d8a62c75b85b9513eb9fb964fc/tumblr_p6k33vvoxd1vpf6ddo1_500.gif" alt="cloud"></br>
# <!-- http://pixelartmaker.com/art/91da7da795ae3b2.png -->

# <!DOCTYPE html>
#   <html>
#     <head>
#       <!--Import Google Icon Font-->
#       <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
#       <link href="https://fonts.googleapis.com/css?family=Questrial|Quicksand" rel="stylesheet">
#       <link rel="icon" type="image/png" href="https://www.scimagojr.com/img/journalicon.png">
#       <!--Import materialize.css-->
#       <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css">
#
#       <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.min.js"></script>
#
#       <!--Let browser know website is optimized for mobile-->
#       <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
#
#       <title>Dream Data</title>
#     </head>
#
#     <body style="background-color:#E4D0F2">
#
#       <nav>
#         <div class="nav-wrapper" style="font-family:Quicksand; background-color:#b39ddb">
#           <a href="#" class="brand-logo right">dreampad</a>
#           <ul id="nav-mobile" class="left hide-on-med-and-down">
#             <li id="mainPage"><a href="/">Home</a></li>
#             <li id="submitNav"><a href="/submit">Submit</a></li>
#             <li id="data"><a href="/showdata">Data</a></li>
#             <li id="all"><a href="/allDreams">Journal</a></li>
#             <li id="aboutUs"><a href="/AboutUs">About Us</a></li>
#           </ul>
#         </div>
#       </nav>
#
#       <br>
#       <div class="container">
#         <div class="row">
#           <div class="col s4 offset-s4">
#             <div class="card hoverable z-depth-2" style="background-color:#F0E6F2">
#               <div class="card-content black-text">
#                 <div class="counter col_fourth" style="background-color:#F0E6F2">
#                   <h2 class="timer count-title count-number" data-to={{ total }} data-speed="1500" style="text-align:center; font-family:Quicksand">></h2>
#                    <p style="text-align:center; font-family:Quicksand" class="count-text ">total dreams</p>
#                 </div>
#               </div>
#             </div>
#           </div>
#         </div>
#       </div>
#
#       <div class="container">
#         <div class="row">
#         <div class="col s12 m12">
#           <div class="card hoverable z-depth-2" style="background-color:#F0E6F2">
#             <div class="card-content white-text">
#               <span class="card-title black-text" style="font-family:Quicksand";>Sentiment Analysis Data</span>
#               <div class="container">
#                 <canvas id="sentimentChart" width="300" height="300"></canvas>
#               </div>
#             </div>
#           </div>
#         </div>
#       </div>
#       </div>
#
#       <div class="container">
#         <div class="row">
#         <div class="col s12 m12">
#           <div class="card hoverable z-depth-2" style="background-color:#F0E6F2">
#             <div class="card-content white-text">
#               <span class="card-title black-text" style="font-family:Quicksand";>Weekday Frequency Data</span>
#               <div class="container">
#                 <canvas id="dayChart" width="300" height="300"></canvas>
#               </div>
#             </div>
#           </div>
#         </div>
#       </div>
#       </div>
#
#       <div class="container">
#         <ul class="collection with-header hoverable z-depth-2" style="font-family:Quicksand";>
#             <li class="collection-header" style="background-color:#F0E6F2"><h4>Word Frequency</h4></li>
#             <li class="collection-item" style="background-color:#F0E6F2">1. {{ first }}</li>
#             <li class="collection-item" style="background-color:#F0E6F2">2. {{ second }}</li>
#             <li class="collection-item" style="background-color:#F0E6F2">3. {{ third }}</li>
#             <li class="collection-item" style="background-color:#F0E6F2">4. {{ fourth }}</li>
#             <li class="collection-item" style="background-color:#F0E6F2">5. {{ fifth }}</li>
#         </ul>
#       </div><!-- .container -->
#
#       <script>
#         let sentimentChart = document.getElementById("sentimentChart").getContext('2d');
#
#         let sentChart = new Chart(sentimentChart, {
#           type:"pie",
#           data:{
#             labels:["Analytical", "Anger", "Confident", "Fear", "Joy", "Sadness", "Tentative", "Null"],
#             datasets:[{
#               label: "Dream Sentiment",
#               data:[
#                 {{ Analytical }},
#                 {{ Anger }},
#                 {{ Confident }},
#                 {{ Fear }},
#                 {{ Joy }},
#                 {{ Sadness }},
#                 {{ Tentative }},
#                 {{ Null }},
#               ],
#               backgroundColor:[
#                 'rgba(245, 226, 79, 0.4)',
#                 'rgba(79, 99, 247, 0.4)',
#                 'rgba(181, 245, 79, 0.4)',
#                 'rgba(245, 143, 79, 0.4)',
#                 'rgba(143, 79, 245, 0.4)',
#                 'rgba(79, 181, 245, 0.4)',
#                 'rgba(227, 170, 170, 0.4)'
#               ],
#               borderWidth:2,
#               borderColor:"rgba(122, 122, 122, 0.4)",
#               hoverBorderWidth:3,
#             }],
#           },
#           options: {
#             legend:{
#               display:true,
#               position:"left"
#             }
#           },
#         });
#       </script>
#
#       <script>
#         let dayChart = document.getElementById("dayChart").getContext('2d');
#
#         let dChart = new Chart(dayChart, {
#           type:"bar",
#           data:{
#             labels:["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
#             datasets:[{
#               label: "# of Dreams",
#               data:[
#                 {{ Monday }},
#                 {{ Tuesday }},
#                 {{ Wednesday }},
#                 {{ Thursday }},
#                 {{ Friday }},
#                 {{ Saturday }},
#                 {{ Sunday }}
#               ],
#               backgroundColor:[
#                 'rgba(245, 226, 79, 0.4)',
#                 'rgba(79, 99, 247, 0.4)',
#                 'rgba(181, 245, 79, 0.4)',
#                 'rgba(245, 143, 79, 0.4)',
#                 'rgba(143, 79, 245, 0.4)',
#                 'rgba(79, 181, 245, 0.4)',
#                 'rgba(227, 170, 170, 0.4)'
#               ],
#               borderWidth:2,
#               borderColor:"rgba(122, 122, 122, 0.4)",
#               hoverBorderWidth:3,
#             }],
#           },
#           options: {},
#         });
#       </script>
#
#       <!--JavaScript at end of body for optimized loading-->
#       <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js"></script>
#
#       <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
#
#       <script type="text/javascript">
#       document.getElementById("submitNav").onclick = function () {
#          location.href = "/submit";
#        };
#
#       document.getElementById("mainPage").onclick = function () {
#          location.href = "/";
#        };
#
#       document.getElementById("data").onclick = function () {
#          location.href = "/showdata";
#        };
#
#       document.getElementById("all").onclick = function () {
#          location.href = "/allDreams";
#        };
#
#       document.getElementById("aboutUs").onclick = function () {
#          location.href = "/AboutUs";
#        };
#       </script>
#
#     </body>
#   </html>
#
# <style media="screen">
#
# .active {
#     background-color: grey;
# }
#
# #nav{
#   background-color: #212121  ;
#   width: 100%;
# }
# .box{
#   border : 1px black;
#   background-color: black;
#   float: none;
#   height: 100px;
#   width: 100px;
#   padding: 0px;
#   margin: 0px;
# }
#
# .box2{
#   border : 1px black;
#   /* background-color: white; */
#   float: none;
#   height: 400px;
#   width: 500px;
#   padding: 0px;
#   margin-left: 75px;
#   margin-top: 0;
#
# }
# #canvas-holder{
#   margin-left: 400px;
#   margin-top: 0px;
# }
#
# #canvas-holder1{
#   margin-top: 0;
# }
#
# .center-div{
#      margin: 0 auto;
#      width: 100px;
# }
#
# .boxed {
#   width: 320px;
#   height: 100px;
#   padding: 10px;
#   border: 1px solid purple;
#   margin-right: 270px;
#   margin-top: 200px;
#   border-radius: 10px;
#   float: right;
#   background-color: #E4D0F2;
#   color: black;
#   text-align: center;
# }
#
# .boxed2 {
#   width: 320px;
#   height: 100px;
#   padding: 10px;
#   border: 1px solid purple;
#   margin-right: 570px;
#   margin-top: 200px;
#   border-radius: 10px;
#   float: right;
#   background-color: #E4D0F2;
#   color: black;
#   text-align: center;
# }
# </style>
#
# <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
# <script>
# (function ($) {
# $.fn.countTo = function (options) {
#   options = options || {};
#
#   return $(this).each(function () {
#     // set options for current element
#     var settings = $.extend({}, $.fn.countTo.defaults, {
#       from:            $(this).data('from'),
#       to:              $(this).data('to'),
#       speed:           $(this).data('speed'),
#       refreshInterval: $(this).data('refresh-interval'),
#       decimals:        $(this).data('decimals')
#     }, options);
#
#     // how many times to update the value, and how much to increment the value on each update
#     var loops = Math.ceil(settings.speed / settings.refreshInterval),
#       increment = (settings.to - settings.from) / loops;
#
#     // references & variables that will change with each update
#     var self = this,
#       $self = $(this),
#       loopCount = 0,
#       value = settings.from,
#       data = $self.data('countTo') || {};
#
#     $self.data('countTo', data);
#
#     // if an existing interval can be found, clear it first
#     if (data.interval) {
#       clearInterval(data.interval);
#     }
#     data.interval = setInterval(updateTimer, settings.refreshInterval);
#
#     // initialize the element with the starting value
#     render(value);
#
#     function updateTimer() {
#       value += increment;
#       loopCount++;
#
#       render(value);
#
#       if (typeof(settings.onUpdate) == 'function') {
#         settings.onUpdate.call(self, value);
#       }
#
#       if (loopCount >= loops) {
#         // remove the interval
#         $self.removeData('countTo');
#         clearInterval(data.interval);
#         value = settings.to;
#
#         if (typeof(settings.onComplete) == 'function') {
#           settings.onComplete.call(self, value);
#         }
#       }
#     }
#
#     function render(value) {
#       var formattedValue = settings.formatter.call(self, value, settings);
#       $self.html(formattedValue);
#     }
#     });
#     };
#
#     $.fn.countTo.defaults = {
#       from: 0,               // the number the element should start at
#       to: 0,                 // the number the element should end at
#       speed: 1000,           // how long it should take to count between the target numbers
#       refreshInterval: 100,  // how often the element should be updated
#       decimals: 0,           // the number of decimal places to show
#       formatter: formatter,  // handler for formatting the value before rendering
#       onUpdate: null,        // callback method for every time the element is updated
#       onComplete: null       // callback method for when the element finishes updating
#     };
#
#     function formatter(value, settings) {
#       return value.toFixed(settings.decimals);
#     }
#     }(jQuery));
#
#     jQuery(function ($) {
#     // custom formatting example
#     $('.count-number').data('countToOptions', {
#     formatter: function (value, options) {
#       return value.toFixed(options.decimals).replace(/\B(?=(?:\d{3})+(?!\d))/g, ',');
#     }
#     });
#
#     // start all the timers
#     $('.timer').each(count);
#
#     function count(options) {
#     var $this = $(this);
#     options = $.extend({}, options || {}, $this.data('countToOptions') || {});
#     $this.countTo(options);
#     }
#     });
# </script>
#
