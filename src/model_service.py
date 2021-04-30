import requests as req

PORT_GPT2 = '5000'
PORT_BERT = '5500'
PORT_LSTM = '7000'
BASE_URL = 'http://127.0.0.1:'
FUNC = '/predict'
def predict_from_server(text):

    data = {'text': text}
    a = req.post(BASE_URL + PORT_GPT2 + FUNC, data)
    b = req.post(BASE_URL + PORT_BERT+ FUNC, data) 
    c = req.post(BASE_URL + PORT_LSTM+ FUNC, data)  
    sum = int(a.text) + int(b.text) + int(c.text)
    return 1 if sum > 1 else 0