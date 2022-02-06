from flask import Flask,jsonify,request
from classifer import get_prediction
app=Flask(__name__)
@app.route("/predict-digit",methods=["Post"])

def predict_data():
    image=request.file.get("digit")
    prediction=get_prediction(image)
    return jsonify({
           "prediction":prediction
    }),200
    if __name__=='__main__':
         app.run(debug=True)