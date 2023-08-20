from flask import Flask, jsonify, request
import feedback_analysis
  
app = Flask(__name__)
  
@app.route('/', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
        data = "Feedback Analysis!"
        return jsonify({'data': data})
  
@app.route('/home/<string:fileName>', methods = ['GET'])
def disp(fileName):  
    summary = feedback_analysis.getFeedbackSummary(fileName)
    return jsonify({'data': summary})
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)



    