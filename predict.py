import pickle

f_name = 'model.bin'
with open(f_name,"rb") as f_in:
	(dv,model) = pickle.load(f_in)
	
from flask import Flask, request, jsonify

def predict_single(banana, dv, model):
    X = dv.transform(banana)
    y_pred = model.predict(X)
    return y_pred

app = Flask('churn')

def predict_multiple(banana_list, dv, model):
    """Predict multiple rows."""
    X = dv.transform(banana_list)
    y_pred = model.predict(X)
    return y_pred

@app.route('/predict', methods=['POST'])
def predict():
    banana = request.get_json()
    if not isinstance(banana, list):
        prediction = predict_single(banana, dv, model)
        
        if (prediction <= 1.5):
            quality_category = 'Unripe'
        elif (prediction>1.5 and prediction<=2.5):
            quality_category = 'Processing'
        elif (prediction >2.5 and prediction<=3.5):
            quality_category = 'Good'
        else:
            quality_category = 'Premium'
        
        result = {
            'quality_score': float(prediction),
            'quality_category': quality_category,
        }

        return jsonify(result)
    elif isinstance(banana, list):
        results = []
        predictions = predict_multiple(banana, dv, model)
        for banana, prediction in zip(banana, predictions):
            if prediction <= 1.5:
                quality_category = 'Unripe'
            elif 1.5 < prediction <= 2.5:
                quality_category = 'Processing'
            elif 2.5 < prediction <= 3.5:
                quality_category = 'Good'
            else:
                quality_category = 'Premium'

            results.append({
                'quality_score': float(prediction),
                'quality_category': quality_category,
            })

        return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)