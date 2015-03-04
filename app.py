from config import MY_NR, ACCOUNT_SID, AUTH_TOKEN
from twilio.rest import TwilioRestClient
import twilio.twiml
from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    recordings = client.recordings.list()
    return render_template('index.html', posts=recordings)


@app.route("/new", methods=['GET', 'POST'])
def new_post():
    from_number = request.values.get('From', None)
    resp = twilio.twiml.Response()

    if from_number == MY_NR:
        resp.say("Hi!")
        with resp.gather(numDigits=1, action="/handle-key", method="POST") as g:
            g.say("To record a post, press 1.")
        return str(resp)
    else:
        resp.say("Go away intruder!")
        return str(resp)


@app.route("/handle-key", methods=['GET', 'POST'])
def handle_key():
    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        resp = twilio.twiml.Response()
        resp.say("Record your post after the tone.")
        resp.record(maxLength="10", action="/handle-recording")
        return str(resp)
    else:
        return redirect("/new")


@app.route("/handle-recording", methods=['GET', 'POST'])
def handle_recording():
    resp = twilio.twiml.Response()
    resp.say("Your post is now live! Goodbye")
    return str(resp)


if __name__ == "__main__":
    app.run()