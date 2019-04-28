import os
from google.cloud import translate
class translation:
    def __init__(self):
        self.translate_client = translate.Client()

    def translate(self,text,target):
        return self.translate_client.translate(text,target_language=target)
