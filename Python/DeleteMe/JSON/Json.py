import json
from json2html import *


def createJson(obj):
    # obj = {
    #             "word": "behroooz",
    #             "type": "behrooz"
    #         }
    jsonStr = json.dumps(obj, ensure_ascii=False).encode('utf-8').decode()
    print(jsonStr)


def importFromFile(filename):
    f = open('/tmp/json.json')
    jData = json.load(f)
    return jData


def EditJson(filename):
    f = open('/tmp/Quran/Input.json')
    jData = json.load(f)
    # print(jData)

    for x in range(0, 6236):
        if jData[x]['SuraNumber'] == "003" and jData[x]['VerseNumber'] == "003":
            jData[x]['Farsi'] = "NewData"

    json_str = json.dumps(jData, ensure_ascii=False).encode('utf-8').decode()
    with open('/tmp/Quran/Output.json', 'w') as ff:
        ff.write(json_str)
    f.close()
    ff.close()


def toHtml(inputFileName, outputFileName):
    f = open(inputFileName)
    jData = json.load(f)
    data = json2html.convert(json={"data": jData})
    with open(outputFileName, 'w') as ff:
        ff.write(json.dumps(data, ensure_ascii=False).encode('utf-8').decode())
    f.close()
    ff.close()


# toHtml("/tmp/All.json", "/tmp/All.html")


def showData():
    json_string = '{ "1":"Red", "2":"Blue", "3":"Green"}'
    parsed_json = json.loads(json_string)
    print(parsed_json['2'])
