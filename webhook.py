import json
from logging import debug
import os
import requests


from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)
    print(json.dumps(req, indent=4))

    res = makeResponse(req)
    res = json.dumps(res,indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeResponse(req):
    result = req.get("sessionInfo")
    parameters = result.get("parameters")
    person = parameters.get("person")
    date = '2021-11-16 00:00:00'#parameters.get("date")
    # url = 'http://api.openweathermap.org/data/2.5/forecast?q='+str(city)+'&appid=c1b2a448c14a73cf18d7713a9993c62d'
    # r = requests.get(url)
    # json_object = r.json()
    # weather = json_object['list']
    # for i in range(0,30):
    #     if date in weather[i]['dt_txt']:
    #         condition= weather[i]['weather'][0]['description']
    #         break
    # speech = "The forecast for"+city+ "for "+date+" is "+condition
    # #speech = "The forecast for"+city+"for "+date+" is "

    if person.get('name') == 'ünal':
        return {
            "fulfillment_response": {
                "messages": [
                {
                    "text": {
                    "text": [
                        "Web Service Result : bildirim var"
                    ]
                    }
                }
                ]
            },
            "sessionInfo": {
                "parameters": {
                    "bildirim": "YES"
                }
            }
        };
    else:
        return {
            "target_page": "projects/chatbot-lj9f/locations/us-central1/agents/daa60922-b192-483b-bcbb-03d39816d215/flows/00000000-0000-0000-0000-000000000000/pages/61457d28-b5d1-4c18-947d-3fd7b0412e8a",
            "fulfillment_response": {
                "messages": [
                {
                    "text": {
                    "text": [
                        "Web Service Result : bildirim yok"
                    ]
                    }
                }
                ]
            },
            "sessionInfo": {
                "parameters": {
                    "bildirim": "NO"
                }
            }
        };



if __name__ == '__main__':
    port = int(os.getenv('PORT',5000))
    print("Starting app on port %d" % port)
    app.run(debug=False, port=port, host='0.0.0.0')