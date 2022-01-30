import requests
from text_to_speech import convert_text_to_speech


def check_profane(text_to_check):
    response = requests.get("https://www.purgomalum.com/service/containsprofanity?text=" + text_to_check)
    
    print(response.text)
    if response.text == "true":
        convert_text_to_speech("Watch your language.")

#check_profane("What are you doing?")