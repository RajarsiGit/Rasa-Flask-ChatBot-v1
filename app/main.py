from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = str(request.args.get('msg'))
    data = json.dumps({"sender" : "Rasa","message" : userText})
    headers = {'Content-type' : 'application/json', 'Accept' : 'text/plain'}
    response = requests.post('http://localhost:5005/webhooks/rest/webhook', data = data, headers = headers)
    response = response.json()
    return str(response[0]['text'])

if __name__ == "__main__":
	app.run(debug = True)