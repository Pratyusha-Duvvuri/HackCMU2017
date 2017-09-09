import requests
import json
 
def analyze_tone(text):
    username="1327224a-e09b-43aa-87b7-fe144ba4c80d"
    password="7IMqG4PiwvkL"
    watsonUrl = 'https://gateway.watsonplatform.net/tone-analyzer/api/v3/tone?version=2016-05-19'
    headers = {"content-type": "text/plain"}
    data = text
    try:
        r = requests.post(watsonUrl, auth=(username,password),headers = headers,
         data=data)
        return r.text
    except:
        return False
 
def welcome():
    message = "Welcome to the IBM Watson Tone Analyzer\n"
    print(message + "-" * len(message) + "\n")
    message = "How it works"
    print(message)
    message = "Perhaps a bit too aggressive in your emails? Are your blog posts a little too friendly? Tone Analyzer might be able to help. The service uses linguistic analysis to detect and interpret emotional, social, and writing cues found in text."
    print(message)
    print()
    print("Have fun!\n")

def calculateWithResults(data):
    data = json.loads(str(data))
    D={}
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        print("-" * len(i['category_name']))
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
        print()
    print() 

"""
Okay so the idea here is to put in 

"""

def display_results(data):
    data = json.loads(str(data))
    print(data,"PLPLPLPL")
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        print("-" * len(i['category_name']))
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
        print()
    print()
 
def display_results_fake(data):
    data = {'document_tone': {'tone_categories': [{'tones': [{'score': 0.088473, 'tone_id': 'anger', 'tone_name': 'Anger'}, {'score': 0.074744, 'tone_id': 'disgust', 'tone_name': 'Disgust'}, {'score': 0.091248, 'tone_id': 'fear', 'tone_name': 'Fear'}, {'score': 0.179551, 'tone_id': 'joy', 'tone_name': 'Joy'}, {'score': 0.148831, 'tone_id': 'sadness', 'tone_name': 'Sadness'}], 'category_id': 'emotion_tone', 'category_name': 'Emotion Tone'}, {'tones': [{'score': 0.0, 'tone_id': 'analytical', 'tone_name': 'Analytical'}, {'score': 0.0, 'tone_id': 'confident', 'tone_name': 'Confident'}, {'score': 0.0, 'tone_id': 'tentative', 'tone_name': 'Tentative'}], 'category_id': 'language_tone', 'category_name': 'Language Tone'}, {'tones': [{'score': 0.418265, 'tone_id': 'openness_big5', 'tone_name': 'Openness'}, {'score': 0.350009, 'tone_id': 'conscientiousness_big5', 'tone_name': 'Conscientiousness'}, {'score': 0.624531, 'tone_id': 'extraversion_big5', 'tone_name': 'Extraversion'}, {'score': 0.614692, 'tone_id': 'agreeableness_big5', 'tone_name': 'Agreeableness'}, {'score': 0.155482, 'tone_id': 'emotional_range_big5', 'tone_name': 'Emotional Range'}], 'category_id': 'social_tone', 'category_name': 'Social Tone'}]}}
    print(data,"PLPLPLPL")
    for i in data['document_tone']['tone_categories']:
        print(i['category_name'])
        print("-" * len(i['category_name']))
        for j in i['tones']:
            print(j['tone_name'].ljust(20),(str(round(j['score'] * 100,1)) + "%").rjust(10))
        print()
    print()


def main():
    welcome()
    data = input("Enter some text to be analyzed for tone analysis by IBM Watson (Q to quit):\n")
    display_results_fake

    if len(data) >= 1:
        if data == 'q'.lower():
            exit
        # display_results_fake("ad")
        
        results = analyze_tone(data)
        if results != False:
            display_results(results)
            exit
        else:
            print("Something went wrong")
 
main()