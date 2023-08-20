from flask import Flask, jsonify, request
import feedback_sentiment_analysis

app = Flask(__name__)
  
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "Analysis of My sessions feedback"
        return jsonify({'data': data})
  
  
@app.route('/getimprovements', methods = ['GET'])
def getImprovements(str):
    #improvements = feedback_sentiment_analysis.getSomething()
    improvements = feedback_sentiment_analysis.getImprovements(str)
    return jsonify({'data': listToString(improvements)})


def listToString(s):
    str1 = " " 
    return (str1.join(s))
  
if __name__ == '__main__':
  
    app.run(debug = True)