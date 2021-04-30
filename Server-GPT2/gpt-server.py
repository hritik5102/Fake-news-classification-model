from flask import Flask, request
from GPT2Inference import GPT2

app = Flask(__name__)
gptModel = GPT2()

@app.route('/')
def hello():
    return 'Welcome to the GPT server! \n use /predict[text] for prediction'

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    label = gptModel.predict(text)
    label = '' + str(label)
    return label

if __name__ == '__main__':
   app.run(debug = False, port=5000)