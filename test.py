from __future__ import print_function
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
import threading

# If service instance provides API key authentication
service = SpeechToTextV1(
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://stream.watsonplatform.net/speech-to-text/api',

# service = SpeechToTextV1(
#     username='YOUR SERVICE USERNAME',
#     password='YOUR SERVICE PASSWORD',
#     url='https://stream.watsonplatform.net/speech-to-text/api')

# models = service.list_models().get_result()
# print(json.dumps(models, indent=2))
#
# model = service.get_model('en-US_BroadbandModel').get_result()
# print(json.dumps(model, indent=2))

with open(join(dirname(__file__), 'project-20-Conference-Call-Minute-Summary/happybirthday.mp3'),
          'rb') as audio_file:
    text = json.dumps(
        service.recognize(
            audio=audio_file,
            content_type='audio/mp3',
            timestamps=True,
            ).get_result(),
        indent=2)
    print(type(text))
    with open("project-20-Conference-Call-Minute-Summary/test.json",'w') as F:
        F.write(text)
# 
# # Example using websockets
# class MyRecognizeCallback(RecognizeCallback):
#     def __init__(self):
#         RecognizeCallback.__init__(self)
#
#     def on_transcription(self, transcript):
#         print(transcript)
#
#     def on_connected(self):
#         print('Connection was successful')
#
#     def on_error(self, error):
#         print('Error received: {}'.format(error))
#
#     def on_inactivity_timeout(self, error):
#         print('Inactivity timeout: {}'.format(error))
#
#     def on_listening(self):
#         print('Service is listening')
#
#     def on_hypothesis(self, hypothesis):
#         print(hypothesis)
#
#     def on_data(self, data):
#         print(data)
#
# # Example using threads in a non-blocking way
# mycallback = MyRecognizeCallback()
# audio_file = open(join(dirname(__file__), '../resources/speech.wav'), 'rb')
# audio_source = AudioSource(audio_file)
# recognize_thread = threading.Thread(
#     target=service.recognize_using_websocket,
#     args=(audio_source, "audio/l16; rate=44100", mycallback))
# recognize_thread.start()