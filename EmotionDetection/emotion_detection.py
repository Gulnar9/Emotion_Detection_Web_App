
import requests
import json
def emotion_detector(text_to_analyse):
    if not text_to_analyse.strip():
        return None      
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=input_json, headers=header)
    response_json = json.loads(response.text)
    emotions_dict = response_json["emotionPredictions"][0]["emotion"]
    max_emotion = max(emotions_dict, key=emotions_dict.get)
    output = {
                'anger': emotions_dict['anger'],
                'disgust': emotions_dict['disgust'],
                'fear': emotions_dict['fear'],
                'joy': emotions_dict['joy'],
                'sadness': emotions_dict['sadness'],
                'dominant_emotion': max_emotion
                } 
    if response.status_code == 200:    
        return output
    return {         
            'anger': None,
            'disgust': None, 
            'fear': None, 
            'joy': None, 
            'sadness': None, 
            'dominant_emotion': None
                    }                
       