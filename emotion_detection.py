import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }
    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    emotion = formatted_response['emotionPredictions'][0]['emotion']
    dominant = max(emotion, key=emotion.get)
    emotion['dominant_emotion'] = dominant

    
    # Returning a dictionary containing emotion detection results
    return emotion
    