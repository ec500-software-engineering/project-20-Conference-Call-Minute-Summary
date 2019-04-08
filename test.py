from __future__ import print_function
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1

# If service instance provides API key authentication
service = SpeechToTextV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://stream.watsonplatform.net/speech-to-text/api',
    iam_apikey="4uC92CUZ5yS5sXxg7GROP0cC63O8wOR72jyj0yf8qTG-")

# with open(join(dirname(__file__), 'project-20-Conference-Call-Minute-Summary/happybirthday.mp3'),
#           'rb') as audio_file:
#     text = json.dumps(
#         service.recognize(
#             audio=audio_file,
#             content_type='audio/mp3',
#             timestamps=True,
#             ).get_result(),
#         indent=2)
#     print(type(text))
#     with open("project-20-Conference-Call-Minute-Summary/test.json",'w') as F:
#         F.write(text)

