from flask import Flask, request
from BertInference import Bert_Classifier

app = Flask(__name__)
bertModel = Bert_Classifier(max_seq_len=150, lr=1e-5)

@app.route('/')
def hello():
    return 'Welcome to the BERT server! \n\n use /predict[text] POST method for prediction'

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    label, loss  = bertModel.predict(text)
    label = '' + str(label)
    return label

if __name__ == '__main__':
   app.run(debug = False, port=5500)