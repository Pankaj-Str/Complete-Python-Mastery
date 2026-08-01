from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

model = joblib.load('model.pkl')

@app.route("/")

def home():
    return "Welcome to the Iris Classifier API!"


@app.route("/predict", methods=["POST"])
def predict():
    
    data = request.json
    
    prediction = model.predict(
        [
            [
                data["sepal_length"],
                data["sepal_width"],
                data["petal_length"],
                data["petal_width"]
            ]
        ]
    )
    return jsonify({"prediction": int(prediction[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)