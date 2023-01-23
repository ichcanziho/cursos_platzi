import numpy as np
from flask import Flask, app, request, jsonify
from core.utils import Utils

app = Flask(__name__)


# POSTMAN PARA PRUEBAS
@app.route('/predict', methods=['POST'])
def predict():
    args = dict(request.get_json())
    values = np.array(list(args.values()))
    values = values.reshape(1, -1)
    y_pred = model.predict(values)[0]
    y_pred = "presente" if y_pred else "ausente"
    return jsonify({"patologia_cardiaca": y_pred})


if __name__ == "__main__":
    model = Utils.load_model("models/best_model_0.992.pkl")
    app.run(port=8080, debug=True)
