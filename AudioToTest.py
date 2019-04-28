from __future__ import print_function
import json
from ibm_watson import SpeechToTextV1
import time


class AudioToTest():
    def __init__(self):
        # If service instance provides API key authentication
        self.service = SpeechToTextV1(
            # url is optional, and defaults to the URL below. Use the correct URL for your region.
            url='https://stream.watsonplatform.net/speech-to-text/api',
            iam_apikey="")
        #print('debug1')

    def recognize(self, path:str):
        #print('debug2')
        with open(path,
                  'rb') as audio_file:
            text = json.dumps(
                self.service.recognize(
                    audio=audio_file,
                    content_type='audio/wav',
                    smart_formatting=False,
                    max_alternatives=1,
                    timestamps=True,
                    ).get_result(),
                indent=2)
            #print(text)
            with open("./"+path.split("/")[-1]+".json", 'w') as F:
                F.write(text)
        #print('debug3')

    def openjson(self, path):

        js = open(path)
        dic = json.loads(js.read())
        print(dic)
        full_path = str(path).strip('test.json') + 'TextRank/words/text.txt'
        file = open(full_path, 'w')
        for i in dic['results']:
            for j in i['alternatives']:

                file.write(j['transcript'])
        file.close()
        return dic['results'][0]['alternatives'][0]['transcript']

    def audiojson(self,path):
        js = open(path)
        dic = json.loads(js.read())
        ret = ""
        print(dic)
        for i in dic['results']:
            for j in i['alternatives']:
                print(j['transcript'])
                ret = ret + j['transcript']
        return ret
