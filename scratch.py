import json
import GUI
js = open("./test.json")
dic = json.loads(js.read())
# print(dic)
# for i in dic['results']:
#     for j in i['alternatives']:
#         print(j['transcript'])
# print(dic['results'][0]['alternatives'][0]['transcript'])

GUI.GUI()


