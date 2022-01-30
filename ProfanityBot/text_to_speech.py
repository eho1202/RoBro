from dotenv import load_dotenv
import os
import azure.cognitiveservices.speech as speechsdk
import time


def convert_text_to_speech(Text_to_Convert):
    Text_to_Convert = str(Text_to_Convert)
    file_location = "Twilio/Audio/I fucking cannot.wav"

    load_dotenv()
    Azure_Speech_Key = os.environ.get('AZURE_SPEECH_KEY')

    speech_config = speechsdk.SpeechConfig(subscription=Azure_Speech_Key, region="eastus")
    speech_config.speech_synthesis_language = "en-US"
    speech_config.speech_synthesis_voice_name = "en-US-AmberNeural"

    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    #audio_config = speechsdk.audio.AudioOutputConfig(filename=file_location)

    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    #synthesizer.start_speaking_text_async(Text_to_Convert)
    synthesizer.speak_text(Text_to_Convert)
