data = {
    "intent": {
        "code": 7110,
        "intentName": "",
        "actionName": ""
    },
    "results": [
        {
            "resultType": "text",
            "values": {
                "text": "你可不要带坏我呀。"
            },
            "groupType": 0
        }
    ]
}

print(data['results'][0]['values']['text'])
print(data.get('results'))