import requests
import time
import os

subscription_key = ''
location = "eastus"

def get_token():
	token_url = "https://{}.api.cognitive.microsoft.com/sts/v1.0/issueToken".format(location)
	headers = {
		'Ocp-Apim-Subscription-Key' : subscription_key
	}
	response = requests.post(token_url, headers=headers)
	access_token = str(response.text)
	return access_token

def generate_speech(input_text, outfile, token):
	url = "https://{}.tts.speech.microsoft.com/cognitiveservices/v1".format(location)
	header = {
		'Authorization': 'Bearer '+str(token),
		'Content-Type': 'application/ssml+xml',
		'X-Microsoft-OutputFormat': 'audio-24khz-160kbitrate-mono-mp3'
	}

	'''
	You can customise your speech output here
	by changing language, gender and name
	'''
	data = "<speak version='1.0' xml:lang='en-US'>\
				<voice xml:lang='en-US' xml:gender='Female' name='en-US-AmberNeural'>\
					{}\
				</voice>\
		   </speak>".format(input_text)
	try:
		response = requests.post(url, headers=header, data=data)
		response.raise_for_status()
		with open(outfile, "wb") as file:
			file.write(response.content)
		print(response)
		response.close()
	except Exception as e:
		print("ERROR: ", e)

def convert_text_to_speech(text_to_convert):
	global outfile
	token = get_token() # Each Token is valid for 10 minutes
	generate_speech(text_to_convert, "output_mp3/test.mp3", token)

#convert_text_to_speech("Hello what are you doing today?")