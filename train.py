#!/usr/bin/env python
# coding: utf-8

# Imports
## Data manipulation and EDA
import pandas as pd
import numpy as np

## Machine learning models
import pickle
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, f1_score, matthews_corrcoef
from sklearn.metrics import make_scorer

# Parameters
maxdepth = 50
nestimators = 200
n_splits = 5
output_file = f'ExtraTreesClassifier_maxdepth{maxdepth}_nestimators{nestimators}.bin'

# Data preparation
## Load feature matrix for training - Amino acid composition (dataset with the best performance)
aac_featmat = pd.read_csv('Data/aac_wp_training.csv', index_col=0)

## Extract y target variable - AMPs activity
y = aac_featmat['class'].copy()

# Encoding the target class label
y = y.map({"positive": 1, "negative": 0})

# Delete target column from the feature matrix
X = aac_featmat.drop('class', axis=1)

# Training 
print(f'Training the model')

etc_def = ExtraTreesClassifier(max_depth=maxdepth, n_estimators=nestimators, n_jobs=-1, 
                            random_state=10).fit(X, y)

# Validation

print(f'Doing validation')
print(f'Matthews correlation coefficient is used as performance metric')

cv_scores = cross_val_score(etc_def, X, y, cv=n_splits, 
                            scoring= make_scorer(matthews_corrcoef))

print('Validation results:')
print(f'ExtraTreesClassifier with max_depth={maxdepth} and n_estimators={nestimators}: \
    {np.mean(cv_scores):.2f} +- {np.std(cv_scores):.2f}')

# Predicting values with ExtraTreesClassifier model on test and external datasets
print(f'Doing evaluation on test and external datasets')

test = pd.read_csv('Data/aac_wp_test.csv', index_col=0)
external = pd.read_csv('Data/aac_wp_external.csv', index_col=0)

# Obtain test and external y, and encoding them
y_test = test['class'].copy()
y_test = y_test.map({"positive": 1, "negative": 0})

y_ext = external['class'].copy()
y_ext = y_ext.map({"positive": 1, "negative": 0})

# Obtain test and external feature matrices
X_test = test.drop('class', axis=1)
X_ext = external.drop('class', axis=1)

# Predicting values with the best model on test and external datasets
y_test_pred = etc_def.predict(X_test)
y_ext_pred = etc_def.predict(X_ext)

# Dataset to store performance metrics
results_bestMLmodel = pd.DataFrame()

# Calculate performance metrics
roc_auc_ext = roc_auc_score(y_ext, y_ext_pred)
    
roc_auc_test = roc_auc_score(y_test, y_test_pred)

acc_ext = accuracy_score(y_ext, y_ext_pred)

acc_test = accuracy_score(y_test, y_test_pred)

prec_ext = precision_score(y_ext, y_ext_pred)

prec_test = precision_score(y_test, y_test_pred)

recall_ext = recall_score(y_ext, y_ext_pred)

recall_test = recall_score(y_test, y_test_pred)

f1score_ext = f1_score(y_ext, y_ext_pred)

f1score_test = f1_score(y_test, y_test_pred)

mcc_ext = matthews_corrcoef(y_ext, y_ext_pred)

mcc_test = matthews_corrcoef(y_test, y_test_pred)

# Add columns to the dataset
results_bestMLmodel["Performance_metric"] = ['ROC_AUC','Accuracy', 'Precision', 
                                             'Recall', 'F1score', 'MCC']

results_bestMLmodel["Test_dataset"] = [roc_auc_test, acc_test, prec_test, 
                                       recall_test, f1score_test, mcc_test]

results_bestMLmodel["External_dataset"] = [roc_auc_ext, acc_ext, prec_ext, 
                                       recall_ext, f1score_ext, mcc_ext]

# Show the evaluation results of the best model
print(results_bestMLmodel.round(2))

# Save the model

with open(output_file, "wb") as f_out:
    pickle.dump(etc_def, f_out)

print(f'The model is saved to {output_file}')
