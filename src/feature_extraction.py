FEATURES=["study_hours","attendance","previous_marks","assignment_score","sleep_hours"]
def create_feature_row(study_hours,attendance,previous_marks,assignment_score,sleep_hours): return [[float(study_hours),float(attendance),float(previous_marks),float(assignment_score),float(sleep_hours)]]
def get_feature_names(): return FEATURES.copy()
