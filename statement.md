# Project Statement

## Project Title
**Student Performance Predictor**

## Problem Statement
Student outcomes are influenced by multiple factors including study time, attendance, previous academic performance, assignment performance and sleep. Estimating the likely outcome from several variables manually can be difficult. This project applies supervised machine learning to learn patterns from structured student-performance records and predict whether a student is likely to PASS or FAIL.

## Scope
The project covers the complete basic ML pipeline:
1. Load a structured CSV dataset.
2. Validate required data fields.
3. Prepare input features and target labels.
4. Split data into training and testing sets.
5. Train a Decision Tree classification model.
6. Evaluate the model with standard classification metrics.
7. Save the trained model.
8. Accept new student data and generate a PASS/FAIL prediction.

The system is an academic prototype and is not intended to make real institutional decisions.

## Target Users
- Students
- Faculty/academic users
- AIML learners
- Project evaluators

## High-Level Features
### 1. Data Loading
Reads the student-performance CSV and checks required columns.

### 2. Data Preprocessing
Selects the five model features and validates prediction inputs.

### 3. Machine Learning
Trains a Decision Tree classifier using an 80:20 stratified train/test split.

### 4. Model Evaluation
Calculates accuracy, precision, recall, F1-score and confusion matrix.

### 5. Prediction
Loads the saved model and predicts PASS/FAIL with confidence for a new student.

## Inputs
- Study hours per day
- Attendance percentage
- Previous marks percentage
- Assignment score percentage
- Sleep hours per day

## Output
- Predicted result: PASS or FAIL
- Prediction confidence

## Technology Stack
- Python
- Pandas
- Scikit-learn
- Pickle
- CSV

## Model
Decision Tree Classifier.

## Dataset
The project uses 1,000 structured records with five numerical input features and a binary result label. The included dataset is generated for academic demonstration.

## Expected Workflow
**Dataset → Validation → Feature Preparation → Train/Test Split → Decision Tree Training → Evaluation → Model Saving → New Student Input → Prediction**
