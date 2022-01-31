from flask import Flask, request
from twilio import twiml
from date_time import get_now
from text_to_speech import convert_text_to_speech
import os
import time

# Receives texts that were sent to the Twilio # and logs them into Message Log.text
# Uses text_to_speech.py(Azure speech API) to convert the incoming text message to speech
# Requires ngrok on port 5000

app = Flask(__name__)
@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form['Body']
    print("You have a message from: " + str(number))
    print(message_body)
    log(number, message_body)

    convert_text_to_speech("You have a message from: " + number[2:])
    convert_text_to_speech(message_body)

    return str('Your message has been relayed.')


def log(phoneNum, message):
    with open('Twilio/Message Log.text', 'a') as logFile:
        logFile.write(get_now() + " -> " + str(phoneNum) + ": " + message + "\n")
        logFile.close() 


if __name__ == '__main__':
    app.run()
