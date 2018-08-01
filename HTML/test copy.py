import requests
import json

url = "https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2017-09-21&text=Sometimes, the greatest adventures in life are internal. This work represents such an adventure. It's a journey through the unseen dimensions of mind and spirit. I can attest to the reality of the events described herein. They are not fictional. The journey isn't new. It's been the quest of millions of persons for thousands of years. But, like the uniqueness of one's fingerprints or DNA, each life story is unique."

# headers = {
# "username" : "12b8c206-770b-4989-9909-2c1c625c9a8d",
# "password" : "nMHwFGhjTHIT"
# }

r = requests.get(url, auth=("12b8c206-770b-4989-9909-2c1c625c9a8d", "nMHwFGhjTHIT"))
# print r.text
json_result = json.loads(r.text)["document_tone"]["tones"][0]["tone_name"]
json_result2 = json.loads(r.text)["sentences_tone"][0]["tones"][0]["tone_name"]
# print json_result
print json_result2
