import websockets
import asyncio
import base64
import json
from configure import auth_key
from quotes import selQuote
from magicbox import selmagicbox
import re
import pandas
import pyaudio

#Recording parameters - do not touch
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000
p = pyaudio.PyAudio()
 
#Recording start
stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	frames_per_buffer=FRAMES_PER_BUFFER
)
 
#Assembly URL and Dataframe of responses
URL = "wss://api.assemblyai.com/v2/realtime/ws?sample_rate=16000"
df = pandas.read_csv('response.csv')

#Finds phrase/word in text
def findCase(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search
async def send_receive():

	print(f'Connecting websocket to url ${URL}')

	async with websockets.connect(
		URL,
		extra_headers=(("Authorization", auth_key),),
		ping_interval=5,
		ping_timeout=20
	) as _ws:

		await asyncio.sleep(0.1)
		print("Receiving Session Begins ...")

		session_begins = await _ws.recv()
		print(session_begins)
		print("Sending messages ...")


		async def send():
			while True:
				try:
					data = stream.read(FRAMES_PER_BUFFER)
					data = base64.b64encode(data).decode("utf-8")
					json_data = json.dumps({"audio_data":str(data)})
					await _ws.send(json_data)

				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					assert False, "Not a websocket 4008 error"

				await asyncio.sleep(0.01)
		  
			return True
	  
# Main receiver function: Finds Phrase from csv file and outputs response and based on
# response, activates function from other scripts
		async def receive():
			while True:
				try:
					result_str = await _ws.recv()
					if json.loads(result_str)['message_type'] =='FinalTranscript':
						#print(json.loads(result_str)['text'])
						for index, row in df.iterrows():
							if findCase(row['Call'])(json.loads(result_str)['text']):
								if row['Response'] == 1:
									selQuote()
								if row['Response'] == 2:
									selmagicbox()
									

				except websockets.exceptions.ConnectionClosedError as e:
					print(e)
					assert e.code == 4008
					break

				except Exception as e:
					assert False, "Not a websocket 4008 error"
	  
		send_result, receive_result = await asyncio.gather(send(), receive())

while True:
	asyncio.run(send_receive())