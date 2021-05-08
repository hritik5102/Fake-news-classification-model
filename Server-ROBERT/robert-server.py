from flask import Flask, request
from RobertInference import Robert
app = Flask(__name__)
RobertModel = Robert()

@app.route('/')
def hello():
    return 'Welcome to the ROBERT server! \n\n use /predict[text] POST method for prediction'

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    label, loss  = RobertModel.predict(text)
    label = '' + str(label)
    return label

if __name__ == '__main__':
   app.run(debug = False, port=5500)