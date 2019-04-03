import json
js = open("project-20-Conference-Call-Minute-Summary/test.json")
dic = json.loads(js.read())
print(dic['results'][0]['alternatives'][0]['transcript'])
