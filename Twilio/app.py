from flask import Flask, request
from twilio import twiml
import os
from twilio.rest import Client

#account_sid = os.environ['TWILIO_ACCOUNT_SID']
#auth_token = os.environ['TWILIO_AUTH_TOKEN']
#client = Client(account_sid, auth_token)

app = Flask(__name__)
@app.route('/sms', methods=['POST'])


def sms():
    number = request.form['From']
    message_body = request.form['Body']
    print("You have a message from: " + number)
    print(message_body)


if __name__ == '__main__':
    app.run()
