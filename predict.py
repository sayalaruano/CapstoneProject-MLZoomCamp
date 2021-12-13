# Imports
import pickle

from flask import Flask
from flask import request
from flask import jsonify
import json
import pandas as pd

from Pfeature.pfeature import aac_wp

# Load the best ML model
model_file = 'ExtraTreesClassifier_maxdepth50_nestimators200.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

# Create a flask app
app = Flask('amps_prediction')

# Create a post method to receive requests
@app.route('/predict', methods=['POST'])
def predict():
    # Obtain information of the molecule to be predicted as a json file
    amp = request.get_json()

    amp_json = json.loads(amp)

    # Export the AMP sequence to a fasta file
    id = amp_json["ID"]
    sequence = amp_json["Sequence"]

    with open("sequence.fasta", "w") as f:
        f.write(id)
        f.write("\n")
        f.write(sequence)

    # Calculate Amino acid composition feature from the AMP 
    aac_wp("sequence.fasta", "aac_amp_test.csv")

    # Read the previous output 
    aac_amp_test = pd.read_csv("aac_amp_test.csv")

    # Make predictions with the best model 
    y_pred = model.predict_proba(aac_amp_test)[0, 1]
    active = y_pred >= 0.5

    # Save results 
    result = {
        'AMP activity': float(y_pred),
        'Active': bool(active)
    }

    # Convert results to a json file for posting them into a web service
    return jsonify(result)

# Run the app in the main 
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)