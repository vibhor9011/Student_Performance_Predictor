import os
import pandas as pd
FEATURES=["study_hours","attendance","previous_marks","assignment_score","sleep_hours"]
def load_data(path=None):
    if path is None: path=os.path.join(os.path.dirname(__file__),"..","data","student_performance.csv")
    path=os.path.abspath(path)
    if not os.path.exists(path): raise FileNotFoundError(f"Dataset not found: {path}")
    df=pd.read_csv(path); required=FEATURES+["result"]; missing=[c for c in required if c not in df.columns]
    if missing: raise ValueError(f"Missing columns: {missing}")
    return df.dropna(subset=required).reset_index(drop=True)
