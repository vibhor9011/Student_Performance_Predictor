import pandas as pd

FEATURES=["study_hours","attendance","previous_marks","assignment_score","sleep_hours"]
LIMITS={"study_hours":(0,24),"attendance":(0,100),"previous_marks":(0,100),"assignment_score":(0,100),"sleep_hours":(0,24)}
def prepare_data(df): return df[FEATURES],df["result"]
def validate_input(values):
    for name in FEATURES:
        value=float(values[name]); low,high=LIMITS[name]
        if not low<=value<=high: raise ValueError(f"{name} must be between {low} and {high}.")
def prepare_input(study_hours,attendance,previous_marks,assignment_score,sleep_hours):
    values=dict(study_hours=study_hours,attendance=attendance,previous_marks=previous_marks,assignment_score=assignment_score,sleep_hours=sleep_hours); validate_input(values)
    return pd.DataFrame([[float(values[n]) for n in FEATURES]], columns=FEATURES)
