import requests


def check_profane(text_to_check):
    response = requests.get("https://www.purgomalum.com/service/containsprofanity?text=" + text_to_check)
    
    if response.text == True:


