#!/usr/bin/env python
# coding: utf-8

# Imports
import pandas as pd
import json
import requests

# Parameters 
# If you want to run this service locally with docker, you 
# should use this url: http://localhost:9696/predict

url = 'https://amps-prediction.herokuapp.com/predict'

id = 'Sequence0019'

sequence = 'VFLDEFKNKEGEPMGVIIQKKDGGYLYTTTDIA'

# Create a json file of the AMP to be predicted 
amp = {
    "ID": "> " + id, 
    "Sequence": sequence
    }

amp_json = json.dumps(amp, indent=4)

# Create a post to the web service of activity prediction 
response = requests.post(url, json=amp_json).json()
print(response)

# Print steps that we need to follow according to the results 
if response['Active'] == True:
    print('The %s is an active AMP' % id)
else:
    print('The %s is a non-active AMP' % id)
