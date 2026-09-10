# Student Performance Predictor

**Student Performance Predictor** is a supervised machine-learning application that predicts whether a student is likely to **PASS or FAIL** using academic and lifestyle-related attributes.

### Project Objective
The objective is to demonstrate an end-to-end AIML workflow: loading structured data, validating and preparing features, training a classification model, evaluating its performance, saving the trained model, and using the model for new predictions.

## Features
- CSV dataset loading and validation
- Input validation and preprocessing
- Decision Tree classification
- PASS/FAIL prediction
- Prediction confidence
- Accuracy, precision, recall and F1-score
- Confusion matrix
- Modular six-file source structure
- Saved trained model using Python `pickle`
- Clear command-line interface

## Input Features
| Feature | Meaning | Range |
|---|---|---|
| `study_hours` | Study hours per day | 0–24 |
| `attendance` | Attendance percentage | 0–100 |
| `previous_marks` | Previous marks percentage | 0–100 |
| `assignment_score` | Assignment score percentage | 0–100 |
| `sleep_hours` | Sleep hours per day | 0–24 |

### Output
The system returns:
- **PASS** or **FAIL**
- Prediction confidence percentage

## Dataset
The included CSV contains **1,000 records**, five input features and one binary target:
- `1` = PASS
- `0` = FAIL

The dataset is a generated academic demonstration dataset. It should not be treated as real institutional student data.

## Machine Learning Approach
The project uses a **Decision Tree Classifier**. Decision Trees are appropriate for structured numerical data and are easy to interpret and explain during an academic demonstration.

Current training configuration:
- `max_depth = 20`
- `min_samples_leaf = 10`
- `random_state = 42`
- Test size = 20%
- Stratified train/test split

## Evaluation
Using the included dataset and the fixed 80:20 split:

- **Accuracy:** 82.00%
- **Precision:** 85.58%
- **Recall:** 80.91%
- **F1 Score:** 83.18%

Confusion matrix:
```text
[[75 15]
 [21 89]]
```

## Project Structure
```text
Student_Performance_Predictor/
├── data/
│   └── student_performance.csv
├── models/
│   └── student_model.pkl
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── feature_extraction.py
│   ├── train_model.py
│   ├── prediction.py
│   └── evaluation.py
├── docs/
│   ├── Project_Report.pdf
│   └── statement.md
├── requirements.txt
└── README.md
```

## Installation

Open CMD in the project root and run:

```cmd
python -m pip install -r requirements.txt
```

Or:

```cmd
python -m pip install pandas scikit-learn
```

## How to Run

### 1. Train the model
```cmd
python src\train_model.py
```

### 2. Run prediction
```cmd
python src\prediction.py
```

The prediction program asks for the five input values and displays the predicted result and confidence.

## Example
```text
===== STUDENT PERFORMANCE PREDICTOR =====
Study hours per day: 6
Attendance percentage: 85
Previous marks percentage: 78
Assignment score percentage: 80
Sleep hours per day: 7

Predicted Result: PASS
Confidence: ...
```

## Testing
The application handles:
- Missing dataset/model files
- Missing dataset columns
- Invalid numerical input
- Values outside the permitted range
- Normal prediction inputs

## VITyarthi Alignment
The project includes:
- Problem statement and objectives
- Functional and non-functional requirements
- Modular implementation
- Dataset description
- Model-selection rationale
- Evaluation methodology
- Structured source files
- Testing and future-enhancement documentation
- Project report and statement

## Limitations
This is an academic prototype. The generated dataset and model should not be used for real academic decisions.

## Future Enhancements
- Compare Random Forest, Logistic Regression and KNN
- Hyperparameter tuning and cross-validation
- Feature-importance visualization
- Web/GUI interface
- Prediction history
- Real-world anonymized dataset
- Multi-class performance prediction

## SCREENSHOTS
TRAIN MODEL
<img width="1614" height="335" alt="Screenshot 2026-09-05 212042" src="https://github.com/user-attachments/assets/7e0f5a89-f753-4700-9886-9ea69410f888" />
PREDICTION
<img width="1461" height="293" alt="Screenshot 2026-09-05 211416" src="https://github.com/user-attachments/assets/d59a9ed6-3411-4de9-8ea9-070264fe78f2" />


## Author
**Vibhor Srivastava**
25MIM10093
