from flask import Flask, request
from biLSTMInference import BiLSTM

app = Flask(__name__)
bilstm = BiLSTM()

@app.route('/')
def hello():
    return 'Welcome to the LSTM server! \n\n use /predict[text] POST method for prediction'

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    label = bilstm.predict(text)
    label = '' + str(label)
    return label

if __name__ == '__main__':
   app.run(debug = False, port=7000)